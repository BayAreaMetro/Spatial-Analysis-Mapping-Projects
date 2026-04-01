"""
SB79 Transit Oriented Development Upzoning — Pipeline Configuration
====================================================================
Centralised data source registry for the SB79 TOD pipeline.
Update file paths and URLs here when inputs change; all pipeline notebooks
reference this file so there is a single authoritative record of every
data source used across the project.

Pipeline steps (run in order; manual Excel review required after Step 2 before running Step 3):

  Step 1 — 1_gtfs_tod_stop_classification.ipynb
            Reads GTFS feed + Caltrans HQTS service, classifies TOD-applicable
            stops and assigns Tier 1 / Tier 2 designations, then exports
            stops, stations, and access_points to the shared GeoPackage.

  Step 2 — 2_tod_stop_and_access_assignment.ipynb
            Reads the curated stations and stops geodatabase layers, merges the
            per-agency pedestrian access-point source files (see constants below),
            spatially assigns stops and access points to parent stations via
            progressive buffer analysis, and exports development layers
            (tod_stations_dev, tod_stops_dev, tod_access_points_dev) to the
            shared GeoPackage, and writes REVIEW_XLSX_OUTPUT for manual review.
            After Step 2 completes: rename REVIEW_XLSX_OUTPUT by appending
            _reviewed_YYYY_MM_DD, update REVIEW_XLSX in config.py to point to
            the renamed file, resolve conflict/no_match rows, then run Step 3.

  Step 3 — 3_tod_station_assignment_reintegration.ipynb
            Reads REVIEW_XLSX, validates manually-assigned station_ids against
            the TOD station universe, applies updates to the _dev datasets, and
            exports final authoritative tod_stations, tod_stops, and
            tod_access_points layers to the shared GeoPackage.

  Step 4 — 4_tod_zone_buffer_generation.ipynb
            Generates TOD buffer zones from reviewed, station-assigned access
            points and exports final zone polygons to the shared GeoPackage.
"""

import getpass
from pathlib import Path

# ---------------------------------------------------------------------------
# Base data directory  (Box cloud storage, per-user path)
# ---------------------------------------------------------------------------
_user = getpass.getuser()
DATA_DIR = Path(
    f"/Users/{_user}/Library/CloudStorage/Box-Box/DSA Projects/"
    "Spatial Analysis and Mapping/SB79 Transit Oriented Development/Data"
)

# ---------------------------------------------------------------------------
# Step 1 inputs — GTFS + Caltrans HQTS
# ---------------------------------------------------------------------------

# Regional GTFS snapshot — update the filename when a new feed is downloaded
GTFS_ZIP = DATA_DIR / "GTFSTransitData_RG_2026_02_18.zip"

# Caltrans High-Quality Transit Stops (HQTS) — ArcGIS REST service
# Filtered to hqta_type = 'major_stop_brt' at query time
HQTS_URL = (
    "https://services3.arcgis.com/i2dkYWmb4wHvYPda/arcgis/rest/services/"
    "cdot_ca_hq_transit_stops/FeatureServer/0/query"
    "?outFields=*&where=hqta_type='major_stop_brt'&f=geojson"
)

# GTFS agencies included in this analysis
RELEVANT_AGENCIES = ["BA", "CT", "AC", "SC", "SF"]

# ---------------------------------------------------------------------------
# Step 2 inputs — manually curated station / stop / access-point data / overrides
# ---------------------------------------------------------------------------

# File geodatabase containing curated stops and stations
TOD_DATABASE_GDB = DATA_DIR / "tod_database_2026_04_01.gdb"
GDB_STATIONS_LAYER = "stations_v2"
GDB_STOPS_LAYER = "stops_v2"

# Excel spreadsheet listing station_ids to exclude from spatial assignment.
# Stations in this list are removed before buffer analysis so that stops and
# access points cannot be assigned to non-TOD stations.
STATIONS_OVERRIDES_XLSX = DATA_DIR / "2026_03_04_tod_stations_overrides.xlsx"
STATION_OVERRIDES_SHEET = "stations"

# ---------------------------------------------------------------------------
# Step 2 inputs — per-agency pedestrian access point source files
# ---------------------------------------------------------------------------
# Each agency delivers access points in its own format (shapefile or GDB).
# Notebook 2 merges these into a single GeoDataFrame before spatial assignment.
# Set the path to the file/GDB for each agency; for GDB sources also set the
# corresponding layer name.  Leave unused layer names as None.

ACCESS_PTS_DIR = DATA_DIR / "Access Points"

# BART (BA)
ACCESS_PTS_BA_PATH = ACCESS_PTS_DIR / "BART_PedAccessPoints_GTFS_v3.zip"
ACCESS_PTS_BA_LAYER = None  # layer name if GDB, else None

# Caltrain (CT)
ACCESS_PTS_CT_PATH = ACCESS_PTS_DIR / "Caltrain_PedAccessPoints_GTFS_v6_updated_fields.zip"
ACCESS_PTS_CT_LAYER = None  # layer name if GDB, else None

# AC Transit (AC)
ACCESS_PTS_AC_PATH = ACCESS_PTS_DIR / "AC_Transit_PedAcessPoints_v3.gdb"
ACCESS_PTS_AC_LAYER = "ACTransit_PedAccessPoints_GTFS_v3"

# VTA / Santa Clara (SC)
ACCESS_PTS_SC_PATH = ACCESS_PTS_DIR / "VTA_PedAccessPoints_GTFS_v5.zip"
ACCESS_PTS_SC_LAYER = None  # layer name if GDB, else None

