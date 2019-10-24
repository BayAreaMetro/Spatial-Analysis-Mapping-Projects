import arcpy
import os

#Define the workspace
arcpy.env.workspace = r"\\Mac\Home\Documents\Planning\PDA_Eligibility_Analysis\PDA_Eligibility_Analysis.gdb"

#Allow features and files to be overwritten 
arcpy.env.overwriteOutput = True

# Create function to multiple fields using a dictionary
def rename_fields(fc, namesDict, clearAlias):
	for fieldName in namesDict:
		arcpy.management.AlterField(fc, fieldName, namesDict[fieldName], clear_field_alias = clearAlias)

# Create function to select specific fields to map when using field mapping for a geoprocessing function
def issolate_fields(output_fields, field_mappings):
	for field in field_mappings.fields:
		if field.name not in output_fields:
			field_mappings.removeFieldMap(field_mappings.findFieldMapIndex(field.name))

# Summarize PPAs within PPA Eligible Areas Feature Class
ppa_fc = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\Growth_Framework_Analysis_Areas.gdb\Regional_PPA_2019_repaired'
in_sum_features = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\Growth_Framework_Analysis_Areas.gdb\IL_Possible_Criteria_Suitability_Dissolve'
out_feature_class = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\Growth_Framework_Analysis_Areas.gdb\Draft_Regional_PPA_2019_Eligibility'
group_field = 'total_crit'
out_group_table = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\Growth_Framework_Analysis_Areas.gdb\Draft_Regional_PPA_2019_Eligibility_IL_Criteria'

summarize_within_args = {'in_polygons': ppa_fc,
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

# Rename fields in join table created based on PPA Eligible Areas Designation field

names_dict = {'total_crit':'Total_Criteria','SUM_area_ACRES':'Acres_Intersect','PercentArea':'Percent_Intersect'}
clear_alias = 'TRUE'

rename_fields(out_group_table,names_dict,clear_alias)

# Join to PPA summary feature class created as result of Sumarize Within step
join_args = {'in_layer_or_view': out_feature_class,
'in_field': 'Join_ID',
'join_table': out_group_table,
'join_field': 'Join_ID',
'join_type': 'KEEP_ALL'
}

ppa_elig_join = arcpy.AddJoin_management(**join_args)

# Copy joined table to file geodatabase
join_output_location = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\Growth_Framework_Analysis_Areas.gdb'
join_output_table = r'Draft_Regional_PPA_2019_Eligibility_Analysis'
elg_analysis_field_mapping = arcpy.FieldMappings()
elg_analysis_final_fields = ['County','Jurisdiction','PPA_Name','Total_Criteria','Acres_Intersect','Percent_Intersect']

elg_analysis_field_mapping.addTable(ppa_elig_join)

issolate_fields(elg_analysis_final_fields, elg_analysis_field_mapping)

fc_to_fc_args = {'in_features': ppa_elig_join,
'out_path':join_output_location,
'out_name':join_output_table,
'where_clause': None,
'field_mapping':elg_analysis_field_mapping
}

arcpy.FeatureClassToFeatureClass_conversion(**fc_to_fc_args)

# Summarize PPA intersect areas by PPA name to get total PPA area that intersect UC Berkeley IL Areas

in_table = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\Growth_Framework_Analysis_Areas.gdb\Draft_Regional_PPA_2019_Eligibility_Analysis'
out_table = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\Growth_Framework_Analysis_Areas.gdb\Draft_Regional_PPA_2019_Sum_Acres_Intersect_UCB'
statistics_fields = [['Acres_intersect','SUM']]
case_field = ['PPA_Name']

summary_stats_args = {'in_table': in_table,
'out_table': out_table,
'statistics_fields': statistics_fields,
'case_field': case_field}

arcpy.Statistics_analysis(**summary_stats_args)

# Create weighted average field

add_field_args = {'in_table': in_table,
'field_name': 'Weighted_Avg',
'field_type': 'DOUBLE',
'field_precision': None,
'field_scale': None,
'field_length': None,
'field_alias': 'Weighted_Avg',
'field_is_nullable': 'NULLABLE',
'field_is_required': 'NON_REQUIRED',
'field_domain': None}

arcpy.management.AddField(**add_field_args)

# Join back to PPA Eligibility Analysis Table 

in_layer = r'Draft_Regional_PPA_2019_Eligibility_Analysis'
join_table = r'Draft_Regional_PPA_2019_Sum_Acres_Intersect_UCB'

join_args = {'in_layer_or_view': in_layer,
'in_field': 'PPA_Name',
'join_table': join_table,
'join_field': 'PPA_Name',
'join_type': 'KEEP_ALL'
}

arcpy.AddJoin_management(**join_args)

# Calculate weighted average field

expression = '!Draft_Regional_PPA_2019_Eligibility_Analysis.Total_Criteria! * (!Draft_Regional_PPA_2019_Eligibility_Analysis.Acres_Intersect!/!Draft_Regional_PPA_2019_Sum_Acres_Intersect_UCB.SUM_Acres_Intersect!)'
field_name = 'Weighted_Avg'

calc_field_args = {'in_table': in_layer,
'field': field_name,
'expression': expression,
'expression_type': 'PYTHON3',
'code_block': None}

arcpy.management.CalculateField(**calc_field_args)

# Remove Join

arcpy.RemoveJoin_management(in_layer, join_table)

# Write report to csv
output_folder = r'C:\Users\mtcgis\Box\GIS (shapefiles)\PPA_Analysis'
output_csv = r'Draft_Regional_PPA_2019_Eligibility_Analysis.csv'

arcpy.TableToTable_conversion(in_layer, output_folder, output_csv)









