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
in_sum_features = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\Growth_Framework_Analysis_Areas.gdb\PDA_Eligible_Areas_11_7_19'
out_feature_class = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\Growth_Framework_Analysis_Areas.gdb\Draft_Regional_PDA_2019_Eligibility'
group_field = 'Designation'
out_group_table = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\Growth_Framework_Analysis_Areas.gdb\Draft_Regional_PDA_2019_Eligibility_Designation_Summary_Table'

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

names_dict = {'Join_ID':'Summary_ID','SUM_area_ACRES':'Acres_Intersect','PercentArea':'Percent_Intersect'}
clear_alias = 'TRUE'

rename_fields(out_group_table,names_dict,clear_alias)

# Join to PDA summary feature class created as result of Sumarize Within step
in_layer = 'Draft_Regional_PDA_2019_Eligibility'
join_table = 'Draft_Regional_PDA_2019_Eligibility_Designation_Summary_Table'

join_args = {'in_layer_or_view': in_layer,
'in_field': 'Join_ID',
'join_table': join_table,
'join_field': 'Summary_ID',
'join_type': 'KEEP_ALL'
}

arcpy.AddJoin_management(**join_args)

# Copy joined table to file geodatabase
join_output_location = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\Growth_Framework_Analysis_Areas.gdb'
join_output_table = r'Draft_Regional_PDA_Eligibility_Summary_2019'
elg_analysis_field_mapping = arcpy.FieldMappings()
elg_analysis_final_fields = ['Join_Key','County','Jurisdiction','PDA_Name', 'PDA_Changes_2019','Designation','Acres_Intersect','Percent_Intersect']

elg_analysis_field_mapping.addTable(in_layer)

issolate_fields(elg_analysis_final_fields, elg_analysis_field_mapping)

#arcpy.TableToTable_conversion(pda_elig_join, join_output_location, join_output_table, None, elg_analysis_field_mapping)

fc_to_fc_args = {'in_features': in_layer,
'out_path':join_output_location,
'out_name':join_output_table,
'where_clause': None,
'field_mapping':elg_analysis_field_mapping
}

arcpy.FeatureClassToFeatureClass_conversion(**fc_to_fc_args)

# Remove Join
arcpy.RemoveJoin_management(in_layer, join_table)

#Create pivot table so designation percent intersect become columns
in_table = 'Draft_Regional_PDA_Eligibility_Summary_2019'
fields = ['Join_ID']
pivot_field = 'Designation'
value_field = 'Percent_Intersect'
out_table = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\Growth_Framework_Analysis_Areas.gdb\Draft_Regional_PDA_Eligibility_Pivot_2019'

pivot_field_args = {'in_table': in_table,
'fields': fields,
'pivot_field': pivot_field,
'value_field': value_field,
'out_table': out_table}

arcpy.PivotTable_management(**pivot_field_args)

# Add field for eligibility flag
add_field_args = {'in_table': out_table,
'field_name': 'Designation',
'field_type': 'TEXT',
'field_precision': None,
'field_length': None,
'field_length': 50,
'field_alias': 'Designation',
'field_is_nullable': 'NULLABLE',
'field_is_required': 'NON_REQUIRED',
'field_domain': None}

arcpy.management.AddField(**add_field_args)

#Rename Join_ID field to PDA_ID
names_dict = {'Join_ID':'PDA_ID'}
clear_alias = 'TRUE'

rename_fields(out_table,names_dict,clear_alias)