# SFMTA / Muni (SF)
ACCESS_PTS_SF_PATH = ACCESS_PTS_DIR / "SFMuni_PedAccessPoints_GTFS_v2.zip"
ACCESS_PTS_SF_LAYER = None  # layer name if GDB, else None

# Valley Link (VL)
ACCESS_PTS_VL_PATH = ACCESS_PTS_DIR / "ValleyLink_PedAccessPoints_v1.zip"
ACCESS_PTS_VL_LAYER = None  # layer name if GDB, else None

# Ordered list used by notebook 2 to iterate over sources
ACCESS_PTS_SOURCES = [
    ("BA", ACCESS_PTS_BA_PATH, ACCESS_PTS_BA_LAYER),
    ("CT", ACCESS_PTS_CT_PATH, ACCESS_PTS_CT_LAYER),
    ("AC", ACCESS_PTS_AC_PATH, ACCESS_PTS_AC_LAYER),
    ("SC", ACCESS_PTS_SC_PATH, ACCESS_PTS_SC_LAYER),
    ("SF", ACCESS_PTS_SF_PATH, ACCESS_PTS_SF_LAYER),
    ("VL", ACCESS_PTS_VL_PATH, ACCESS_PTS_VL_LAYER),
]

# ---------------------------------------------------------------------------
# Step 4 inputs — jurisdiction boundaries and ACS population data
# ---------------------------------------------------------------------------

# Bay Area jurisdiction boundaries (incorporated places + unincorporated county
# lands).  ArcGIS REST FeatureService — region_jurisdiction (public).
JURISDICTION_BOUNDARIES_URL = (
    "https://services3.arcgis.com/i2dkYWmb4wHvYPda/arcgis/rest/services/"
    "region_jurisdiction/FeatureServer/0/query"
    "?outFields=*&where=1%3D1&f=geojson"
)

WATER_BODIES_URL = (
    "https://services3.arcgis.com/i2dkYWmb4wHvYPda/arcgis/rest/services/"
    "region_water_area/FeatureServer/0/query"
    "?f=geojson&where=(wfcc%20IN%20('H2053'%2C%20'H2051'))&outFields=*"
)

# ACS 5-year estimates (2019–2023), Table B01003 — Total Population
# Used to apply the SB79 jurisdictional population threshold (35,000 residents).
# Pulled via mtcpy.census.pull_acs_data at the Census "place" geography level.
ACS_YEAR = 2023  # endpoint year of the 5-year estimate window
ACS_TYPE = "acs5"  # 5-year ACS product
ACS_TABLE_ID = "B01003"  # Total Population
ACS_GEOGRAPHY_LEVEL = "place"  # incorporated places (cities/CDPs)

# ---------------------------------------------------------------------------
# Shared output — GeoPackage written to by all pipeline steps
# ---------------------------------------------------------------------------

TOD_DATABASE_GPKG = DATA_DIR / "SB79_tod_database.gpkg"

# Layer names written by Step 1
GPKG_STOPS_LAYER = "stops"
GPKG_STATIONS_LAYER = "stations"
GPKG_ACCESS_PTS_LAYER = "access_points"

# Development layers written by Step 2 (in-progress, not authoritative)
GPKG_TOD_STATIONS_DEV_LAYER = "tod_stations_dev"
GPKG_TOD_STOPS_DEV_LAYER = "tod_stops_dev"
GPKG_TOD_ACCESS_PTS_DEV_LAYER = "tod_access_points_dev"

# Step 4 output — linkage gap review workbook written when stops or access points
# are missing a corresponding match. Only created when gaps exist.
LINKAGE_GAPS_XLSX = DATA_DIR / "tod_linkage_gaps_review_v1.xlsx"

# Step 2 output — Step 2 always writes to this fixed filename.
# After Step 2 completes, rename this file by appending _reviewed_YYYY_MM_DD
# (e.g. SB79_tod_review_reviewed_2026_03_10.xlsx) so a future re-run of
# Step 2 cannot overwrite your manual edits.
REVIEW_XLSX_OUTPUT = DATA_DIR / "SB79_tod_review.xlsx"

# UPDATE BEFORE RUNNING STEP 3:
# Set this to the path of the renamed/reviewed workbook.
# Example: DATA_DIR / "SB79_tod_review_2026_03_10.xlsx"
REVIEW_XLSX = DATA_DIR / "SB79_tod_review_2026_03_20.xlsx"  # replace YYYY_MM_DD
REVIEW_STOPS_SHEET = "stops"
REVIEW_ACCESS_PTS_SHEET = "access_points"

# Final authoritative layers written by Step 3
GPKG_TOD_STATIONS_FINAL_LAYER = "tod_stations"
GPKG_TOD_STOPS_FINAL_LAYER = "tod_stops"
GPKG_TOD_ACCESS_PTS_FINAL_LAYER = "tod_access_points"

# Pre-resolution buffer layer written by Step 4 — one full-circle buffer per
# access point per band; tier precedence, jurisdictional rules, and ring
# differencing are applied downstream.
GPKG_TOD_ZONE_BUFFERS_LAYER = "tod_zone_buffers"
GPKG_JURISDICTIONS_WITH_POP_LAYER = "jurisdictions_with_pop_acs2019_2023"

# Final resolved TOD zone layer (written by a future downstream step)
GPKG_TOD_ZONES_LAYER = "tod_zones"
