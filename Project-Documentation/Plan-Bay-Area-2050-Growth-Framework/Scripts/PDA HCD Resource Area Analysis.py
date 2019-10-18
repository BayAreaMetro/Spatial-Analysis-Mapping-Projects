import arcpy
import os

#Define the workspace
arcpy.env.workspace = r"\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\PDA_Analysis.gdb"

#Allow features and files to be overwritten 
arcpy.env.overwriteOutput = True

# Tabluate intersection between Regional PDA 2019 feature class and PDA Eligible Areas Feature Class
in_zone_features = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\Growth_Framework_Analysis_Areas.gdb\priority_development_areas_current_project'
zone_fields = ['Jurisdiction', 'County', 'PDA_Name']
input_class_fc = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\Growth_Framework_Analysis_Areas.gdb\CTCAC_HCD_Resource_Opportunity_Areas_BayArea_2019_Project'
output_table = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\PDA_Analysis.gdb\Current_PDA_Resource_Opportunity_Area_Analysis_All_PDAs'
class_field = 'Final_Category'
out_units = 'ACRES'

tabulate_args = {'in_zone_features': in_zone_features,
'zone_fields': zone_fields,
'in_class_features': input_class_fc,
'out_table': output_table,
'class_fields': class_field,
'sum_fields': None,
'xy_tolerance': None,
'out_units': out_units}

try:
	arcpy.analysis.TabulateIntersection(**tabulate_args)
except Exception:
	e = sys.exc_info()[1]
	print(e.args[0])


# Rename fields 
def rename_fields(fc, namesDict, clearAlias):
	for fieldName in namesDict:
		arcpy.management.AlterField(fc, fieldName, namesDict[fieldName], clear_field_alias = clearAlias)

names_dict = {'AREA':'Acres','PERCENTAGE':'Percentage'}
clear_alias = 'TRUE'

rename_fields(output_table,names_dict,clear_alias)

# Write report to csv
output_folder = r'C:\Users\mtcgis\Box\GIS (shapefiles)'
output_csv = r'Current_PDA_Resource_Opportunity_Area_Analysis.csv'

arcpy.TableToTable_conversion(output_table, output_folder, output_csv)