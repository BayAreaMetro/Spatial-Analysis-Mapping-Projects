import arcpy
import os

#Define the workspace
arcpy.env.workspace = r"\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\PDA_Analysis.gdb"

#Allow features and files to be overwritten 
arcpy.env.overwriteOutput = True

# Tabluate intersection between Regional PDA 2019 feature class and PDA Eligible Areas Feature Class
in_zone_features = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\Growth_Framework_Analysis_Areas.gdb\priority_development_areas_current_project'
zone_fields = ['PDA_Name','Jurisdiction']
input_class_fc = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\Growth_Framework_Analysis_Areas.gdb\PDA_Eligible_Areas'
output_table = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\PDA_Analysis.gdb\Current_Regional_PDA_Eligibility_Analysis'
class_fields = 'Designation'
out_units = 'ACRES'

tabulate_args = {'in_zone_features': in_zone_features,
'zone_fields': zone_fields,
'in_class_features': input_class_fc,
'out_table': output_table,
'class_fields': class_fields,
'sum_fields': None,
'xy_tolerance': None,
'out_units': out_units}

try:
	arcpy.analysis.TabulateIntersection(**tabulate_args)
except Exception:
	e = sys.exc_info()[1]
	print(e.args[0])

# Add field for eligibility flag

add_field_args = {'in_table': output_table,
'field_name': 'Eligible',
'field_type': 'TEXT',
'field_precision': None,
'field_length': None,
'field_length': 50,
'field_alias': 'Eligible',
'field_is_nullable': 'NULLABLE',
'field_is_required': 'NON_REQUIRED',
'field_domain': None}

arcpy.management.AddField(**add_field_args)

# Calculate eligibility field to determine if PDAs meet criteria of 50% or more within eligibility area 
expression = 'eligible_flag(!PERCENTAGE!)'
code_block = """ 
def eligible_flag(percentage):
    if percentage >= 50:
        return 'Meets Eligibility Criteria'
    else:
        return 'Does Not Meet Eligibility Criteria'"""

arcpy.management.CalculateField(output_table, "Eligible", expression, "PYTHON3", code_block)

# Rename fields 
def rename_fields(fc, namesDict, clearAlias):
	for fieldName in namesDict:
		arcpy.management.AlterField(fc, fieldName, namesDict[fieldName], clear_field_alias = clearAlias)

names_dict = {'Designatio':'Designation','AREA':'Acres','PERCENTAGE':'Percentage'}
clear_alias = 'TRUE'

rename_fields(output_table,names_dict,clear_alias)

# Write report to csv
output_folder = r'C:\Users\mtcgis\Box\GIS (shapefiles)'
output_csv = r'Current_Regional_PDA_Eligibility_Analysis.csv'

arcpy.TableToTable_conversion(output_table, output_folder, output_csv)









