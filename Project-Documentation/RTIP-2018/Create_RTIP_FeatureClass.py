#This script is meant to be run in the ArcGIS Pro Python Window

#Add the following web layers to your project (Add Data From Path)

# http://services3.arcgis.com/i2dkYWmb4wHvYPda/arcgis/rest/services/2040_Regional_Transportation_Projects_Polygon/FeatureServer 
# http://services3.arcgis.com/i2dkYWmb4wHvYPda/arcgis/rest/services/2040_Regional_Transportation_Projects_Line/FeatureServer
# http://services3.arcgis.com/i2dkYWmb4wHvYPda/arcgis/rest/services/2040_Regional_Transportation_Projects_Point/FeatureServer

#Add connection to GISDB2 webGIS RPD user

#Create geodatabase table from RTIP Excel Project List 
arcpy.conversion.ExcelToTable(r"C:\Users\mtcgis\Box\DataViz Projects\Spatial Analysis and Mapping\RTIP 2018\RTIP Project Map info.xlsx", r"\\Mac\Home\Documents\Programming and Allocations\RTIP_2018\RTIP_2018.gdb\RTIPProjectMapinfo_ExcelToTaRTIPProjectMapinfo_ExcelToTa", "Project List")

#Join RTIP projects to RTP project geometries for projects with RTP IDs and export to new feature class 

arcpy.management.AddJoin(r"2040_Regional_Transportation_Projects_Point\RTP.dbo.arcgis_point_VW", "rtpId", "RTIPProjectMapinfo_ExcelToTa", "RTP_ID", "KEEP_COMMON")

arcpy.management.CopyFeatures(r"2040_Regional_Transportation_Projects_Point\RTP.dbo.arcgis_point_VW", r"\\Mac\Home\Documents\Programming and Allocations\RTIP_2018\RTIP_2018.gdb\RTIP_RTP_Project_Points", None, None, None, None) 

arcpy.management.AddJoin(r"2040_Regional_Transportation_Projects_Line\RTP.dbo.arcgis_line_VW", "rtpId", "RTIPProjectMapinfo_ExcelToTa", "RTP_ID", "KEEP_COMMON")

arcpy.management.CopyFeatures(r"2040_Regional_Transportation_Projects_Line\RTP.dbo.arcgis_line_VW", r"\\Mac\Home\Documents\Programming and Allocations\RTIP_2018\RTIP_2018.gdb\RTIP_RTP_Project_Lines", None, None, None, None)

