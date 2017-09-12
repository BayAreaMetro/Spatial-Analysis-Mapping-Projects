# This script should be run within the ArcGIS Pro Python Window 

import arcpy
import pandas as pd 

#Select 2016 California Businesses within Northern Californa Megaregion & Create New Feature Class

caBusinesses = r"GMS_2016_CA_Businesses"
norCalMegaregion = r"Northern_CA_Megaregion_Counties"
norCalMegaRegBusinesses = r"\\Mac\Home\Documents\Planning\Regional Goods Movement\Mega_Region_Analysis\NC_Megaregion_Goods_Movement_Study.gdb\GMS_2016_North_CA_Megaregion_Businesses"

#Create fieldmappings object and add the two above input feature class tables  

fieldmappings = arcpy.FieldMappings()
fieldmappings.addTable(caBusinesses)

keepCountyFields = ["NAME","REGION"]

for field in keepCountyFields:
	counties_fm = arcpy.FieldMap()
	counties_fm.addInputField(norCalMegaregion,field)
	fieldmappings.addFieldMap(counties_fm)

arcpy.SpatialJoin_analysis(caBusinesses,norCalMegaregion,norCalMegaRegBusinesses, "#","KEEP_COMMON", fieldmappings)

#Add two additional fields to Northern California Business Feature Class

fields = ["Goods_Mvmt_Class","Supply_Chain_Class"]

def addFields(fc,array):
	for field in array:
		arcpy.AddField_management(fc, field, "TEXT", field_length=5)

addFields(norCalMegaRegBusinesses,fields)

#Create row updator function which accepts featureclass, where clause, feature class field, and desired field value, iterating over subset of rows and updates 
#given field value within each row

def rowUpdator(fc, clause, field, value):
	cursor = arcpy.UpdateCursor(fc, clause)
	for row in cursor:
		row.setValue(field,value)
		cursor.updateRow(row)

#Wrap rowUpdator function in updateClassField function which iterates over ClassSelectionDictionary, which selects feature class subsets and sets value of field
#as the value within the dictionary

def updateClassField(fc, field, dictionary):
	for clause, fieldValue in dictionary.items():
		rowUpdator(fc, clause, field, fieldValue)

#Create cursor where clause objects which represent Goods Movement Classes

gmCore = r"SUBSTRING(NAICS, 1,3) IN ('481','482','483','484','488','491','492','493','486','423','424','425') OR SUBSTRING(NAICS, 1, 4) = '5621'"
gmDependent = r"SUBSTRING(NAICS, 1,2) IN ('11','21','23','31','32','33','44','45') OR SUBSTRING(NAICS, 1,4) IN ('5622','5629')"
gmSupported = r"SUBSTRING(NAICS, 1,2) IN ('22','51','52','53','54','55','61','62','71','72','81','92','99') OR SUBSTRING(NAICS,1,3) IN ('485','487','561')" 

#Create dictionary of where clause objects as keys, and the classes they represent as values

gmClassSelectionDict = {gmCore:"1",gmDependent:"2",gmSupported:"3"}

#Populate Goods_Mvmt_Class Field:
updateClassField(norCalMegaRegBusinesses, "Goods_Mvmt_Class", gmClassSelectionDict)

#Create cursor where clause objects which represent Supply Chain Classes
scProduction = r"SUBSTRING(NAICS, 1,2) IN ('11','21','23','31','32','33')" 
scTransportation = r"SUBSTRING(NAICS, 1,3) IN ('481','482','483','484','486','488','491','492')"
scDistribution = r"SUBSTRING(NAICS, 1,3) IN ('423','424','425','493')"
scRetail = r"SUBSTRING(NAICS, 1,2) IN ('44','45')"
scWaste = r"SUBSTRING(NAICS, 1,4) IN ('5621','5622','5629')" 
scOther = r"SUBSTRING(NAICS, 1,2) IN ('22','51','52','53','54','55','61','62','71','72','81','92','99') OR SUBSTRING(NAICS,1,3) IN ('485','487','561')" 

scClassSelectionDict = {scProduction:"1",scTransportation:"2",scDistribution:"3",scRetail:"4",scWaste:"5",scOther:"6"} 

#Populate Supply_Chain_Class Field
updateClassField(norCalMegaRegBusinesses, "Supply_Chain_Class", scClassSelectionDict)

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













