#This script is meant to be run in an ArcGIS Pro Python Window 

#Variables 

proj_fgdb = r'\\Mac\Home\Documents\Planning\North Bay Wildfire Analysis\North Bay Wildfire Analysis.gdb\{0}'

#Make Feature Layers 

input_fc = r'Final\Calfire_Active_Fire_Perimeters_2017_disso'

input_ly = arcpy.MakeFeatureLayer_management(proj_fgdb.format(input_fc),"Calfire_Active_Fire_Perimeters_2017_disso")

#Calfire Active Fire Perimeters Demographics 

output_fc = r'Final\Calfire_Active_Fire_Perimeters_2017_Demo_test' 
county = r'United States (US)'

arcpy.analysis.EnrichLayer(input_ly, proj_fgdb.format(output_fc), county, "Race & Hispanic Origin (raceandhispanicorigin)", "'2017 Total Population (Age_by_Sex_by_Race_Profile_rep.TOTPOP_CY)';'2017 Total Households (Age_by_Sex_by_Race_Profile_rep.TOTHH_CY)';'2017 Median Age (Age_by_Sex_by_Race_Profile_rep.MEDAGE_CY)';'2017 Median Household Income (householdincome.MEDHINC_CY)';'2017 Per Capita Income (householdincome.PCI_CY)';'2017 Average Household Income (householdincome.AVGHINC_CY)';'2017 Owner Occupied HUs (OwnerRenter.OWNER_CY)';'2017 Renter Occupied HUs (OwnerRenter.RENTER_CY)';'ACS Housing: 1 Attached Unit in Structure (unitsinstructure.ACSUNT1ATT)';'ACS Housing: 1 Detached Unit in Structure (unitsinstructure.ACSUNT1DET)';'ACS Housing: 10 to 19 Units in Structure (unitsinstructure.ACSUNT10)';'ACS Housing: 2 Units in Structure (unitsinstructure.ACSUNT2)';'ACS Housing: 20 to 49 Units in Structure (unitsinstructure.ACSUNT20)';'ACS Housing: 3 or 4 Units in Structure (unitsinstructure.ACSUNT3)';'ACS Housing: 5 to 9 Units in Structure (unitsinstructure.ACSUNT5)';'ACS Housing: 50+ Units in Structure (unitsinstructure.ACSUNT50UP)';'ACS Housing: Mobile Homes (unitsinstructure.ACSUNTMOB)';'ACS Total Housing Units (unitsinstructure.ACSTOTHU)';'2017 Population by Race Base (raceandhispanicorigin.RACEBASECY)';'2017 Non-Hispanic American Indian Pop (raceandhispanicorigin.NHSPAI_CY)';'2017 Non-Hispanic Asian Pop (raceandhispanicorigin.NHSPASN_CY)';'2017 Non-Hispanic Black Pop (raceandhispanicorigin.NHSPBLK_CY)';'2017 Non-Hispanic Multiple Race Pop (raceandhispanicorigin.NHSPMLT_CY)';'2017 Non-Hispanic Pacific Islander Pop (raceandhispanicorigin.NHSPPI_CY)';'2017 Non-Hispanic White Pop (raceandhispanicorigin.NHSPWHT_CY)';'2017 Non-Hispanic Population (raceandhispanicorigin.NONHISP_CY)';'2017 Hispanic Population (raceandhispanicorigin.HISPPOP_CY)'", "STRAIGHT_LINE", None, "MILES")


