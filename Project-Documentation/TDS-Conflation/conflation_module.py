import os
import sys
import warnings
import osmnx as ox
import networkx as nx
import pandas as pd
import geopandas as gpd
import getpass

user = getpass.getuser().lower()

MAPPYMATCH_PATH = f"/Users/{user}/Documents/GitHub/mappymatch"
sys.path.insert(0, MAPPYMATCH_PATH)

from mappymatch import package_root
from mappymatch.constructs.trace import Trace
from mappymatch.constructs.geofence import Geofence
from mappymatch.matchers.lcss.lcss import LCSSMatcher
from mappymatch.maps.nx.nx_map import NxMap, NetworkType
from shapely.geometry import LineString


def create_batch_traces(df, trip_id_column, xy=True):
    """Create a batch of traces from a dataframe with xy coordinates

    Args:
        df (Pandas Dataframe): Dataframe with xy coordinates in EPGS:4326.
        trip_id_column (String): Column name with unique trip ids.
        xy (bool, optional): Projects trace to EPSG:3857. Defaults to True.

    Returns:
        List: List of dictionaries with trip_id, trace, trace_gdf, and trace_line_gdf.
        Structure of the list:
        [
            {
                "trip_id": "unique_id",
                "trace": Trace object,
                "trace_gdf": GeoDataFrame with trace points,
                "trace_line_gdf": GeoDataFrame with trace line
            },
            ...
        ]
    """
    unique_ids = df[trip_id_column].unique()
    batch_traces = []
    for i in unique_ids:
        filter_df = df[df["trip_id"] == i]
        gdf = gpd.GeoDataFrame(
            filter_df, geometry=gpd.points_from_xy(filter_df.lon, filter_df.lat), crs=4326
        )
        batch_trace = Trace.from_geo_dataframe(frame=gdf, xy=xy)

        # create a trace_line_gdf from the trace
        coords = [(p.x, p.y) for p in batch_trace.coords]
        line = LineString(coords)
        trace_line_gdf = gpd.GeoDataFrame([{"geometry": line}], crs="EPSG:3857")
        trace_line_gdf["trip_id"] = i

        # create a trace_gdf from the trace
        trace_gdf = batch_trace._frame
        trace_gdf["trip_id"] = i

        # create a dictionary with the trip_id, trace, trace_gdf, and trace_line_gdf and append to the batch_traces list
        trace_dict = {
            "trip_id": i,
            "trace": batch_trace,
            "trace_gdf": trace_gdf,
            "trace_line_gdf": trace_line_gdf,
        }
        batch_traces.append(trace_dict)
    return batch_traces


def process_trace(trace_dict, geofence_buffer, network_type):
    """Process a single trace using the LCSS matcher.

    The function creates a geofence around each trace and creates a networkx graph from the geofence.
    Returns a matched trace dictionary.

    Args:
        trace_dict (dict): dictionary with trip_id and trace.
        geofence_buffer (int, optional): Buffer in meters. Defaults to 100.
        network_type (Enumerator, optional): Enumerator for Network Types supported by osmnx. Defaults to NetworkType.DRIVE.

    Returns:
        dict: dictionary with trip_id, trace, matched_result, matched_gdf, and matched_path_gdf.
        Structure of the dictionary:
        {
            "trip_id": trip_id,
            "trace": trace,
            "unmatched_trips": None or trip_id,
            "trace_gdf": trace_gdf,
            "trace_line_gdf": trace_line_gdf,
            "matched_result": match_result,
            "matched_gdf": matched_gdf,
            "matched_path_gdf": matched_path_gdf,
        }

    """

    try:
        # create a geofence around the trace
        geofence = Geofence.from_trace(trace_dict["trace"], padding=geofence_buffer)
        # create a networkx map from the geofence
        nx_map = NxMap.from_geofence(geofence, network_type=network_type)
        # match the trace to the map
        matcher = LCSSMatcher(nx_map)
        match_result = matcher.match_trace(trace_dict["trace"])
        # add full match result to the trace dictionary
        trace_dict["matched_result"] = match_result
        # matched_traces.append(trace_dict)
    except Exception as e:
        warnings.warn(
            f"The trace with trip_id {trace_dict['trip_id']} encountered an exception: {e}. Adding trip to the unmatched list."
        )
        trace_dict["unmatched_trips"] = trace_dict["trip_id"]
        return trace_dict
    # check if any road ids within a list of matches are null
    road_id_check = True
    for match in match_result.matches:
        if match.road is None:
            road_id_check = False
            break
    if road_id_check == False:
        warnings.warn(
            f"The trace with trip_id {trace_dict['trip_id']} has null road_ids meaning there was no match to the network. Adding to the unmatched list."
        )
        trace_dict["unmatched_trips"] = trace_dict["trip_id"]
    else:
        # create a geodataframe from the matches and add the trip_id; add the match result and matched df to the trace dictionary
        # print(trace_dict["trip_id"]) # debugging
        matched_df = match_result.matches_to_dataframe()
        matched_df["trip_id"] = trace_dict["trip_id"]
        matched_df["road_id"] = matched_df["road_id"]
        matched_gdf = gpd.GeoDataFrame(matched_df, geometry="geom", crs="EPSG:3857")
        # create a geodataframe from the matched path and add the trip_id; add the match result and matched df to the trace dictionary
        matched_path_df = match_result.path_to_dataframe()
        matched_path_df["trip_id"] = trace_dict["trip_id"]
        matched_path_df["road_id"] = matched_path_df["road_id"]
        matched_path_gdf = gpd.GeoDataFrame(matched_path_df, geometry="geom", crs="EPSG:3857")
        # add network attributes to the matched gdf and matched path gdf
        attrs = ["ref", "name", "maxspeed", "highway", "bridge", "tunnel"]
        for attr in attrs:
            # get attributes from the raw graph
            attr_dict = nx.get_edge_attributes(nx_map.g, attr)
            # add attributes to the matched gdf
            matched_gdf[attr] = matched_gdf["road_id"].map(attr_dict)
            # add attributes to the matched path gdf
            matched_path_gdf[attr] = matched_path_gdf["road_id"].map(attr_dict)
        # Set unmatched_trips to None and add matched_gdf and matched_path_gdf to the trace dictionary
        trace_dict["unmatched_trips"] = None
        trace_dict["matched_gdf"] = matched_gdf
        trace_dict["matched_path_gdf"] = matched_path_gdf

    return trace_dict


