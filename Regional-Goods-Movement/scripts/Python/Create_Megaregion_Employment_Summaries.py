# This script should be run within the ArcGIS Pro Python Window 
#Add GMS_2016_North_CA_Megaregion_Businesses to map before processing

import arcpy
import pandas as pd 

#Set script variables  

norCalMegaRegBusinesses = r"\\Mac\Home\Documents\Planning\Regional Goods Movement\Mega_Region_Analysis\NC_Megaregion_Goods_Movement_Study.gdb\GMS_2016_North_CA_Megaregion_Businesses"

#Create function which returns pandas DF
def feature_class_to_pandas_df(feature_class,field_list):
	return pd.DataFrame(arcpy.da.FeatureClassToNumPyArray(feature_class,field_list,skip_nulls=False))

#Create pandas df from Northern California 2016 Feature Class
norCalMegaRegBusinessesDF = feature_class_to_pandas_df(norCalMegaRegBusinesses, ('EMPNUM','Goods_Mvmt_Class','Supply_Chain_Class')).rename(columns = {'Goods_Mvmt_Class':'Goods Movement Class','Supply_Chain_Class':'Supply Chain Class','EMPNUM':'Total Employment'})

#Group DF by Goods Movement Class and sum employment 
megaRegionEmpTotByGMClass2016 = norCalMegaRegBusinessesDF.groupby(['Goods Movement Class']).agg({'Total Employment':'sum'})

#Add Percentage of Total Employment Column and calculate percentage of total employment
megaRegionEmpTotByGMClass2016['Percentage of Total'] = megaRegionEmpTotByGMClass2016.apply(lambda x: 100 * x / float(x.sum()))

#Export to CSV 
megaRegionEmpTotByGMClass2016.to_csv(r"\\Mac\Home\Documents\Github_Documentation\Regional-Goods-Movement\Northern-California-Megaregion-Employment-Density-Maps\data\2016_Megaregion_Emp_Tot_By_GM_Class.csv")

#Group DF by Supply Chain Class and sum employment
megaRegionEmpTotBySCClass2016 = norCalMegaRegBusinessesDF.groupby(['Supply Chain Class']).agg({'Total Employment':'sum'}) 

#Add Percentage of Total Employment Column and calculate percentage of total employment 
megaRegionEmpTotBySCClass2016['Percentage of Total'] = megaRegionEmpTotBySCClass2016.apply(lambda x: 100 * x / float(x.sum()))

#Export to CSV
megaRegionEmpTotBySCClass2016.to_csv(r"\\Mac\Home\Documents\Github_Documentation\Regional-Goods-Movement\Northern-California-Megaregion-Employment-Density-Maps\data\2016_Megaregion_Emp_Tot_By_SC_Class.csv")

