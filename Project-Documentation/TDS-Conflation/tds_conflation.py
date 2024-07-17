# Travel Diary Survey Conflation
#
# Notebook for Exploratory Data Analysis (EDA) only. Final code will be refactored into a python utilities module and script to run the conflation process.

# %% [markdown]
# ## How to run this notebook
#
# 1. Install the required package dependencies using the [requirements.txt](requirements/requirements.txt) file.
# 2. Clone the [mappymatch github repository](https://github.com/BayAreaMetro/mappymatch), which has been forked and modified from the original repository.
# 3. Update the MAPPYMATCH_PATH below to point to the location of the cloned repository.

import os
import sys
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

# ## Define functions

# create a batch process function to create a list of traces


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
    from shapely.geometry import LineString

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


# create a function that takes a list of traces and batch processes them using the LCSS matcher


def batch_process_traces(traces, geofence_buffer=1000, network_type=NetworkType.DRIVE):
    """Batch process traces using the LCSS matcher.

    The function creates a geofence around each trace and creates a networkx graph from the geofence.
    Returns a list of matched traces.

    Args:
        traces (List): list of dictionaries with trip_id and trace.
        geofence_buffer (int, optional): Buffer in meters. Defaults to 100.
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
    import osmnx as ox
    import networkx as nx
    import warnings

    processed_trip_count = 0
    matched_traces = []
    for trace_dict in traces:
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
            matched_traces.append(trace_dict)
        except Exception as e:
            warnings.warn(
                f"The trace with trip_id {trace_dict['trip_id']} encountered an exception: {e}. Adding trip to the unmatched list."
            )
            trace_dict["unmatched_trips"] = trace_dict["trip_id"]
            matched_traces.append(trace_dict)
            continue

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
        # processed_trip_count += 1
        # print(f"Processed {processed_trip_count} trips.")

    return matched_traces


def process_trace(trace_dict, geofence_buffer, network_type):
    """_summary_

    Args:
        trace_dict (_type_): _description_
        geofence_buffer (_type_): _description_
        network_type (_type_): _description_
    """
    # create a function that takes a single trace and processes it using the LCSS matcher

    import osmnx as ox
    import networkx as nx
    import warnings

    # processed_trip_count = 0
    # matched_traces = []
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
    """_summary_

    Args:
        traces (_type_): _description_
        geofence_buffer (int, optional): _description_. Defaults to 1000.
        network_type (_type_, optional): _description_. Defaults to NetworkType.DRIVE.

    Returns:
        _type_: _description_
    """
    import concurrent.futures

    matched_traces = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
        # Prepare future tasks
        futures = [
            executor.submit(process_trace, trace, geofence_buffer, network_type) for trace in traces
        ]
        for future in concurrent.futures.as_completed(futures):
            matched_traces.append(future.result())
    return matched_traces


# create a function that takes a list of dictionaries with matched trace geodataframes, concatenates them, and returns a single geodataframe


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


# define a function to concatenate matched gdfs and write each match type to geopackage


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


# ## Prepare the data

## Define file name
location_tbl = "location.csv"
trip_tbl = "trip.csv"

## Define Box System Root Directory
box_dir = os.path.join("/Users", user, "Library", "CloudStorage", "Box-Box")

## Define BAUS directory on Box for .csv output files
file_dir = os.path.join(
    box_dir,
    "Modeling and Surveys",
    "Surveys",
    "Travel Diary Survey",
    "Biennial Travel Diary Survey",
    "Data",
    "2023",
    "Full Unweighted 2023 Dataset",
)

location_path = os.path.join(file_dir, location_tbl)
trip_path = os.path.join(file_dir, trip_tbl)

# read location and trip
location_df = pd.read_csv(location_path)
trip_df = pd.read_csv(trip_path)

# merge trips with locations
trip_locations = pd.merge(
    location_df,
    trip_df[
        [
            "trip_id",
            "o_in_region",
            "d_in_region",
            "mode_type",
            "mode_1",
            "mode_2",
            "mode_3",
            "mode_4",
        ]
    ],
    on="trip_id",
)

trip_locations.head()

# filter trips_locations to only include trips with mode 8 in mode_1 or mode_2 or mode_3 or mode_4 columns with origins and destinations in region
car_trips = trip_locations[
    ((trip_locations["mode_type"].isin([5, 6, 8, 9, 11]))) & (trip_locations["o_in_region"] == 1)
    | (trip_locations["d_in_region"] == 1)
]

unique_trips = car_trips["trip_id"].unique()

print("Unique trip count " + str(unique_trips.shape[0]))

# # create batch traces from the test list
# test_list = [
#     2304076901001, #highway
#     2333407402028, #highway
#     2304076901002, #highway
#     2347455701047, #highway
#     # 2333407402031, #might be too long
#     2333407402037,
#     2333413601001, # issue with the trace - missing geometry
# ]
# select top 1000 trips from unique trip list
test_list = unique_trips[:20]
car_trips_test = car_trips[car_trips["trip_id"].isin(test_list)]
batch_traces_test = create_batch_traces(car_trips_test, trip_id_column="trip_id", xy=True)
# batch_traces = create_batch_traces(car_trips, trip_id_column="trip_id", xy=True)

# ## Match using the LCSS matching algorithm

match_result_test = batch_process_traces_parallel(
    batch_traces_test, geofence_buffer=1000, network_type=NetworkType.DRIVE
)

match_result = batch_process_traces(
    traces=batch_traces_test, geofence_buffer=1000, network_type=NetworkType.DRIVE
)

# write the matched gdfs to a geopackage
out_file_path = f"/Users/{user}/Library/CloudStorage/Box-Box/DataViz Projects/Spatial Analysis and Mapping/TDS Conflation/Data"
gpkg_path = os.path.join(out_file_path, "tds_conflation_results.gpkg")
write_matched_gdfs(match_result, gpkg_path)