def batch_process_traces_parallel(traces, geofence_buffer=1000, network_type=NetworkType.DRIVE):
    """Batch process traces using the LCSS matcher in parallel using multiprocessing.

    Args:
        traces (List): list of dictionaries with trip_id and trace.
        geofence_buffer (int, optional): Buffer in meters. Defaults to 1000 meters.
        network_type (Enumerator, optional): Enumerator for Network Types supported by osmnx. Defaults to NetworkType.DRIVE.

    Returns:
        List: List of dictionaries with trip_id, trace, matched_result, matched_gdf, and matched_path_gdf.
        Structure of the list:
        [
            {
            "trip_id": trip_id,
            "trace": trace,
            "unmatched_trips": None or trip_id,
            "trace_gdf": trace_gdf,
            "trace_line_gdf": trace_line_gdf,
            "matched_result": match_result,
            "matched_gdf": matched_gdf,
            "matched_path_gdf": matched_path_gdf,
            },
        ...
        ]
    """
    import concurrent.futures

    matched_traces = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Prepare future tasks
        futures = [
            executor.submit(process_trace, trace, geofence_buffer, network_type) for trace in traces
        ]
        for future in concurrent.futures.as_completed(futures):
            matched_traces.append(future.result())
    return matched_traces


def concatenate_matched_gdfs(matched_traces, match_type="matched_gdf"):
    """Concatenate matched trace geodataframes into a single geodataframe.

    Args:
        matched_traces (List): List of dictionaries with matched trace geodataframes.
        match_type (String, optional): Type of match to concatenate. Defaults to "matched_gdf".
        Options are "matched_gdf", "matched_path_gdf", "trace_gdf".

    Returns:
        GeoDataFrame: Concatenated geodataframe.
    """
    matched_gdfs = []
    for trace_dict in matched_traces:
        # check if the match type is in the trace dictionary
        if match_type not in list(trace_dict.keys()):
            print(f"Match type {match_type} not found in trace dictionary. Skipping.")
            continue
        else:
            print(f"Match type {match_type} found in trace dictionary.")
            matched_gdfs.append(trace_dict[match_type])
    matched_gdf = pd.concat(matched_gdfs)

    # if values in the matched_gdf are lists, convert to strings
    for col in matched_gdf.columns:
        if matched_gdf[col].apply(lambda x: isinstance(x, list)).any():
            matched_gdf[col] = matched_gdf[col].apply(
                lambda x: "; ".join(x) if isinstance(x, list) else x
            )
    return matched_gdf


def write_matched_gdfs(match_result, file_path):
    """Write traces matched with the LCSS matcher to a geopackage.

    Args:
        match_result (List): List of dictionaries with matched trace geodataframes.
        file_path (String): path to the geopackage file.
    """
    trace_gdf = concatenate_matched_gdfs(match_result, match_type="trace_gdf")
    trace_line_gdf = concatenate_matched_gdfs(match_result, match_type="trace_line_gdf")
    matched_gdf = concatenate_matched_gdfs(match_result, match_type="matched_gdf")
    matched_path_gdf = concatenate_matched_gdfs(match_result, match_type="matched_path_gdf")

    # convert matched_gdf and matched_path_gdf "road_id" column from RoadId data type to string
    matched_gdf["road_id"] = matched_gdf["road_id"].astype(str)
    matched_path_gdf["road_id"] = matched_path_gdf["road_id"].astype(str)

    # write the trace_gdf, trace_line_gdf, matched_gdf, and matched_path_gdf to a geopackage
    trace_gdf.to_file(file_path, layer="trace_gdf", driver="GPKG")
    trace_line_gdf.to_file(file_path, layer="trace_line_gdf", driver="GPKG")
    matched_gdf.to_file(file_path, layer="matched_gdf", driver="GPKG")
    matched_path_gdf.to_file(file_path, layer="matched_path_gdf", driver="GPKG")


if __name__ == "__main__":