# Calculate eligibility field to determine if PDAs meet criteria of 50% or more within eligibility area 
expression = 'designation_criteria(!Connected_Community_Outside_High_Resource_Area!,!Connected_Community_Within_High_Resource_Area!,!Transit_Rich_Outside_High_Resource_Area!,!Transit_Rich_Within_High_Resource_Area!)'
code_block = """ 
def designation_criteria(conncomm_nonhra, conncomm_hra, trans_rich_nonhra, trans_rich_hra):
    if int(0 if conncomm_nonhra is None else conncomm_nonhra) >= 50:
        return 'Connected Community Outside HRA'
    if int(0 if conncomm_hra is None else conncomm_hra) >= 50:
        return 'Connected Community Within HRA'
    if int(0 if trans_rich_nonhra is None else trans_rich_nonhra) >= 50:
        return 'Transit-Rich'
    if int(0 if trans_rich_hra is None else trans_rich_hra) >= 50:
        return 'Transit-Rich'
    if int(0 if trans_rich_nonhra is None else trans_rich_nonhra) + int(0 if trans_rich_hra is None else trans_rich_hra) >= 50:
        return 'Transit-Rich'
    if int(0 if conncomm_hra is None else conncomm_hra) + int(0 if trans_rich_hra is None else trans_rich_hra) >= 50:
        return 'Connected Community Within HRA'
    if int(0 if conncomm_nonhra is None else conncomm_nonhra) + int(0 if trans_rich_nonhra is None else trans_rich_nonhra) >= 50:
        return 'Connected Community Outside HRA'"""

arcpy.management.CalculateField(out_table, "Designation", expression, "PYTHON3", code_block)

# Join to PDA summary feature class created as result of Sumarize Within step
in_layer = 'Draft_Regional_PDA_2019_Eligibility'
join_table = 'Draft_Regional_PDA_Eligibility_Pivot_2019'

join_args = {'in_layer_or_view': in_layer,
'in_field': 'Join_ID',
'join_table': join_table,
'join_field': 'PDA_ID',
'join_type': 'KEEP_ALL'
}

arcpy.AddJoin_management(**join_args)

# Copy joined table to file geodatabase
join_output_location = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\Growth_Framework_Analysis_Areas.gdb'
join_output_table = r'Draft_Regional_PDA_Designation_2019'
designation_field_mapping = arcpy.FieldMappings()
designation_final_fields = ['Join_Key','County','Jurisdiction','PDA_Name', 'PDA_Changes_2019','Designation','Connected_Community_Outside_High_Resource_Area','Connected_Community_Within_High_Resource_Area','Transit_Rich_Within_High_Resource_Area','Transit_Rich_Outside_High_Resource_Area']

designation_field_mapping.addTable(in_layer)

issolate_fields(designation_final_fields, designation_field_mapping)

#arcpy.TableToTable_conversion(pda_elig_join, join_output_location, join_output_table, None, elg_analysis_field_mapping)

fc_to_fc_args = {'in_features': in_layer,
'out_path':join_output_location,
'out_name':join_output_table,
'where_clause': None,
'field_mapping':designation_field_mapping
}

arcpy.FeatureClassToFeatureClass_conversion(**fc_to_fc_args)

# Remove Join
arcpy.RemoveJoin_management(in_layer, join_table)

# Add join to CTA Transit Improvement Table 
join_table = 'PDA_Calculated_Designations'

join_args = {'in_layer_or_view': join_output_table,
'in_field': 'Join_Key',
'join_table': join_table,
'join_field': 'PDA_ID',
'join_type': 'KEEP_ALL'
}

arcpy.AddJoin_management(**join_args)

# Calculate Designation field based on whether or not the PDA has a CTA Transit Improvement
expression = 'transit_designation(!Draft_Regional_PDA_Designation_2019.Designation!,!PDA_Calculated_Designations.Designation!,!PDA_Calculated_Designations.CTA_Transit_Improvement!)'
code_block = """
def transit_designation(designation, improv_designation, flag_field):
    if flag_field == 'Y':
        return improv_designation
    else:
        return designation"""

arcpy.management.CalculateField(join_output_table, "Designation", expression, "PYTHON3", code_block)

# Remove Join
arcpy.RemoveJoin_management(join_output_table, join_table)

# Write report to csv
output_folder = r'C:\Users\mtcgis\Box\GIS (shapefiles)\PDA_Analysis'
output_csv = r'Draft_Regional_PDA_2019_Designation_11_18_19.csv'

arcpy.TableToTable_conversion(join_output_table, output_folder, output_csv)









