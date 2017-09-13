# Northern California Megaregion Goods Movement Analysis & Mapping 

The Goods Movement program at MTC provides a regional, coordinating framework from which funding and planning priorities are developed. The current planning framework is the San Francisco Goods Movement Plan, adopted in 2016, which prioritizes sustainable, global competitiveness in freight. The primary strategies for realizing this goal are through increasing capacity at the Port of Oakland, increasing access to industrial land region-wide, improving efficiency and emissions of urban deliveries, and reducing adverse impacts of freight movement along the highway and rail corridors.

### Contents 

[Problem Statement](#problem-statement)
[Data Sources](#data-sources)  
[Methodology](#methodology)  
[Expected Outcomes](#expected-outcomes)
[Results](#results) 

## Problem Statement

The purpose of this project is to analyze business, transportation, and demographic data for the 22 County Northern California Megaregion, which will inform the works of planners and decision makers supporting the MTC Goods Movement program. 

[Asana Project](https://app.asana.com/0/353588576094175/353588576094186)  

## Data Sources 
- [California Business Data: Esri;Infogroup 2016](https://mtcdrive.app.box.com/folder/11272654765)
  - *Datasets are licensed and therefore not to be distributed publicly*
- [FMMP Urban 2014](http://www.conservation.ca.gov/dlrp/fmmp)


## Analysis Parameters 

## Methodology 

### Summary

1. Create Northern California Megaregion Businesses FC

    [Create Northern California Megaregion Business FC Script](https://github.com/BayAreaMetro/Spatial-Analysis-Mapping-Projects/blob/master/Regional-Goods-Movement/scripts/Python/Create_Northern_CA_Megaregion_Businesses_2016_FC.py)

2. Create Nothern California Megaregion Employment Density Feature Classes

    
3. Employment Summary by Goods Movement Class / Supply Chain Class 

    [Create Megaregion Employment Summaries](https://github.com/BayAreaMetro/Spatial-Analysis-Mapping-Projects/blob/master/Regional-Goods-Movement/scripts/Python/Create_Megaregion_Employment_Summaries.py)

### Detailed 

**Create Northern California Megaregion Business FC** 

Script:

- [Create Northern California Megaregion Business FC Script](https://github.com/BayAreaMetro/Spatial-Analysis-Mapping-Projects/blob/master/Regional-Goods-Movement/scripts/Python/Create_Northern_CA_Megaregion_Businesses_2016_FC.py)

Input:

- [California Business Data](#data-sources)
- [Northern California Megaregion Counties](#feature-classes--csvs)

Output: 

- [GMS 2016 North CA Megaregion Businesses](#feature-classes--csvs)

Output Data Dictionary: 
Four fields were added to the original [GMS_2016_CA_Businesses](#feature-classes--csvs) feature class; the full domain of each field is summarized in the table below:

|Field Name     |Values              |
|---------------|--------------------|
|County         |Alameda, Contra Costa, El Dorado, Marin, Merced, Monterey, Napa, Placer, Sacramento, San,Benito, San Francisco, San Joaquin, San Mateo, Santa Clara, Santa Cruz, Solano, Sonoma, Stanislaus, Sutter, Yolo, Yuba|
|Region         |Bay Area, Monterey Bay Area, Northern San Joaquin Valley, Sacramento Area|
|Goods_Mvmt_Class |1, 2, 3 See: [NAICS Mapping to Goods Movement Classes](https://github.com/BayAreaMetro/Spatial-Analysis-Mapping-Projects/blob/master/Regional-Goods-Movement/data/NAICS_Mapping_to_Goods_Mvmt_Classes.csv)|
|Supply_Chain_Class |1, 2, 3, 4, 5, 6 See: [NAICS Mapping to Supply Chain Classes](https://github.com/BayAreaMetro/Spatial-Analysis-Mapping-Projects/blob/master/Regional-Goods-Movement/data/NAICS_Mapping_to_Supply_Chain_Classes.csv)|

**Create Northern Claifornia Mega Region Employment Density Feature Classes**

Two custom tools were created using ArcGIS Pro Model Builder to generate the final output feature class, as well as intermediary feature classes & rasters. The feature class generated highlights employment density within [FMMP Urban and Built Up](http://www.conservation.ca.gov/dlrp/fmmp/mccu/Pages/map_categories.aspx) areas. The toolbox containing the tools is linked below. Assumptions are maintained as defaults within the tools.

***Select By Attribute Create Point Density Raster*** 

Tool: [Select_By_Attr_Create_Point_Density_Raster](#tools) 

![Select by Attr Create Point Density Raster Model](https://github.com/BayAreaMetro/Spatial-Analysis-Mapping-Projects/blob/master/Regional-Goods-Movement/readme_images/Screen%20Shot%202017-05-25%20at%2010.54.57%20AM.png)

Input: 

- [GMS 2016 North CA Megaregion Businesses](#feature-classes--csvs)

Tool Input Values: 

  - Population field: EMPNUM
  - Expressions: 
      - All Industries: ```'Goods_Mvmt_Class IN (1,2,3)'``` 
      - Core Industries: ```'Goods_Mvmt_Class = 1'```
      - Dependent Industries: ```'Goods_Mvmt_Class = 2'```
      - Supported Industries: ```'Goods_Mvmt_Class = 3'```
      - Production: ```'Supply_Chain_Class = 1'```
      - Transportation: ```'Supply_Chain_Class = 2'``` 
      - Distribution: ```'Supply_Chain_Class = 3'```
      - Retail: ```'Supply_Chain_Class = 4'```
      - Waste: ```'Supply_Chain_Class = 5'```
  - Output Cell Size: 20
  - Mask: [NC_Mega_Region_FMMP_Urban_2014_SF (Polygon)](#feature-classes--csvs)
    - Built - up areas

Tool Assumptions: 

![Point Density Inputs](https://github.com/BayAreaMetro/regional-goods-movement/blob/master/Northern-California-Megaregion-Employment-Density-Maps/readme_images/Screen%20Shot%202017-06-08%20at%2010.12.04%20AM.png)

## Expected Outcomes 

## Results 

### Tools

### Maps, Charts, and Graphics

### Feature Classes & CSVs