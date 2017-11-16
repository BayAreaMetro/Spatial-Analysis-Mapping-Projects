# This script should be run in the ArcGIS Pro Python window 

# Create multi-part features for OBAG Lines

arcpy.management.MultipartToSinglepart("RPD_OBAG_2_Project_Lines_11_07_2017", r"\\Mac\Home\Documents\Programming and Allocations\OBAG\OBAG_2_Mapping\OBAG_2_Mapping.gdb\RPD_OBAG_2_Project_Lines_11_07_2017_multi")

# Create multi-part features for OBAG Points 

arcpy.management.MultipartToSinglepart("RPD_OBAG_2_Project_Points_11_07_2017", r"\\Mac\Home\Documents\Programming and Allocations\OBAG\OBAG_2_Mapping\OBAG_2_Mapping.gdb\RPD_OBAG_2_Project_Points_11_07_2017_multi")

# Created PDA status coded domain 

arcpy.management.CreateDomain(r"\\Mac\Home\Documents\Programming and Allocations\OBAG\OBAG_2_Mapping\OBAG_2_Mapping.gdb", "PDA_status", None, "LONG", "CODED", "DEFAULT", "DEFAULT")

domainDict = {1: 'Within PDA', 2: 'Touches PDA', 3: 'Within 1/2 Mile of PDA', 4: 'Within 1 Mile of PDA', 5: 'Outside PDA'}

for key, value in domainDict.items():
	print(value) 
	arcpy.management.AddCodedValueToDomain(r"\\Mac\Home\Documents\Programming and Allocations\OBAG\OBAG_2_Mapping\OBAG_2_Mapping.gdb", "PDA_status", key, value) 

# Add PDA status audit field for OBAG Lines 

arcpy.management.AddField("RPD_OBAG_2_Project_Lines_11_07_2017_multi", "PDA_status_audit", "LONG", 0, None, None, None, "NULLABLE", "NON_REQUIRED", "PDA_status")

# Add PDA status audit field to for OBAG Points

arcpy.management.AddField("RPD_OBAG_2_Project_Points_11_07_2017_multi", "PDA_status_audit", "LONG", 0, None, None, None, "NULLABLE", "NON_REQUIRED", "PDA_status")

# Select and update PDA status by attribute / location for OBAG Lines 

arcpy.management.SelectLayerByLocation("RPD_OBAG_2_Project_Lines_11_07_2017_multi", "WITHIN", r"Priority_Development_Areas_(current)\Priority_Development_Areas_(current)", None, "NEW_SELECTION", "NOT_INVERT")

arcpy.management.CalculateField("RPD_OBAG_2_Project_Lines_11_07_2017_multi", "PDA_status_audit", 1, "PYTHON_9.3", None)

arcpy.management.SelectLayerByLocation("RPD_OBAG_2_Project_Lines_11_07_2017_multi", "CROSSED_BY_THE_OUTLINE_OF", r"Priority_Development_Areas_(current)\Priority_Development_Areas_(current)", None, "NEW_SELECTION", "NOT_INVERT")

arcpy.management.CalculateField("RPD_OBAG_2_Project_Lines_11_07_2017_multi", "PDA_status_audit", 2, "PYTHON_9.3", None)

arcpy.management.SelectLayerByAttribute("RPD_OBAG_2_Project_Lines_11_07_2017_multi", "NEW_SELECTION", "PDA_status_audit IS NULL", None)

arcpy.management.SelectLayerByLocation("RPD_OBAG_2_Project_Lines_11_07_2017_multi", "WITHIN_A_DISTANCE", r"Priority_Development_Areas_(current)\Priority_Development_Areas_(current)", ".5 Miles", "SUBSET_SELECTION", "NOT_INVERT")

arcpy.management.CalculateField("RPD_OBAG_2_Project_Lines_11_07_2017_multi", "PDA_status_audit", 3, "PYTHON_9.3", None)

arcpy.management.SelectLayerByAttribute("RPD_OBAG_2_Project_Lines_11_07_2017_multi", "NEW_SELECTION", "PDA_status_audit IS NULL", None)

arcpy.management.SelectLayerByLocation("RPD_OBAG_2_Project_Lines_11_07_2017_multi", "WITHIN_A_DISTANCE", r"Priority_Development_Areas_(current)\Priority_Development_Areas_(current)", "1 Miles", "SUBSET_SELECTION", "NOT_INVERT")

arcpy.management.CalculateField("RPD_OBAG_2_Project_Lines_11_07_2017_multi", "PDA_status_audit", 4, "PYTHON_9.3", None)

arcpy.management.SelectLayerByAttribute("RPD_OBAG_2_Project_Lines_11_07_2017_multi", "NEW_SELECTION", "PDA_status_audit IS NULL", None)

arcpy.management.CalculateField("RPD_OBAG_2_Project_Lines_11_07_2017_multi", "PDA_status_audit", 5, "PYTHON_9.3", None)

# Select and update PDA status by attribute / location for OBAG Points

arcpy.management.SelectLayerByLocation("RPD_OBAG_2_Project_Points_11_07_2017_multi", "WITHIN", r"Priority_Development_Areas_(current)\Priority_Development_Areas_(current)", None, "NEW_SELECTION", "NOT_INVERT")

arcpy.management.CalculateField("RPD_OBAG_2_Project_Points_11_07_2017_multi", "PDA_status_audit", 1, "PYTHON_9.3", None)

arcpy.management.SelectLayerByAttribute("RPD_OBAG_2_Project_Points_11_07_2017_multi", "NEW_SELECTION", "PDA_status_audit IS NULL", None)

arcpy.management.SelectLayerByLocation("RPD_OBAG_2_Project_Points_11_07_2017_multi", "WITHIN_A_DISTANCE", r"Priority_Development_Areas_(current)\Priority_Development_Areas_(current)", ".5 Miles", "SUBSET_SELECTION", "NOT_INVERT")

arcpy.management.CalculateField("RPD_OBAG_2_Project_Points_11_07_2017_multi", "PDA_status_audit", 3, "PYTHON_9.3", None)

arcpy.management.SelectLayerByAttribute("RPD_OBAG_2_Project_Points_11_07_2017_multi", "NEW_SELECTION", "PDA_status_audit IS NULL", None)

arcpy.management.SelectLayerByLocation("RPD_OBAG_2_Project_Points_11_07_2017_multi", "WITHIN_A_DISTANCE", r"Priority_Development_Areas_(current)\Priority_Development_Areas_(current)", "1 Miles", "SUBSET_SELECTION", "NOT_INVERT")

arcpy.management.CalculateField("RPD_OBAG_2_Project_Points_11_07_2017_multi", "PDA_status_audit", 4, "PYTHON_9.3", None)

arcpy.management.SelectLayerByAttribute("RPD_OBAG_2_Project_Points_11_07_2017_multi", "NEW_SELECTION", "PDA_status_audit IS NULL", None)

arcpy.management.CalculateField("RPD_OBAG_2_Project_Points_11_07_2017_multi", "PDA_status_audit", 5, "PYTHON_9.3", None)







