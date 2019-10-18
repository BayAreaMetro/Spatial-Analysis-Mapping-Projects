#The purpose of this script is to merge all PDA features received from jurisdictions, as well as previous PDAs into one regional feature. 
#This script should be executed within the analysis window of the ArcGIS Pro project linked in the readme. Filepaths should be updated accordingly.

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

# Add all feature classes in project gdb to list
feature_classes = arcpy.ListFeatureClasses()

# Create FieldMappings object to manage merge output fields
field_mappings = arcpy.FieldMappings()

# Add all fields from all feature classes
add_fields(feature_classes,field_mappings)

# Remove all output fields from the field mappings, except fields of interest
output_fields = ['Jurisdiction','County','PDA_Name', 'PDA_Changes_2019']

issolate_fields(output_fields, field_mappings)

# Use Merge tool to move features into single dataset
pda_fc = r'\\Mac\Home\Documents\Planning\Growth_Framework_Analysis\Growth_Framework_Analysis_Areas.gdb\Regional_PDA_2019'

arcpy.Merge_management(feature_classes, pda_fc, field_mappings, 
                       "NO_SOURCE_INFO")