#Add RTIP projects mapped using project mapper from the project mapper db and export to new feature class
arcpy.management.MakeQueryLayer(r"\\Mac\Home\Documents\Programming and Allocations\RTIP_2018\gisdb2.c4ttzt2cz0de.us-west-2.rds.amazonaws.com.sde", "RTIP_PM_Project_Points", r"SELECT ID,WKT,Shape,Project,_id,Date FROM WebGIS.rpd.MapApplicatonData\nWHERE Project = 'TIP' AND WKT LIKE 'POINT%' ", "ID", "POINT", 4326, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;.001;.001;IsHighPrecision")

arcpy.management.CopyFeatures("WebGIS.rpd.MapApplicatonData", r"\\Mac\Home\Documents\Programming and Allocations\RTIP_2018\RTIP_2018.gdb\RTIP_PM_Project_Points", None, None, None, None)

arcpy.management.MakeQueryLayer(r"\\Mac\Home\Documents\Programming and Allocations\RTIP_2018\gisdb2.c4ttzt2cz0de.us-west-2.rds.amazonaws.com.sde", "RTIP_PM_Project_Lines", r"SELECT ID,WKT,Shape,Project,_id,Date FROM WebGIS.rpd.MapApplicatonData\nWHERE Project = 'TIP' AND WKT LIKE 'LINE%' ", "ID", "POLYLINE", 4326, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;.001;.001;IsHighPrecision")

#Add TIP projects from TIP DB, and export to new feature class
arcpy.management.MakeQueryLayer(r"\\Mac\Home\Documents\Programming and Allocations\RTIP_2018\gisdb2.c4ttzt2cz0de.us-west-2.rds.amazonaws.com.sde", "RTIP_TIP_Projects_Points", "select OBJECTID,PROJ_SEQ,TIP_ID,PROJ_NAME,PROJ_DESCRIPTION,AGENCY_CDE,SYSTEM_CDE,COUNTY_CDE,TOTAL_PROJECT_COST,MAPPING_STATUS,MAP_ID,Shape from WebGIS.rpd.TIP_POINTS_2017", "OBJECTID", "POINT", 26910, "PROJCS['NAD_1983_UTM_Zone_10N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-123.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]];-5120900 -9998100 10000;-100000 10000;-100000 10000;.001;.001;.001;IsHighPrecision")

##Select by attributes vs. where clause in query layer due to issues with mixed feature types in table; entire tip table could be added but software would not recognize feature type when selecting from subset using where clause.
arcpy.management.SelectLayerByAttribute("RTIP_TIP_Projects_Points", "NEW_SELECTION", "TIP_ID IN ('CC-110082','NAP150001','SOL150003')", None)

arcpy.management.CopyFeatures("RTIP_TIP_Projects_Points", r"\\Mac\Home\Documents\Programming and Allocations\RTIP_2018\RTIP_2018.gdb\RTIP_TIP_Projects_Points", None, None, None, None)

arcpy.management.MultipartToSinglepart("RTIP_TIP_Project_Points", r"\\Mac\Home\Documents\Programming and Allocations\RTIP_2018\RTIP_2018.gdb\RTIP_TIP_Project_Points_Mult")

arcpy.management.MakeQueryLayer(r"\\Mac\Home\Documents\Programming and Allocations\RTIP_2018\gisdb2.c4ttzt2cz0de.us-west-2.rds.amazonaws.com.sde", "RTIP_TIP_Projects_Lines", r"select OBJECTID,PROJ_SEQ,TIP_ID,PROJ_NAME,PROJ_DESCRIPTION,AGENCY_CDE,SYSTEM_CDE,COUNTY_CDE,TOTAL_PROJECT_COST,MAPPING_STATUS,MAP_ID,Shape from WebGIS.rpd.TIP_LINES_2017\nWHERE TIP_ID IN ('CC-110082','NAP130006','NAP150001','NAP130008','SM-070002','SCL150001','SOL150003')", "OBJECTID", "POLYLINE", 26910, "PROJCS['NAD_1983_UTM_Zone_10N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-123.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]];-5120900 -9998100 10000;-100000 10000;-100000 10000;.001;.001;.001;IsHighPrecision")

arcpy.management.CopyFeatures("RTIP_TIP_Projects_Lines", r"\\Mac\Home\Documents\Programming and Allocations\RTIP_2018\RTIP_2018.gdb\RTIP_TIP_Projects_Lines", None, None, None, None)

#Merge all RTIP point features 
arcpy.management.Merge("RTIP_TIP_Project_Points_Mult;RTIP_PM_Project_Points;RTIP_RTP_Project_Points", r"\\Mac\Home\Documents\Programming and Allocations\RTIP_2018\RTIP_2018.gdb\RTIP_2018_Project_Points", 'TIP_ID "TIP_ID" true true false 9 Text 0 0,First,#,RTIP_TIP_Project_Points_Mult,TIP_ID,0,9;PM_ID "ID" true true false 60 Text 0 0,First,#,RTIP_PM_Project_Points,PM_ID,0,60;L0RTP_dbo_arcgis_point_VW_rtpId "RTP_ID" true true false 20 Text 0 0,First,#,RTIP_RTP_Project_Points,L0RTP_dbo_arcgis_point_VW_rtpId,0,20')

#Merge all RTIP line features 
arcpy.management.Merge("RTIP_TIP_Projects_Lines;RTIP_PM_Project_Lines;RTIP_RTP_Project_Lines_V2", r"\\Mac\Home\Documents\Programming and Allocations\RTIP_2018\RTIP_2018.gdb\RTIP_2018_Project_Lines_V2", 'TIP_ID "TIP_ID" true true false 9 Text 0 0,First,#,RTIP_TIP_Projects_Lines,TIP_ID,0,9;PM_ID "ID" true true false 60 Text 0 0,First,#,RTIP_PM_Project_Lines,PM_ID,0,60,RTIP_PM_Project_Lines,PM_ID,0,60;RTP_ID "rtpId" true true false 20 Text 0 0,First,#,RTIP_RTP_Project_Lines,RTP_ID,0,20')

#Add source field to each RTIP feature class
arcpy.management.AddField("RTIP_2018_Project_Points", "Source", "TEXT", None, None, None, "Source", "NULLABLE", "NON_REQUIRED", None)

arcpy.management.AddField("RTIP_2018_Project_Lines_V2", "Source", "TEXT", None, None, None, "Source", "NULLABLE", "NON_REQUIRED", None)

#Update field names
arcpy.management.AlterField("RTIP_2018_Project_Points", "PM_ID", "PM_ID", "PM_ID", "TEXT", 60, "NULLABLE", False)

arcpy.management.AlterField("RTIP_2018_Project_Lines_V2", "PM_ID", "PM_ID", "PM_ID", "TEXT", 60, "NULLABLE", False)

#Add source
arcpy.management.CalculateField("RTIP_2018_Project_Points", "Source", "add_source(!TIP_ID!,!PM_ID!,!L0RTP_dbo_arcgis_point_VW_rtpId!)", "PYTHON_9.3", r"def add_source(tipid, pmid, rtpid):\n    if tipid is not None:\n        return 'TIP'\n    elif pmid is not None:\n        return 'PM'\n    else:\n        return 'RTP'\n    ")

arcpy.management.CalculateField("RTIP_2018_Project_Lines_V2", "Source", "add_source(!TIP_ID!,!PM_ID!,!RTP_ID!)", "PYTHON_9.3", r"def add_source(tipid, pmid, rtpid):\n    if tipid is not None:\n        return 'TIP'\n    elif pmid is not None:\n        return 'PM'\n    else:\n        return 'RTP'\n    ")

#Add Join_ID field 
arcpy.management.AddField("RTIP_2018_Project_Lines_V2", "Join_ID", "TEXT", None, None, None, "Join_ID", "NULLABLE", "NON_REQUIRED", None)

arcpy.management.AddField("RTIP_2018_Project_Points", "Join_ID", "TEXT", None, None, None, "Join_ID", "NULLABLE", "NON_REQUIRED", None)

#Add join id
arcpy.management.CalculateField("RTIP_2018_Project_Points", "Join_ID", "add_join_id(!TIP_ID!,!PM_ID!,!L0RTP_dbo_arcgis_point_VW_rtpId!)", "PYTHON_9.3", r"def add_join_id(tipid, pmid, rtpid):\n    if tipid is not None:\n        return tipid\n    elif pmid is not None:\n        return pmid\n    else:\n        return rtpid\n    ")

arcpy.management.CalculateField("RTIP_2018_Project_Lines_V2", "Join_ID", "add_join_id(!TIP_ID!,!PM_ID!,!RTP_ID!)", "PYTHON_9.3", r"def add_join_id(tipid, pmid, rtpid):\n    if tipid is not None:\n        return tipid\n    elif pmid is not None:\n        return pmid\n    else:\n        return rtpid\n    ")

#Add Join_ID field to project list table 
arcpy.management.AddField("RTIP_2018_Project_List", "Join_ID", "TEXT", None, None, None, "Join_ID", "NULLABLE", "NON_REQUIRED", None)

#add join id to project list table 
arcpy.management.CalculateField("RTIP_2018_Project_List", "Join_ID", "add_join_id(!TIP_ID!,!PM_ID!,!RTP_ID!)", "PYTHON_9.3", r"def add_join_id(tipid, pmid, rtpid):\n    if pmid is not '':\n        return pmid\n    elif tipid is not '' and rtpid is '':\n        return tipid\n    else:\n        return rtpid\n    ")

#Join projects to RTIP project list 











