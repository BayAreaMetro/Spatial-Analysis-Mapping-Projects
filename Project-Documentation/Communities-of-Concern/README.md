## MTC Communities of Concern 

Identify census tracts within the Bay Area that are considered Communities of Concern as defined by [MTC Resolution No. 4217-Equity Framework for Plan Bay Area 2040](https://mtc.legistar.com/LegislationDetail.aspx?ID=2555452&GUID=575A6D3F-B8B8-44CF-9F2D-ABEF8B3C9F06&Options=ID|Text|&Search=%22communities+of+concern%22)

### Project Management 

- [Asana Project](https://app.asana.com/0/229355710745434/526057462891473)
- [Box Directory](https://mtcdrive.box.com/s/nszb0i88eheraaa0303nithjl7ej496y)

## Data Sources

- [U.S. Census - American Community Survey 2012-2016](https://www.census.gov/programs-surveys/acs/)
- [U.S. Census - TIGER/Line Shapefiles 2016](https://www.census.gov/geo/maps-data/data/tiger-line.html)

## Analysis Parameters

The 2018 update of MTC's Communities of Concern follows the Adopted Communities of Concern (COC) Framework for Plan Bay Area 2040, and is based on on 2012-2016 American Community Survey (ACS) 5-year tract level data. The MTC COC Framework is provided below as well as a summary table which provides the 8 COC disadvantage factors, definitions of disadvantage factors, census-tract concentration thresholds, relevant ACS table variables, and ACS variable definitions. 

**MTC Communities of Concern Framework**

- [MTC Resolution No. 4217-Equity Framework for Plan Bay Area 2040](https://mtc.legistar.com/LegislationDetail.aspx?ID=2555452&GUID=575A6D3F-B8B8-44CF-9F2D-ABEF8B3C9F06&Options=ID|Text|&Search=%22communities+of+concern%22)
- [Plan Bay Area 2040-Equity Report](http://2040.planbayarea.org/sites/default/files/2017-07/Equity_Report_PBA%202040%20_7-2017.pdf)

![COC Framework](README_Images/COC_Framework_PBA2040.png)

**Summary of MTC COC Disadvantage Factors & Disadvantage Factor Definitnions**

[ACS Table Variables and MTC COC Disadvantage Factors Lookup](Data/ACS_Table_Variables_COC_Factors.csv)

| Disadvantage Factor                            | Disadvantage Factor Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Concentration Threshold |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| Minority                                       | Minority populations include persons who identify as any of the following groups as defined by the Census Bureau in accordance with guidelines provided by the U.S. Office of Management and Budget: American Indian or Pacific Islander Alone (Non-Hispanic/non-Latino); Asian Alone (non-Hispanic/non-Latino); Black or African-American Alone (non-Hispanic/non-Latino); and Other (Some Other Race, Two or More Races).                                                                                                                                              | 70%                     |
| Low Income (< 200% Federal Poverty Level -FPL) | Person living in a household with incomes less than 200% of the federal poverty level established by the Census Bureau.                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 30%                     |
| Limited English Proficienty                    | Person above the age of 5 years, who do not speak English "very well" as their primary language or had a limited ability to read, speak, write, or understand English "very well"                                                                                                                                                                                                                                                                                                                                                                                        | 20%                     |
| Zero-Vehicle Household                         | Households that do not own a personal vehicle.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 10%                     |
| Seniors 75 Years and Over                      | Self-explanatory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 10%                     |
| People with Disability                         | The U.S. Census Bureau defines disability as: Hearing difficulty- deaf or having serious difficulty hearing (DEAR); Vision difficulty- blind or having serious difficulty remembering, concentrating, or making decisions (DREM); Ambulatory difficulty- having serious difficulty walking or climbing stars (DPHY; Self-care difficulty- having difficulty bathing or dressing (DDRS); Independent living difficulty- because of a physical, mental, or emotional problem, having difficulty doing errands alone such as visiting a doctor's office or shopping (DOUT). | 25%                     |
| Single-Parent Family                           | Families with at least one child.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 20%                     |
| Severely Rent-Burdened Household               | Renters paying > 50% of income in rent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 15%                     |

## Methodology

**Calculate MTC COC Disadvantage Factor Population from ACS Variable Populations**

| Disadvantage Factor                            | Disadvantage Factor Population Based on ACS Variable Population                                                                                            |
|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minority                                       | B00001_001E - B03002_002E                                                                                                                                  |
| Low Income (< 200% Federal Poverty Level -FPL) | C17002_001E - C17002_008E                                                                                                                                  |
| Limited English Proficienty                    | B16005_001E - (B16005_003E + B16005_005E + B16005_010E + B16005_015E + B16005_020E + B16005_025E + B16005_027E +  B16005_032E + B16005_037E + B16005_042E) |
| Zero-Vehicle Household                         | B08201_002E                                                                                                                                                |
| Seniors 75 Years and Over                      | B01001_023E + B01001_024E + B01001_025E + B01001_047E + B01001_048E + B01001_049E                                                                          |
| People with Disability                         | C18108_001E - (C18108_005E + C18108_009E + C18108_013E)                                                                                                    |
| Single-Parent Family                           | (B11004_003E + B11004_010E + B11004_016E) - (B11004_010E - B11004_016E)                                                                                    |
| Severely Rent-Burdened Household               | B25070_001E - B25070_010E                                                                                                                                  |


## Expected Outcomes

- Feature class that contains Census Tracts meeting MTC Communities of Concern criteria 
- Web layer that contains Census Tracts meeting MTC Communities of Concern criteria 
- Print map of MTC Communities of Concern

## Results

