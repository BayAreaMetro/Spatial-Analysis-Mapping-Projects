**Draft Status: Draft**

## CASA Equity Analysis

Identify the geographic impacts of the [CASA Compact](https://mtc.ca.gov/sites/default/files/CASA_Compact.pdf) as adopted by the CASA Technical Committee on December 3, modified before appproval by the CASA Steering Committee on December 12, and authorized for Commission Chair signiature by the MTC on December 19, 2018.

### Project Management

- [Asana Project](https://app.asana.com/0/356840529458476/913179078257017/f)
- [Box](https://mtcdrive.box.com/s/32q1ukuaifx0n7fowwowmsm97gohdtf7)

### Contents 

- [Data Sources](#data-sources)
- [Analysis Parameters](#analysis-parameters)
    - 
    
- [Methodology](#methodology)
    - 
- [Expected Outcomes](#expected-outcomes)
    - 
- [Results](#results)

## Data Sources

- [U.S. Census - American Community Survey 2012-2016](https://www.census.gov/programs-surveys/acs/)
- [U.S. Census - TIGER/Line Shapefiles 2016](https://www.census.gov/geo/maps-data/data/tiger-line.html)
- [MTC Communities of Concern (2018)](https://mtc.maps.arcgis.com/home/item.html?id=1501fe1552414d569ca747e0e23628ff)
- [BCDC Communities of Concern]  

## Analysis Parameters

### Sensitive Communities

Sensitive Communities are definined as the intersection of the MTC's Communities of Concern and the BCDC's equivalent. To explore MTC's definition of Communities of Concern, please see the [Communities of Concern project documentation page](https://github.com/BayAreaMetro/Spatial-Analysis-Mapping-Projects/tree/master/Project-Documentation/Communities-of-Concern). To explore BCDC's definition, 

### Parcels Zoned for Housing

The Equity Analysis uses Bay Area Metro's existing regionwide general plan land use data. To explore the database, please see the [Plan Land Use project documentation page](https://github.com/BayAreaMetro/petrale/tree/master/policies/plu). For the equity analysis, single-family parcels are those classified as HS (single family residential), multi-family parcels are those classified as HT (townhomes) or HM (multi family residential), and mixed-use parcels are those classified as MR (mixed use residential focused) or ME (mixed use employment focused).

### Rent Increases, 2011 to 2016

Rent is defined as American Community Survey variable B25064-001E, which refers to median gross rent (dollars) in renter-occupied housing units paying cash rent. Rent increases are measured by the percent change between the 2011 and 2016 ACS.

To explore the methodology, take a look at the [Low Income Tenure Methodology](CASA_acs_vars_lowincomeTenure.Rmd)

The link below provides schema and domains, along with calculations and written descriptions of the calculations which may be helpful for analysis purposes. Below the link is a table for informational purposes. 

### Low Income Renters

The Equity Analysis looks at the spatial distribution of low income renters paying 30 and 50% of their income on rent and low income *minority* renters paying 30 and 50% of their income on rent. Data on low income renters comes from the American Community Survey's Public Use Microdata Sample (PUMS) data. The table below provides the written and variable definitions for the terms in this section. To get variable definitions, please refer to the [2012-2016 ACS 5-year PUMS Data Dictionary](https://www2.census.gov/programs-surveys/acs/tech_docs/pums/data_dict/PUMS_Data_Dictionary_2012-2016.txt?#)

| Term                            | Written definition                                                                                                                                                               | Variable definition                                                                                                                                                   |
|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Low Income                                       | Household income < 200% Federal Poverty Level (FPL)                                                                                                                                                                                                   | POVPIP>=0, <200                                                                                                                                                                                                     |
| Renter | Self-explanatory                                                                                                                                                                                                     | TEN=3                                                                                                                                                                                                       |
| Minority                    | Gnot non-Hispanic/Latino White | All except HISP=1 AND RAC1P=1 |
| Paying Greater than 30% of Income on Housing                         | Self-explanatory                                                                                                                                                                                                                   | GRPIP>=30                                                                                                                                                                                                                    |
| Paying Greater than 50% of Income on Housing                      | Self-explanatory                                                                                                                                             | GRPIP>=30                                                                                                                                            |

### Jurisdiction Housing Policies

Jurisdiction housing policies come from the [Association of Bay Area Governments' Housing Policy Database](http://housing.abag.ca.gov/policysearch). Please note that the data in the Equity Analysis has caveats due to discrepancies between the user-friendly interface and the underlying dataset in addition to the dataset becoming partially out of date:

1. Mountain View CDP is listed as having both rent stabilization and just cause policies, but CDPs have no legal authority to enact such policies. The City of Mountain View has both, but the interface says the City of Mountain View has neither. The dataset correctly states the city has both.
2. Richmond has both rent stabilization and just cause policies, but the interface says it has neither. The database correctly states the city has both.
3. The interface says Sebastopol has rent stabilization, but an [article](https://www.pressdemocrat.com/news/7081053-181/sebastopol-looks-warily-at-rent) from *The Press Democrat* seems to indicate it was only considering it. Sebastopol did have a [temporary rent freeze](https://www.pressdemocrat.com/news/6251432-181/sebastopol-city-council-passes-temporary), which is recorded by the dataset, but that appears to have since expired.
4. Alameda is listed as having just cause protections in both the dataset and , but that appears to have been [repealed]((https://www.eastbaytimes.com/2017/09/06/no-cause-eviction-provision-pulled-from-alameda-ordinance/).
5. Concord, Alameda, Union City, and Fremont are listed as having rent stabilization programs. [Concord](http://www.ci.concord.ca.us/page.asp?pid=1003), [Alameda](http://www.alamedarentprogram.org/about-rrac/), [Union City](https://www.unioncity.org/306/Rent-Review-Ordinance), and [Fremont](https://www.fremont.gov/RentReview) have rent review programs, which are voluntary non-binding mediation processes that do not guarantee limits on rent increases. When jurisdictions were surveyed in 2017 for the database, the four cities self-reported their policies as rent stabilization. While differences between rent stabilization, rent mediation, and rent arbitration ordinances are noted in the "summary/benefits" tab of the database, they do not preclude them from being on the "who implements" tab. Removing them from the map more than a year after they self-reported, based on a definitional change, would in effect be reteroactively changing the question the jurisdictions responded to.

### Displacement Risk Areas

High-displacement risk areas are defined as American Community Survey 2009-2013 tracts where more than 39% of households are low income (below 200% of the Federal Poverty Level) and are undergoing displacement or advanced gentrification as defined as the UC Berkeley Urban Displacement Project. The table and term definitions below define the two latter terms for informational purposes.

![CASA UDP Definition](readme_images/CASA_UDP_areas.png)

**UDP Term Definitions**

- Vulnerable to gentrification in 1990 or 2000 (at least 3 out of 4 of the following indicators):
    - % low income households > regional median
    - % college educated < regional median
    - % renters > regional median
    - $ nonwhite > regional median
- "Hot Market" in 2000 or 2015
    - Change in median real rent > regional median
    or
    - Change in median value for owner-occupied homes > regional median
- Gentrification from 1990 to 2000 or 2000 to 2015
    - Vulnerable in base year (as defined above)
    - Demographic change between base and end years (at least 2 of 3 occurring):
        - Growth in % college educated > regional median
        - Growth in real median household income (percent change) > regional median
        - Lost low-income households
    - LI migration rate (percent of all migration to tract that was LI) in 2015 < in 2009 (only used for 2000-2015 time frame)
    - "Hot market" (defined above)

## Methodology

### Low Income Renters
The analysis was performed in R and leverages the censusapi library which is documented here: [CensusAPI](https://hrecht.github.io/censusapi/index.html)



## Expected Outcomes

Feature classes and web layers of:
- 

Print maps of:
- 

Most mapswill have an overlay showing Sensitive Community Areas

## Results

[Racial Equity Analysis for the CASA Compact](https://mtc.ca.gov/sites/default/files/Racial_Equity_Analysis_for_the_CASA_Compact.pdf)

## Related Works

[Sensitive Communities Threshold Analysis](https://github.com/BayAreaMetro/Spatial-Analysis-Mapping-Projects/tree/master/Project-Documentation/COC-TPA-Thresholds-App)  
[MTC Communities of Concern](https://github.com/BayAreaMetro/Spatial-Analysis-Mapping-Projects/tree/master/Project-Documentation/Communities-of-Concern)