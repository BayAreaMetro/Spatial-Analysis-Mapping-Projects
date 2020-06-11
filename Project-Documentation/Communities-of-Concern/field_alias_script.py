#This script reassigns the alias field for the communities of concern feature class

#Import geoprocessing
import arcpy

#Set workspace
arcpy.env.workspace = r'Z:\Documents\DataManagement\COC_ACS2018.gdb'

#Create field map dict
field_dict = {'geoid': 'Geographic ID',
 'state': 'State',
 'county_fip': 'County FIPS',
 'tract': 'Tract',
 'tot_pop': 'Total Population',
 'tot_pop_po': 'Total Low Income Population',
 'tot_pop_ci': 'Total Civilian Noninstitutionalized Population',
 'tot_hh': 'Total Households',
 'tot_fam': 'Total Families',
 'tot_pop_ov': 'Total Population Over 5',
 'pop_minori': 'Population Minority',
 'pop_over75': 'Population Over 75',
 'pop_spfam': 'Population Single Parent Family',
 'pop_lep': 'Population Limited English Proficiency',
 'pop_below2': 'Population Low Income',
 'pop_disabi': 'Population Disabled',
 'pop_hus_re': 'Population Rent Burdened',
 'pop_zvhhs': 'Population Zero Vehicle Household',
 'pct_over75': 'Percent Over 75',
 'pct_minori': 'Percent Minority',
 'pct_spfam': 'Percent Single Parent Family',
 'pct_lep': 'Percent Limited English Proficiency',
 'pct_below2': 'Percent Low Income',
 'pct_disab': 'Percent Disabled',
 'pct_zvhhs': 'Percent Zero Vehicle Household',
 'pct_hus_re': 'Percent Rent Burdened',
 'over75_1_2': 'Over 75 Regional Mean Plus Half SD',
 'minori_1_2': 'Minority Mean Plus Half SD',
 'spfam_1_2': 'Single Parent Family Mean Plus Half SD',
 'disab_1_2': 'Disabled Mean Plus Half SD',
 'lep_1_2': 'Limited English Proficiency Mean Plus Half SD',
 'below2_1_2': 'Low Income Mean Plus Half SD',
 'zvhh_1_2': 'Zero Vehicle Household Mean Plus Half SD',
 'hus_re_1_2': 'Rent Burdened Mean Plus Half SD',
 'coc_2035': 'Community of Concern PBA 2035',
 'coc_2040': 'Community of Concern PBA 2040',
 'coc_2050': 'Community of Concern PBA 2050',
 'c2040_2050': 'Loss or Gain of COCs PBA 2040 2050',
 'coc_class': 'Community of Concern Class'}

#Loop through dict and update alias

fc = r'Z:\Documents\DataManagement\COC_ACS2018.gdb\COCs_ACS2014_2018'

[arcpy.AlterField_management(fc, f, new_field_alias=field_dict[f]) for f in field_dict]
