#This script is meant to be run within the ArcPro Arcpy analysis window

import arcpy, os

#Set path to fgdb containing analysis layers and fgdb for final output 

analysisfgdb = r"\\Mac\Home\Documents\ArcGIS\Packages\SB35_Data_Analysis\p20\sb35_data_analysis.gdb"
resultfgdb = r"\\Mac\Home\Documents\Planning\SB 35 Mapping Overlay\SB35_Data_Analysis\SB35_Datasets.gdb"

#Create list of feature classes in analysis fgdb 

feature_classes = []
walk = arcpy.da.Walk(analysisfgdb, datatype="FeatureClass", type="All")

for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        feature_classes.append(os.path.join(dirpath, filename))

#Union all features in feature class list

unionresult = resultfgdb + r"\SB_35_Exclusion_Areas_v3" 
print(unionresult)

arcpy.analysis.Union(feature_classes, unionresult, "ALL", None, "GAPS")

#Make feature layer from urbanized tracts gdb feature class 

urbanizedtracts = r"\\Mac\Home\Documents\Planning\SB 35 Mapping Overlay\SB35_Data_Analysis\SB35_Datasets.gdb\tl_2017_us_uac10_BayArea"
arcpy.MakeFeatureLayer_management(urbanizedtracts,"tl_2017_us_uac10_BayArea")

#Run identity operation on SB 35 Exclusion Areas and Urbanized Census tracts per legislation (legeslation applies to urbanized tract areas)

identresult = resultfgdb + r"\SB_35_Exclusion_Areas_Urbanized_v3"
arcpy.Identity_analysis("tl_2017_us_uac10_BayArea","SB_35_Exclusion_Areas_v3",identresult, join_attributes = "ONLY_FID")


#Add field to indicate if area is an exclusion area or urbanized area 

arcpy.AddField_management("SB_35_Exclusion_Areas_Urbanized_v3", "Exclusion_Area","LONG",field_alias="Exclusion Area",field_length = 10)

#Calculate value of exclusion area field (1 - Urbanized Area: Within One or More Exclusion Areas; 2 - Urbanized Area - Not Within Exclusion Areas)
arcpy.management.CalculateField("SB_35_Exclusion_Areas_Urbanized_v3", "Exclusion_Area", "exclusionarea(!FID_SB_35_Exclusion_Areas_v3!)", "PYTHON_9.3", r"def exclusionarea(fid_exclusion):\n    if fid_exclusion == -1:\n        return 2\n    else:\n        return 1\n    ")

#Dissolve exclusion area by exclusion area status

dissresult = resultfgdb + r"\SB_35_Exclusion_Areas_Simplified_v3"
arcpy.Dissolve_management("SB_35_Exclusion_Areas_Urbanized_v3",dissresult,"Exclusion_Area")

