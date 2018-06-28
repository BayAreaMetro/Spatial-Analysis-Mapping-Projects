# This script is meant to be run within the Python analysis window within the ArcGIS Pro Desktop environment

# Create surface from intersection level walkscore data with a cell size of 30m 

out_raster = arcpy.sa.Idw(r"\\Mac\Home\Documents\Planning\PDA_Single_Family_Neighborhoods\BayArea_Walkscore_Intersections_2017.gdb\BayArea_WalkScore_Intersection_Level_2017", "walkscore", 30, 2, "VARIABLE 12", None); out_raster.save(r"\\Mac\Home\Documents\Planning\PDA_Single_Family_Neighborhoods\Single_Family_Neighborhood_Analysis.gdb\BayArea_Walkscore_Surface_IDW_30m")

# Summarize the values of the walkscore raster by parcel using parcel_id as the zone. Output results to a fgdb table. 

arcpy.sa.ZonalStatisticsAsTable(r"\\Mac\Home\Documents\Planning\PDA_Single_Family_Neighborhoods\Parcels 2010 Final PBA40 Version.gdb\parcels2010", "Parcel_ID_Text", "BayArea_Walkscore_Surface_IDW_30m", r"\\Mac\Home\Documents\Planning\PDA_Single_Family_Neighborhoods\Single_Family_Neighborhood_Analysis.gdb\Parcels_Walkscore_Table", "DATA", "MEAN")