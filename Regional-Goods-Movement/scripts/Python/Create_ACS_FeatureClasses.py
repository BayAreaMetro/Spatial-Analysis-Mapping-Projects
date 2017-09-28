import pandas as pd
import requests
import xlsxwriter

#Variables 
api_key = '13f1e5cda2e31e0a8c7657aac968aa5327b055d3'
state = '06'
MR_Counties = '001,013,041,055,075,081,085,095,097,113,099,077,047,067,061,017,101,115,053,069,087' 
ACS_2015_5_YR_Est_Base_URL = 'http://api.census.gov/data/2015/acs5?key={0}&NAME&for=tract:*&in=state:{1}+county:{2}&get={3}'

#Get ACS 2015 5 Yr Est- Educational Attainment by Employment Status for the population 25 to 64 years

ACS_EA_BY_Emp_Status = 'B23006_001E,B23006_004E,B23006_006E,B23006_011E,B23006_013E,B23006_018E,B23006_020E'
ACS_EA_BY_Emp_Status_URL = ACS_2015_5_YR_Est_Base_URL.format(api_key,state,MR_Counties,ACS_EA_BY_Emp_Status)

#Get ACS 2015 5 Yr Est- Means of Transportation to Work by Workers' Earnnings in the Past 12 Months 
ACS_Worker_Earnings = 'B08119_001,B08119_002,B08119_003,B08119_004,B08119_005,B08119_006,B08119_007,B08119_008,B08119_009'
ACS_Worker_Earnings_URL = ACS_2015_5_YR_Est_Base_URL.format(api_key,state,MR_Counties,ACS_Worker_Earnings)

#ACS 2015 API Request to JSON 

ACS_2015_EA_BY_EMP_JSON = requests.get(ACS_EA_BY_Emp_Status_URL).json()
ACS_Worker_Earnings_Json = requests.get(ACS_Worker_Earnings_URL).json()

#Convert to dataframe

df_ACS_EA_EMP = pd.DataFrame(data=(ACS_2015_EA_BY_EMP_JSON[1:-1]),columns=(ACS_2015_EA_BY_EMP_JSON[0]))
df_ACS_Worker_Earn = pd.DataFrame(data=(ACS_Worker_Earnings_Json[1:-1]),columns=(ACS_Worker_Earnings_Json[0]))

#Rename Columns
df_ACS_EA_EMP.columns = ['Total_Pop_25_64','No_HS_Armed_Forces','No_HS_Employed','HS_Armed_Forces','HS_Employed','Some_College_Armed_Forces','Some_College_Employed','Name','State','County','Tract']
df_ACS_Worker_Earn.columns = ['Total_Pop_16_Over','Male_Earn','Female_Earn','Name','State','County','Tract']

#Create new column of total workers without a college degree - converting columns to numeric types

df_ACS_EA_EMP = df_ACS_EA_EMP[['Total_Pop_25_64','No_HS_Armed_Forces','No_HS_Employed','HS_Armed_Forces','HS_Employed','Some_College_Armed_Forces','Some_College_Employed']].apply(pd.to_numeric)

df_ACS_EA_EMP['Total_Workers_Without_Degree'] = df_ACS_EA_EMP['No_HS_Armed_Forces'] + df_ACS_EA_EMP['No_HS_Employed'] + df_ACS_EA_EMP['HS_Armed_Forces'] + df_ACS_EA_EMP['HS_Employed'] + df_ACS_EA_EMP['Some_College_Armed_Forces'] + df_ACS_EA_EMP['Some_College_Employed']

#Create new column of total low income workers (workers below CA Median) 

#Join Educational Attainment & Median Earnings DFs

df_Net_Change_2000_2016 = pd.merge(df_Census, df_Est, on=['State','County'], how='left')