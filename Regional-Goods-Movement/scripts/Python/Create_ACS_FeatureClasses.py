#This script should be run in the ArcGIS Pro Python Window

import pandas as pd
import numpy as np 
import requests

#Variables 

api_key = '13f1e5cda2e31e0a8c7657aac968aa5327b055d3'
state = '06'
MR_Counties = '001,013,041,055,075,081,085,095,097,113,099,077,047,067,061,017,101,115,053,069,087' 
ACS_2015_5_YR_Est_Base_URL = 'http://api.census.gov/data/2015/acs5?key={0}&NAME&for=tract:*&in=state:{1}+county:{2}&get={3}'

#Get ACS 2015 5 Yr Est- Educational Attainment by Employment Status for the population 25 to 64 years

ACS_EA_BY_Emp_Status = 'B23006_001E,B23006_004E,B23006_006E,B23006_011E,B23006_013E,B23006_018E,B23006_020E,B23006_025E,B23006_027E'
ACS_EA_BY_Emp_Status_URL = ACS_2015_5_YR_Est_Base_URL.format(api_key,state,MR_Counties,ACS_EA_BY_Emp_Status)

#Get ACS 2015 5 Yr Est- Means of Transportation to Work by Workers Earnnings in the Past 12 Months 

ACS_Worker_Earnings = 'B08119_001E,B08119_002E,B08119_003E,B08119_004E,B08119_005E,B08119_006E,B08119_007E,B08119_008E,B08119_009E'
ACS_Worker_Earnings_URL = ACS_2015_5_YR_Est_Base_URL.format(api_key,state,MR_Counties,ACS_Worker_Earnings)

#Get ACS 2015 5 Yr Est- Employment Status for the Population 16 Years and Over 

ACS_Employment_Status = 'B23025_001E,B23025_002E,B23025_003E,B23025_004E,B23025_005E,B23025_006E,B23025_007E'
ACS_Employment_Status_URL = ACS_2015_5_YR_Est_Base_URL.format(api_key,state,MR_Counties,ACS_Employment_Status)

#ACS 2015 API Request to JSON 

ACS_2015_EA_BY_EMP_JSON = requests.get(ACS_EA_BY_Emp_Status_URL).json()
ACS_Worker_Earnings_Json = requests.get(ACS_Worker_Earnings_URL).json()
ACS_Employment_Status_JSON = requests.get(ACS_Employment_Status_URL).json()

#Convert to dataframe

df_ACS_EA_EMP = pd.DataFrame(data=(ACS_2015_EA_BY_EMP_JSON[1:-1]),columns=(ACS_2015_EA_BY_EMP_JSON[0]))
df_ACS_Worker_Earn = pd.DataFrame(data=(ACS_Worker_Earnings_Json[1:-1]),columns=(ACS_Worker_Earnings_Json[0]))
df_ACS_Employment_Status = pd.DataFrame(data=(ACS_Employment_Status_JSON[1:-1]),columns=(ACS_Employment_Status_JSON[0]))

#Rename Columns

df_ACS_EA_EMP.columns = ['Total_Pop_25_64','No_HS_Armed_Forces','No_HS_Employed','HS_Armed_Forces','HS_Employed','Some_College_Armed_Forces','Some_College_Employed','Bachelors_or_Higher_Armed_Forces','Bachelors_or_Higher_Employed','Name','State','County','Tract']

df_ACS_Worker_Earn.columns = ['Total_Pop_16_Over_Earn','Income_9999_or_Below','Income_10000_to_14999','Income_15000_to_24999','Income_25000_to_34999','Income_35000_to_49999','Income_50000_to_64999','Income_65000_to_74999','Income_75000_or_More','Name','State','County','Tract']

df_ACS_Employment_Status.columns = ['Total_Pop_16_Over','Total_In_LF','Total_In_Civilian_LF','Civilian_LF_Employed','Civilian_LF_Unemployed','Armed_Forces','Not_In_LF','Name','State','County','Tract']

#Create 2 new columns: Total workers without a college degree; Total workers - converting columns to numeric types

df_ACS_EA_EMP[['Total_Pop_25_64','No_HS_Armed_Forces','No_HS_Employed','HS_Armed_Forces','HS_Employed','Some_College_Armed_Forces','Some_College_Employed','Bachelors_or_Higher_Armed_Forces','Bachelors_or_Higher_Employed']] = df_ACS_EA_EMP[['Total_Pop_25_64','No_HS_Armed_Forces','No_HS_Employed','HS_Armed_Forces','HS_Employed','Some_College_Armed_Forces','Some_College_Employed','Bachelors_or_Higher_Armed_Forces','Bachelors_or_Higher_Employed']].apply(pd.to_numeric)

df_ACS_EA_EMP['Total_Workers_Without_Degree'] = df_ACS_EA_EMP['No_HS_Armed_Forces'] + df_ACS_EA_EMP['No_HS_Employed'] + df_ACS_EA_EMP['HS_Armed_Forces'] + df_ACS_EA_EMP['HS_Employed'] + df_ACS_EA_EMP['Some_College_Armed_Forces'] + df_ACS_EA_EMP['Some_College_Employed']

