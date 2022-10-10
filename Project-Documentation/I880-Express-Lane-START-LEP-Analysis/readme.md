# FastTrak Start Pilot Program Limited English Proficiency Population Analysis 

Using American Community Survey 5-Year Estimates, map top Non-English Languages spoken in
Low-Income Census Tracts in the I-880 corridor. Additionally, provide tabular data including total tract population, and total low-income population. Provide total population of people that speak English 'Less than Very Well' and the share a given population by languages spoken at home for every tract within the I-880 corridor. 


### Table of Contents

- [Data Sources](#data-sources)
- [Analysis Parameters](#analysis-parameters)
- [Methodology](#methodology)
- [Expected Outcomes](#expected-outcomes)
- [Results](#results)
- [Tags](#tags)

## Data Sources
    
**LANGUAGE SPOKEN AT HOME FOR THE POPULATION 5 YEARS AND OVER**
- Survey/Program: American Community Survey
- Product: 2019: ACS 5-Year Estimates Detailed Tables
- Universe: Population 5 years and over
- TableID: C16001

**Ratio of Income to Poverty Level in the Past 12 Months**
- Survey/Program: American Community Survey
- Product: 2019: ACS 5-Year Estimates Detailed Tables
- Universe: Population 5 years and over
- TableID: C17002!

## Analysis Parameters

### Definitions 

Limited English Proficiency: Limited English Proficiency for the purposes of this analysis means any person age 5 years and over that speaks a language other than English at home and also speaks English 'less than very well' as defined by the Census Bureau.

Low Income Population: Person living in a household with incomes less than 200% of the federal poverty level established by the Census Bureau.
    
### Study Area
    
Study Area includes Census Tracts within 7 miles of the I-880 corridor in Alameda and Santa Clara Counties. 
    
### Population Thresholds

Limited English proficiency population should be 5% or more of total population for a given tract. This threshold was set by the MTC Plan for Special Language Services to Limited English Proficient (LEP) Populations.  

## Methodology

Data analysis and wrangling for this project was performed in a [Python Jupyter Notebook here](FastTrak-Start-Pilot-Program.ipynb). 

Households and Race analysis was performed in a [Python Jupyter Notebook here](Households_and_Race_880_Corridor_2020.ipynb)


Maps and visualizations were created in [ArcGIS Pro](https://mtcdrive.box.com/s/jkyly5aic1xbx3ylto3wq2a2ptwxadeo).

## Expected Outcomes

- Map of Top Non-English Language Population Tracts along I-880 Corridor
- Tabular dataset/ spreadsheet summarizing total population, low-income population, Limited English Proficiency Population, and share of Limited English Proficincy Population within I-880 Corridor

## Results

- [Limited English Proficiency Language Spoken at Home Map](https://mtcdrive.box.com/s/y2lel3tk8df7h2hw6dmua2fe533gox07)
- [Low Income Population Map](https://mtcdrive.box.com/s/3od1s6r5uxcrmdqi8ze1h64h87187oka)
- [Low Income Language Over 5 Tabular Data](https://mtcdrive.box.com/s/4wawptrj9262ucd1cphyrgotndglg5bx)
- [Low Income Language Over 5 Tabular Data Definitions](https://mtcdrive.box.com/s/edj8325zfnjly1o3yg7x4zk995k72cyl)
