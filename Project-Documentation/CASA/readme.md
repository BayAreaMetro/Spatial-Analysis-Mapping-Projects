**Draft Status: Draft**

## CASA Equity Analysis

Identify the geographic impacts of the [CASA Compact](https://mtc.ca.gov/sites/default/files/CASA_Compact.pdf) as adopted by the CASA Technical Committee on December 3, modified before appproval by the CASA Steering Committee on December 12, and authorized for Commission Chair signiature by the MTC on December 19, 2018.

### Project Management

- [Asana Project](https://app.asana.com/0/356840529458476/913179078257017/f)
- [Box](https://mtcdrive.box.com/s/32q1ukuaifx0n7fowwowmsm97gohdtf7)

### Contents 

- [Data Sources](#data-sources)
- [Analysis Parameters](#analysis-parameters)
    -[Low Income Tenure](#low-income-tenure)
- [Methodology](#methodology)
    -[Low Income Tenure](#low-income-tenure)
- [Expected Outcomes](#expected-outcomes)
    -[Low Income Tenure](#low-income-tenure)
    -[Sensitive Communities](#sensitive-communities)
- [Results](#results)

## Data Sources

- [U.S. Census - American Community Survey 2012-2016](https://www.census.gov/programs-surveys/acs/)
- [U.S. Census - TIGER/Line Shapefiles 2016](https://www.census.gov/geo/maps-data/data/tiger-line.html)
- [MTC Communities of Concern (2018)](https://mtc.maps.arcgis.com/home/item.html?id=1501fe1552414d569ca747e0e23628ff)
- [BCDC Communities of Concern]  

## Analysis Parameters

###Low Income Tenure###
The table below provides the calculations that need to be performed to get Disadvantage Factor populations and Disadvantage Shares. To translate from variable to written description, please review the [ACS Table Variables Lookup for Low Income Tenure](CASA\Data\Low-Income-Tenure\ACS_Table_Variables_lowincome.csv). ACS Variables are also defined on the American Community Survey (ACS) website. To get variable definitions as well as the layout of tables without the estimates or margins of error filled in, download [2016 ACS Detailed Table Shells](https://www2.census.gov/programs-surveys/acs/summary_file/2016/documentation/user_tools/ACS2016_Table_Shells.xlsx) as an Excel spreadsheet. 

The link below provides the COC schema and domains, along with calculations and written descriptions of the calculations which may be helpful for analysis purposes. Below the link is a table for informational purposes. 

## Methodology

###Low Income Tenure###
The analysis was performed in R and leverages the censusapi library which is documented here: [CensusAPI](https://hrecht.github.io/censusapi/index.html)

To explore the methodology, take a look at the [Low Income Tenure Methodology](CASA_acs_vars_lowincomeTenure.Rmd)

## Expected Outcomes

###Low Income Tenure###

- Feature class that displays low income renters by race and share paying greater than 30% of income on housing
	- Feature class name: ***CASA\Data\Low-Income-Tenure\lowincomeTenure_ACS2016_tbl.csv***
	- [Feature Class Schema](???) 
- Print map of low income tenure

###Sensitive Communities###
- Feature class that contains Census Tracts meeting CASA Sensitive Communities criteria
	- Feature class name: ***???***
	- [Feature Class Schema](???)  
- Print map of CASA Sensitive Communities

## Results

[Racial Equity Analysis for the CASA Compact](https://mtc.ca.gov/sites/default/files/Racial_Equity_Analysis_for_the_CASA_Compact.pdf)

## Related Works

[Sensitive Communities Threshold Analysis](https://github.com/BayAreaMetro/Spatial-Analysis-Mapping-Projects/tree/master/Project-Documentation/COC-TPA-Thresholds-App)  
[MTC Communities of Concern](https://github.com/BayAreaMetro/Spatial-Analysis-Mapping-Projects/tree/master/Project-Documentation/Communities-of-Concern)