df_ACS_EA_EMP['Total_Workers_25_64'] = df_ACS_EA_EMP['No_HS_Armed_Forces'] + df_ACS_EA_EMP['No_HS_Employed'] + df_ACS_EA_EMP['HS_Armed_Forces'] + df_ACS_EA_EMP['HS_Employed'] + df_ACS_EA_EMP['Some_College_Armed_Forces'] + df_ACS_EA_EMP['Some_College_Employed'] + df_ACS_EA_EMP['Bachelors_or_Higher_Armed_Forces'] + df_ACS_EA_EMP['Bachelors_or_Higher_Employed']

#Create new column of total low income workers (workers below CA Median 0f $31,296)

df_ACS_Worker_Earn[['Total_Pop_16_Over_Earn','Income_9999_or_Below','Income_10000_to_14999','Income_15000_to_24999','Income_25000_to_34999','Income_35000_to_49999','Income_50000_to_64999','Income_65000_to_74999','Income_75000_or_More']] = df_ACS_Worker_Earn[['Total_Pop_16_Over_Earn','Income_9999_or_Below','Income_10000_to_14999','Income_15000_to_24999','Income_25000_to_34999','Income_35000_to_49999','Income_50000_to_64999','Income_65000_to_74999','Income_75000_or_More']].apply(pd.to_numeric) 

df_ACS_Worker_Earn['Total_Low_Income_Workers'] = df_ACS_Worker_Earn['Income_9999_or_Below'] + df_ACS_Worker_Earn['Income_10000_to_14999'] + df_ACS_Worker_Earn['Income_15000_to_24999'] + df_ACS_Worker_Earn['Income_25000_to_34999']

#Convert columns to numeric type (no creation of new column)

df_ACS_Employment_Status[['Total_Pop_16_Over','Total_In_LF','Total_In_Civilian_LF','Civilian_LF_Employed','Civilian_LF_Unemployed','Armed_Forces','Not_In_LF']] = df_ACS_Employment_Status[['Total_Pop_16_Over','Total_In_LF','Total_In_Civilian_LF','Civilian_LF_Employed','Civilian_LF_Unemployed','Armed_Forces','Not_In_LF']].apply(pd.to_numeric)

#Create GEOID field and cast as string for each df

df_ACS_EA_EMP['GEOID'] = df_ACS_EA_EMP['State'] + df_ACS_EA_EMP['County'] + df_ACS_EA_EMP['Tract']
df_ACS_Worker_Earn['GEOID'] = df_ACS_Worker_Earn['State'] + df_ACS_Worker_Earn['County'] + df_ACS_Worker_Earn['Tract']
df_ACS_Employment_Status['GEOID'] = df_ACS_Employment_Status['State'] + df_ACS_Employment_Status['County'] + df_ACS_Employment_Status['Tract'] 

#Drop duplicate columns 

df_ACS_EA_EMP = df_ACS_EA_EMP.drop(['Name','State','County','Tract'], axis=1)
df_ACS_Worker_Earn = df_ACS_Worker_Earn.drop(['Name','State','County','Tract'], axis=1)
df_ACS_Employment_Status = df_ACS_Employment_Status.drop(['Name','State','County','Tract'], axis=1)

#Join all dataframes

df_ACS_2015_Demographics = pd.merge(pd.merge(df_ACS_EA_EMP, df_ACS_Worker_Earn, on=['GEOID'], how='inner'),df_ACS_Employment_Status, on=['GEOID'], how='inner')

#Data frame to ArcGIS Table 

x = np.array(np.rec.fromrecords(df_ACS_2015_Demographics.values))
datatypes = df_ACS_2015_Demographics.dtypes.index.tolist()
x.dtype.names = tuple(datatypes)
arcpy.da.NumPyArrayToTable(x,r'\\Mac\Home\Documents\Planning\Regional Goods Movement\Mega_Region_Analysis\NC_Megaregion_Goods_Movement_Study.gdb\ACS_2015_Demographics_Table')

#Set local variables

inFeatures = r'\\Mac\Home\Documents\GIS Data\TIGER Geography\tl_2015_06_tract\tl_2015_06_tract.shp'
layerName = 'TL_2015_06_Tract'
clipFeature = r'\\Mac\Home\Documents\Planning\Regional Goods Movement\Mega_Region_Analysis\NC_Megaregion_Goods_Movement_Study.gdb\NC_Mega_Region_FMMP_Urban_2014'
clipLayerName = 'FMMP_Urban_2014'
clipOutput = r'\\Mac\Home\Documents\Planning\Regional Goods Movement\Mega_Region_Analysis\Mega_Region_Analysis.gdb\clipOutput'
joinField = "GEOID"
joinTable = r'\\Mac\Home\Documents\Planning\Regional Goods Movement\Mega_Region_Analysis\NC_Megaregion_Goods_Movement_Study.gdb\ACS_2015_Demographics_Table'
outFeatures = r'\\Mac\Home\Documents\Planning\Regional Goods Movement\Mega_Region_Analysis\NC_Megaregion_Goods_Movement_Study.gdb\Goods_Mvmt_Features\NC_Megaregion_ACS_2015_Demographics'

#Create a feature layer from the census tracts & water

arcpy.MakeFeatureLayer_management(inFeatures, layerName)

arcpy.MakeFeatureLayer_management(clipFeature, clipLayerName)

#Join the feature layer to a table 

arcpy.AddJoin_management(layerName, joinField, joinTable, joinField, "KEEP_COMMON")

#Erase water areas

arcpy.Clip_analysis(layerName, clipLayerName, clipOutput)

#Copy feature layer into project gdb as feature class

arcpy.management.CopyFeatures(clipOutput, outFeatures) 



