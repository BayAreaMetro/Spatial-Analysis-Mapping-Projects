"""
SB79 Transit Oriented Development Upzoning — Pipeline Configuration
====================================================================
Centralised data source registry for the SB79 TOD pipeline.
Update file paths and URLs here when inputs change; all pipeline notebooks
reference this file so there is a single authoritative record of every
data source used across the project.

Pipeline steps (run in order; ⚠️  manual GIS review required after Step 2 before running Step 3):

  Step 1 — 1_gtfs_tod_stop_classification.ipynb
            Reads GTFS feed + Caltrans HQTS service, classifies TOD-applicable
            stops and assigns Tier 1 / Tier 2 designations, then exports
            stops, stations, and access_points to the shared GeoPackage.

  Step 2 — 2_tod_stop_and_access_assignment.ipynb
            Reads the curated stations and stops geodatabase layers, merges the
            per-agency pedestrian access-point source files (see constants below),
            spatially assigns stops and access points to parent stations via
            progressive buffer analysis, and exports review layers to the shared
            GeoPackage.
            ⚠️  Requires manual GIS review of tod_stops_review_v1 and
            tod_access_review_v1 before proceeding to Step 3.

  Step 3 — 3_tod_station_assignment_reintegration.ipynb
            Reads the manually-reviewed conflict/orphan layers, applies valid
            assignments back to the main stop and access-point datasets, and
            re-exports corrected tod_stops and tod_access_points layers.

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
TOD_DATABASE_GDB = DATA_DIR / "tod_database.gdb"
GDB_STATIONS_LAYER = "stations_v1"
GDB_STOPS_LAYER = "stops_v1"

# Excel spreadsheet containing access point assignment overrides and station removals
OVERRIDES_XLSX = DATA_DIR / "2026.3.4_TOD_data_review.xlsx"
ACCESS_OVERRIDES_SHEET = "accesspoints"
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
ACCESS_PTS_BA_PATH = ACCESS_PTS_DIR / "BART_PedAccessPoints_GTFS_v1.zip"
ACCESS_PTS_BA_LAYER = None  # layer name if GDB, else None

# Caltrain (CT)
ACCESS_PTS_CT_PATH = ACCESS_PTS_DIR / "Caltrain_PedAccessPoints_GTFS_v3.zip"
ACCESS_PTS_CT_LAYER = None  # layer name if GDB, else None

# AC Transit (AC)
ACCESS_PTS_AC_PATH = ACCESS_PTS_DIR / "AC_Transit_PedAcessPoints_v3.gdb"
ACCESS_PTS_AC_LAYER = "ACTransit_PedAccessPoints_GTFS_v3"

# VTA / Santa Clara (SC)
ACCESS_PTS_SC_PATH = ACCESS_PTS_DIR / "VTA_PedAccessPoints_GTFS_v2.zip"
ACCESS_PTS_SC_LAYER = None  # layer name if GDB, else None

# SFMTA / Muni (SF)
ACCESS_PTS_SF_PATH = ACCESS_PTS_DIR / "SFMuni_PedAccessPoints_GTFS_v1.zip"
ACCESS_PTS_SF_LAYER = None  # layer name if GDB, else None

# Ordered list used by notebook 2 to iterate over sources
ACCESS_PTS_SOURCES = [
    ("BA", ACCESS_PTS_BA_PATH, ACCESS_PTS_BA_LAYER),
    ("CT", ACCESS_PTS_CT_PATH, ACCESS_PTS_CT_LAYER),
    ("AC", ACCESS_PTS_AC_PATH, ACCESS_PTS_AC_LAYER),
    ("SC", ACCESS_PTS_SC_PATH, ACCESS_PTS_SC_LAYER),
    ("SF", ACCESS_PTS_SF_PATH, ACCESS_PTS_SF_LAYER),
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

# ACS 5-year estimates (2019–2023), Table B01003 — Total Population
# Used to apply the SB79 jurisdictional population threshold (35,000 residents).
# Pulled via mtcpy.census.pull_acs_data at the Census "place" geography level.
ACS_YEAR = 2023           # endpoint year of the 5-year estimate window
ACS_TYPE = "acs5"         # 5-year ACS product
ACS_TABLE_ID = "B01003"   # Total Population
ACS_GEOGRAPHY_LEVEL = "place"  # incorporated places (cities/CDPs)

# ---------------------------------------------------------------------------
# Shared output — GeoPackage written to by all pipeline steps
# ---------------------------------------------------------------------------

TOD_DATABASE_GPKG = DATA_DIR / "SB79_tod_database.gpkg"

# Layer names written by Step 1
GPKG_STOPS_LAYER = "stops"
GPKG_STATIONS_LAYER = "stations"
GPKG_ACCESS_PTS_LAYER = "access_points"

# Layer names written by Step 2
GPKG_TOD_STATIONS_LAYER = "tod_stations"
GPKG_TOD_STOPS_LAYER = "tod_stops"
GPKG_TOD_ACCESS_PTS_LAYER = "tod_access_points"

# Review layers exported by Step 2 (pre-manual-review)
# These are overwritten each time Step 2 runs.
GPKG_TOD_STOPS_REVIEW_LAYER = "tod_stops_review"
GPKG_TOD_ACCESS_REVIEW_LAYER = "tod_access_review"

# Review layers read by Step 3 (post-manual-review)
# After reviewing tod_stops_review / tod_access_review in GIS, save the
# corrected layers under these names before running Step 3.
GPKG_TOD_STOPS_REVIEWED_LAYER = "tod_stops_review_v1"
GPKG_TOD_ACCESS_REVIEWED_LAYER = "tod_access_review_v1"

# Layer name written by Step 4
GPKG_TOD_ZONES_LAYER = "tod_zones"
