#This script is meant to be run in an ArcGIS Pro Python Window 

#Variables 

proj_fgdb = r'\\Mac\Home\Documents\Planning\North Bay Wildfire Analysis\North Bay Wildfire Analysis.gdb\{0}'

#Calfire Active Fire Perimeters Demographics 

input_ly = "Calfire_Active_Fire_Perimeters_2017_disso"
output_ly = "Calfire_Active_Fire_Perimeters_2017_Demo" 
county = "United States (US)"

arcpy.analysis.EnrichLayer(input_ly, proj_fgdb.format(output_ly), county, "Race and Ethnicity (RaceAndEthnicity)", "'2017 Total Population (Age_by_Sex_by_Race_Profile_rep.TOTPOP_CY)';'2017 Total Households (Age_by_Sex_by_Race_Profile_rep.TOTHH_CY)';'2017 Median Age (Age_by_Sex_by_Race_Profile_rep.MEDAGE_CY)';'2017 Median Household Income (householdincome.MEDHINC_CY)';'2017 Per Capita Income (householdincome.PCI_CY)';'2017 Average Household Income (householdincome.AVGHINC_CY)';'2017 Owner Occupied HUs (OwnerRenter.OWNER_CY)';'2017 Renter Occupied HUs (OwnerRenter.RENTER_CY)';'American Indian/Alaska Native Alone (RaceAndEthnicity.AMERIND_CY_P)';'Asian Alone (RaceAndEthnicity.ASIAN_CY_P)';'Black Alone (RaceAndEthnicity.BLACK_CY_P)';'Hispanic Origin (Any Race) (RaceAndEthnicity.HISPPOP_CY_P)';'Other Race (RaceAndEthnicity.OTHRACE_CY_P)';'Pacific Islander Alone (RaceAndEthnicity.PACIFIC_CY_P)';'Two or More Races (RaceAndEthnicity.RACE2UP_CY_P)';'White Alone (RaceAndEthnicity.WHITE_CY_P)'", "STRAIGHT_LINE", None, "MILES")

#Calfire Active Fire Perimeters Built-Environment 

