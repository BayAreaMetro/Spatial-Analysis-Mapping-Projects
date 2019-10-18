import arcpy
import os

#Define the workspace
arcpy.env.workspace = r"\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\PDA_Analysis.gdb"

#Allow features and files to be overwritten 
arcpy.env.overwriteOutput = True

# Create function to select specific fields to map when using field mapping for a geoprocessing function
def issolate_fields(output_fields, field_mappings):
	for field in field_mappings.fields:
		if field.name not in output_fields:
			field_mappings.removeFieldMap(field_mappings.findFieldMapIndex(field.name))

# Create function to all fields from feature classes to a field mapping object
def add_fields(feature_classes, field_mappings):
	for fc in feature_classes:
		field_mappings.addTable(fc)

# Create function to multiple fields using a dictionary
def rename_fields(fc, namesDict, clearAlias):
	for fieldName in namesDict:
		arcpy.management.AlterField(fc, fieldName, namesDict[fieldName], clear_field_alias = clearAlias)

# Summarize PDAs within PDA Eligible Areas Feature Class
pda_fc = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\Growth_Framework_Analysis_Areas.gdb\Regional_PDA_2019_Repaired'
in_sum_features = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\Growth_Framework_Analysis_Areas.gdb\PDA_Eligible_Areas'
out_feature_class = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\Growth_Framework_Analysis_Areas.gdb\Draft_Regional_PDA_2019_Eligibility'
group_field = 'Designation'
out_group_table = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\Growth_Framework_Analysis_Areas.gdb\Draft_Regional_PDA_2019_Eligibility_Designation'

summarize_within_args = {'in_polygons': pda_fc,
'in_sum_features': in_sum_features,
'out_feature_class': out_feature_class,
'keep_all_polygons': True,
'sum_fields': None,
'sum_shape': True,
'shape_unit': 'ACRES',
'group_field': group_field,
'add_min_maj': False,
'add_group_percent': True,
'out_group_table':out_group_table}

arcpy.SummarizeWithin_analysis(**summarize_within_args)

# Rename fields in join table created based on PDA Eligible Areas Designation field

names_dict = {'SUM_area_ACRES':'Acres_Intersect','PercentArea':'Percent_Intersect'}
clear_alias = 'TRUE'

rename_fields(out_group_table,names_dict,clear_alias)

# Join to PDA summary feature class created as result of Sumarize Within step
join_args = {'in_layer_or_view': out_feature_class,
'in_field': 'Join_ID',
'join_table': out_group_table,
'join_field': 'Join_ID',
'join_type': 'KEEP_ALL'
}

pda_elig_join = arcpy.AddJoin_management(**join_args)

# Copy joined table to file geodatabase
join_output_location = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\Growth_Framework_Analysis_Areas.gdb'
join_output_table = r'Draft_Regional_PDA_Designation_2019'
elg_analysis_field_mapping = arcpy.FieldMappings()
elg_analysis_final_fields = ['County','Jurisdiction','PDA_Name', 'PDA_Changes_2019','Designation','Acres_Intersect','Percent_Intersect']

elg_analysis_field_mapping.addTable(pda_elig_join)

issolate_fields(elg_analysis_final_fields, elg_analysis_field_mapping)

#arcpy.TableToTable_conversion(pda_elig_join, join_output_location, join_output_table, None, elg_analysis_field_mapping)

fc_to_fc_args = {'in_features': pda_elig_join,
'out_path':join_output_location,
'out_name':join_output_table,
'where_clause': None,
'field_mapping':elg_analysis_field_mapping
}

arcpy.FeatureClassToFeatureClass_conversion(**fc_to_fc_args)

# Add field for eligibility flag
add_field_args = {'in_table': join_output_table,
'field_name': 'Eligibility',
'field_type': 'TEXT',
'field_precision': None,
'field_length': None,
'field_length': 50,
'field_alias': 'Eligibility',
'field_is_nullable': 'NULLABLE',
'field_is_required': 'NON_REQUIRED',
'field_domain': None}

arcpy.management.AddField(**add_field_args)

# Calculate eligibility field to determine if PDAs meet criteria of 50% or more within eligibility area 
expression = 'eligible_flag(!Percent_Intersect!)'
code_block = """ 
def eligible_flag(percentage):
	if percentage is None:
		return 'Does Not Meet Eligibility Criteria'
	elif percentage >= 50:
		return 'Meets Eligibility Criteria'
	else:
		return 'Does Not Meet Eligibility Criteria'"""

arcpy.management.CalculateField(join_output_table, "Eligibility", expression, "PYTHON3", code_block)

# Write report to csv
output_folder = r'C:\Users\mtcgis\Box\GIS (shapefiles)\PPA_Analysis'
output_csv = r'Draft_Regional_PPA_2019_Eligibility_Analysis.csv'

arcpy.TableToTable_conversion(join_output_table, output_folder, output_csv)









