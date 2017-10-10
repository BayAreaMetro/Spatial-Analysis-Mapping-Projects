import fiona
import pandas as pd
import geopandas as gpd

#data sourced from http://mtc.maps.arcgis.com/home/item.html?id=53f98257229b49c1a0f53447bff434c8
sd = gpd.read_file('data/2013_unified_ca_subset.shp')
sd.GEOID = sd.GEOID.str.slice(start=1)
sd.GEOID = sd.GEOID.astype('int')

df = pd.read_csv('data/schools_ca.csv')

print(df.columns)

###
#join fields
###

sd_df = sd.merge(df, right_on="leaid",
	left_on="GEOID", 
	how="left", suffixes=("_sd","_df"))

sd_df = sd_df.fillna(-999999)

sd_df_na = sd_df[sd_df["gsmean_pool"]==-999999]

sd_df_na.to_file('schools_data_stanford_geoms_na.shp')

sd_df = sd_df[~(sd_df["gsmean_pool"]==-999999)]

#sd_df.to_file('schools_data_stanford_geoms_no_na.shp')

cnty = gpd.read_file('C:/projects/merge_highways/TomTom_CA.gdb/TomTom_CA.gdb', driver="OpenFileGDB", layer="mn_a8")

county_select = ["CA041", "CA055", "CA095", "CA097", "CA081", "CA001", "CA085", "CA013", "CA075"]

cnty_ba = cnty.loc[cnty.ORDER08.isin(county_select),:]

cnty_ba = cnty_ba.to_crs({'init': 'epsg:26910'})

sd_df.crs = {'init': 'epsg:4326'}

sd_df = sd_df.to_crs({'init': 'epsg:26910'})

ba = cnty_ba.dissolve(by="ORDER01")

ba_boundary = ba.ix[0].geometry

sd_df_ba = sd_df.loc[sd_df.geometry.intersects(ba_boundary),:]

sd_df_ba.to_file('schools_data_stanford_geoms_no_na_ba.shp')

sd_not_in_times = gpd.read_file('data/data_not_in_nyt.shp')

sd_df_ba.loc[sd_df_ba.leaid.isin(sd_not_in_times.GEOID),"leaname"].to_csv("sd_not_in_nyt.csv")

####redfin

rdfn = gpd.read_file('C:/projects/motm_april_17/places_redfin.shp')

sd_not_in_times.crs = {'init': 'epsg:4326'}
sd_not_in_times = sd_not_in_times.to_crs({'init': 'epsg:26910'})

sd_ni_d = sd_not_in_times.dissolve(by="STATEFP")

sd_not_in_nyt_boundary = sd_ni_d.ix[0].geometry

rdfn_slct = rdfn.loc[rdfn.geometry.intersects(sd_not_in_nyt_boundary).value_counts(),:]

rdfn_slct.place_name.to_csv("places_we_can_add.csv")