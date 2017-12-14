#This script is meant to be run in the ArcGIS Pro Python Window

#Add the following web layers to your project (Add Data From Path)

# http://services3.arcgis.com/i2dkYWmb4wHvYPda/arcgis/rest/services/2040_Regional_Transportation_Projects_Polygon/FeatureServer 
# http://services3.arcgis.com/i2dkYWmb4wHvYPda/arcgis/rest/services/2040_Regional_Transportation_Projects_Line/FeatureServer
# http://services3.arcgis.com/i2dkYWmb4wHvYPda/arcgis/rest/services/2040_Regional_Transportation_Projects_Point/FeatureServer

#Create geodatabase table from RTIP Excel Project List 
arcpy.conversion.ExcelToTable(r"C:\Users\mtcgis\Box\DataViz Projects\Spatial Analysis and Mapping\RTIP 2018\RTIP Project Map info.xlsx", r"\\Mac\Home\Documents\Programming and Allocations\RTIP_2018\RTIP_2018.gdb\RTIPProjectMapinfo_ExcelToTa", "Project List")

#Join RTIP projects to RTP project geometries for projects with RTP IDs and export to new feature class 

arcpy.management.AddJoin(r"2040_Regional_Transportation_Projects_Point\RTP.dbo.arcgis_point_VW", "rtpId", "RTIPProjectMapinfo_ExcelToTa", "RTP_ID", "KEEP_COMMON")

arcpy.management.CopyFeatures(r"2040_Regional_Transportation_Projects_Point\RTP.dbo.arcgis_point_VW", r"\\Mac\Home\Documents\Programming and Allocations\RTIP_2018\RTIP_2018.gdb\RTIP_RTP_Project_Points", None, None, None, None) 

arcpy.management.AddJoin(r"2040_Regional_Transportation_Projects_Line\RTP.dbo.arcgis_line_VW", "rtpId", "RTIPProjectMapinfo_ExcelToTa", "RTP_ID", "KEEP_COMMON")

arcpy.management.CopyFeatures(r"2040_Regional_Transportation_Projects_Line\RTP.dbo.arcgis_line_VW", r"\\Mac\Home\Documents\Programming and Allocations\RTIP_2018\RTIP_2018.gdb\RTIP_RTP_Project_Lines", None, None, None, None)







