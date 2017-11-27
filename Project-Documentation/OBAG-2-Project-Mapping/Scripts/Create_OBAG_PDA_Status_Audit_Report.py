# This script should be run in the ArcGIS Pro Python window 

# ********** This script is not working *************
# Features not converting to NumPyArray for some reason  

import pandas as pd 

# Variables 

OBAGpoints = r"\\Mac\Home\Documents\Programming and Allocations\OBAG\OBAG_2_Mapping\OBAG_2_Mapping.gdb\RPD_OBAG_2_Project_Points_11_07_2017_multi"

OBAGLines = r"\\Mac\Home\Documents\Programming and Allocations\OBAG\OBAG_2_Mapping\OBAG_2_Mapping.gdb\RPD_OBAG_2_Project_Lines_11_07_2017_multi"

field_list = ('App_Proj_ID','MAP_Label','MAP_Mode','County','MAP_project_name','PDA_status','PDA_status_audit') 

# Create function which returns pandas DF

def feature_class_to_pandas_df(feature_class,field_list):
	return pd.DataFrame(arcpy.da.FeatureClassToNumPyArray(feature_class,field_list,skip_nulls=False))

# Create report of points and lines and their PDA audit status

OBAGpointsDF = feature_class_to_pandas_df(OBAGpoints, field_list) 
OBAGLinesDF = feature_class_to_pandas_df(OBAGLines, field_list)


OBAGLines = r"RPD_OBAG_2_Project_Lines_11_07_2017_multi"
field_list = ('App_Proj_ID','MAP_Label','MAP_Mode','County','MAP_project_name','PDA_status','PDA_status_audit') 

OBAGLinesNP = arcpy.da.FeatureClassToNumPyArray(OBAGLines,field_list,skip_nulls=False)