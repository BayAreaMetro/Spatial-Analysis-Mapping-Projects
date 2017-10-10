import fiona
import pandas as pd
import geopandas as gpd

sd = gpd.read_file('C:/Users/tbuckl/Documents/ArcGIS/Projects/MyProject/motm_04_2017_schools_and_housing_source_data.gdb',layer='esri_places_geometries_bay_area', driver='OpenFileGDB')
# sd.GEOID = sd.GEOID.str.slice(start=1)
# sd.GEOID = sd.GEOID.astype('int')

iter_csv = pd.read_csv('data/redfin_export1.csv', iterator=True, chunksize=1000)
df = pd.concat([chunk[chunk['State'] == "California"] for chunk in iter_csv])

print(df.columns)

df1 = df[df["Region Type"] == 'place']

sd1 = sd.loc[:,'NAME','geometry']

df1.loc[:,"place_name"] = df1.Region.str[:-4]

df_now = df1[df1['Period End'] == "2/28/2017"]

df_now_all = df_now[df_now['Property Type'] == "All Residential"]

df_sd = sd1.merge(df_now_all, left_on="NAME",
	right_on="place_name", 
	how="left", suffixes=("_sd","_df"))

field_select = ['place_name',
'Median Ppsf',
'Median Ppsf Mom',
'Median Ppsf Yoy',
'geometry']


df_sd1 = df_sd.loc[~df_sd['Median Ppsf'].isnull(),field_select]

field_remap = {'place_name':'place_name',
'Median Ppsf':'Ppsf',
'Median Ppsf Mom':'PpsfMom',
'Median Ppsf Yoy':'PpsfYoy'}

df_sd1.rename(columns=field_remap)

df_sd1.to_file('places_redfin.shp')
