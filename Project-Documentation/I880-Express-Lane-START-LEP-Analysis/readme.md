# I880 Express Lanes START Analysis

Using American Community Survey 5-Year Estimates, map top Non-English Languages spoken in Low-Income Census Tracts in the I-880 corridor. Provide total population of people that speak English 'Less than Very Well' and the share a given population by languages spoken at home for every tract within the I-880 corridor. Additionally, provide data on Race and Origin as well as Poverty status by Race and Origin. 


### Table of Contents

- [Data Sources](#data-sources)
- [Analysis Parameters](#analysis-parameters)
- [Methodology](#methodology)

## Data Sources
    
**LANGUAGE SPOKEN AT HOME FOR THE POPULATION 5 YEARS AND OVER**
- Survey/Program: American Community Survey
- Product: 2020: ACS 5-Year Estimates Detailed Tables
- Universe: Population 5 years and over
- TableID: C16001

**POVERTY STATUS IN THE PAST 12 MONTHS**
- Survey/Program: American Community Survey
- Product: 2020: ACS 5-Year Estimates Survey Tables
- Universe: Population for whom poverty status is determined / Population Below Poverty Level
- TableID: S1701

**HISPANIC OR LATINO, AND NOT HISPANIC OR LATINO BY RACE**
- Survey/Program: Decennial Census
- Product: 2020 Decennial Census
- Universe: Total Population
- TableID: P2

## Analysis Parameters

### Definitions 

#### Limited English Proficiency
Limited English Proficiency for the purposes of this analysis means any person age 5 years and over that speaks a language other than English at home and also speaks English 'less than very well' as defined by the Census Bureau.

#### Low-Income Population
Person living in a household with incomes less than the Federal Poverty Level established by the Census Bureau.
    
### Study Area
    
Study Area includes Census Tracts within 7 miles of the I-880 corridor in Alameda and Santa Clara Counties. 
    
### Population Thresholds

Limited English proficiency population should be 5% or more of total population for a given tract. This threshold was set by the MTC Plan for Special Language Services to Limited English Proficient (LEP) Populations.  

## Methodology

### Limited English Proficiency Analysis
The limited English Proficiency Analysis was performed in a [Python Jupyter Notebook here](I880%20Express%20Lanes%20START%20LEP%20Analysis.ipynb). 

**Input:** LANGUAGE SPOKEN AT HOME FOR THE POPULATION 5 YEARS AND OVER

**Output:** 
- [Study area tract data tabular](https://mtcdrive.box.com/s/ijnvn00sosnqojylm0n183kcmyyk48va) 
- [Study area tract data geojson](https://mtcdrive.box.com/s/dirga1v2ipp41vedvlao80sywdx7ts31)
- [Study area summary tabular](https://mtcdrive.box.com/s/9rhg236y8n07ufrpktc6y79uzttym8e6) 

### Population by Race and Origin Analysis
The population by Race and Origin analysis was performed in a [Python Jupyter Notebook here](I880%20Express%20Lanes%20START%20Race%20and%20Origin.ipynb)

**Input:** HISPANIC OR LATINO, AND NOT HISPANIC OR LATINO BY RACE

**Output:**
- [Study area summary tabular](https://mtcdrive.box.com/s/wzkg8blpptj365ulreribl4ryu7zrili)
- [Study area summary chart](https://mtcdrive.box.com/s/bg83irmksg8ueg8lmxbrfenyfflfp846)

### Poverty Status by Race and Origin Analysis
The poverty analysis was performed in a [Python Jupyter Notebook here](I880%20Express%20Lanes%20START%20Race%20and%20Poverty%20Analysis.ipynb)

**Input:** POVERTY STATUS IN THE PAST 12 MONTHS

**Output:**
- [Study area tract data tabular](https://mtcdrive.box.com/s/8avgqzc0xiz19teg8ephrf14kchnaqg4)
- [Study area tract data geojson](https://mtcdrive.box.com/s/waryuvu53vjyp5llm4se9np0ri4xbiow)
- [Study area summary tabular](https://mtcdrive.box.com/s/u3gv3mqjblv3l7tdwnbn3skwno1uituk)

Maps and visualizations were created in [ArcGIS Pro](https://mtcdrive.box.com/s/jkyly5aic1xbx3ylto3wq2a2ptwxadeo).

