#This script should be run in the ArcGIS Pro Python Window

import pandas as pd
import requests
import xlsxwriter 

api_key = '13f1e5cda2e31e0a8c7657aac968aa5327b055d3' 
#Total Population Year 2000
c_2000_pop = 'P001001'
#Api url summary file 1
census_2000_url = 'http://api.census.gov/data/2000/sf1?get={0}&for=county:*&key=13f1e5cda2e31e0a8c7657aac968aa5327b055d3'.format(c_2000_pop)

#Total Population Year Year 2016
acs_2016_pop = 'B01003'

#Api url Census Pop Estimates 2016
c_estimates_2016_url = 'http://api.census.gov/data/2016/pep/population?get=POP&for=county:*&key=13f1e5cda2e31e0a8c7657aac968aa5327b055d3'

#2000 Census Request to JSON 
Request_2000_Census = requests.get(census_2000_url)
R_2000_Census_JSON = Request_2000_Census.json()

#2016 Estimates Request to JSON
Request_2016_Est = requests.get(c_estimates_2016_url)
R_2016_Est_JSON = Request_2016_Est.json()

#Convert to dataframe
df_Census = pd.DataFrame(data=(R_2000_Census_JSON[1:-1]),columns=(R_2000_Census_JSON[0]))
df_Est = pd.DataFrame(data=(R_2016_Est_JSON[1:-1]),columns=(R_2016_Est_JSON[0])) 

#Rename Columns
df_Census.columns= ['Pop_2000','State','County']
df_Est.columns= ['Pop_2016','State','County']

#Join 2000 Census Population DF with 2016 Census Population Estimate DF
df_Net_Change_2000_2016 = pd.merge(df_Census, df_Est, on=['State','County'], how='left')

#Concatenate state and county for form geoid column
df_Net_Change_2000_2016 = df_Net_Change_2000_2016.assign(geoid = df_Net_Change_2000_2016['State']+df_Net_Change_2000_2016['County'])

#Convert Pop_2000 and Pop_2016 to numeric types
df_Net_Change_2000_2016[['Pop_2000','Pop_2016']] = df_Net_Change_2000_2016[['Pop_2000','Pop_2016']].apply(pd.to_numeric)

#Create new column with net difference of population between 2000 and 2016
df_Net_Change_2000_2016 = df_Net_Change_2000_2016.assign(Pop_Change = df_Net_Change_2000_2016['Pop_2016'] - df_Net_Change_2000_2016['Pop_2000'])

#Save dataframe to excel 
writer = pd.ExcelWriter(r'\\Mac\Home\Documents\Github_Documentation\motm\2017_08\data\Population_Change_2000_2016_Census.xlsx', engine='xlsxwriter')
df_Net_Change_2000_2016.to_excel(writer, sheet_name='Sheet1',index=False)
writer.save()

#Add excel table to ArcGIS Pro project 
arcpy.ExcelToTable_conversion(r'\\Mac\Home\Documents\Github_Documentation\motm\2017_08\data\Population_Change_2000_2016_Census.xlsx','Sheet1') 

#Set local variables
inFeatures = "tl_2010_us_county"
joinField = "geoid"
joinTable = "Sheet1"
outFeatures = r"\\Mac\Home\Documents\MapOfTheMonth\MapOfTheMonth\MapOfTheMonth.gdb\US_Counties_Pop_Change_2000_2016_V3"

#Join the feature layer to a table 
arcpy.AddJoin_management(inFeatures, joinField, joinTable, joinField, "KEEP_ALL")

#Copy feature layer into project gdb as feature class
arcpy.management.CopyFeatures(inFeatures, outFeatures)





