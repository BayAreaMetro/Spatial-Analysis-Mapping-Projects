import os
import getpass

# Define user
user = getpass.getuser()

# Define file name
location_tbl = "location.csv"
trip_tbl = "trip.csv"

# Define Box System Root Directory
box_dir = os.path.join("/Users", user, "Library", "CloudStorage", "Box-Box")

# Define BAUS directory on Box for .csv output files
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

# Define input file paths
location_path = os.path.join(file_dir, location_tbl)
trip_path = os.path.join(file_dir, trip_tbl)

# Define output file paths
out_file_path = os.path.join(
    box_dir, "DataViz Projects", "Spatial Analysis and Mapping", "TDS Conflation", "Data"
)
gpkg_path = os.path.join(out_file_path, "tds_conflation_results.gpkg")
