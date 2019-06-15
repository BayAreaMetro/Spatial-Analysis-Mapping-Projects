# Documentation  

![test](https://mtcdrive.box.com/s/wp8jslbumoh67j9zgznkxw5lwzw6020g)

Active Tranportation Planners in the [Bicycle and Pedestrian Planning Department](https://mtc.ca.gov/our-work/plans-projects/bicycle-pedestrian-planning) at MTC/ABAG are requesting mapping support from the [Data Visualization Department](http://opendata.mtc.ca.gov/) to identify bicycle facilities built since 2009 in the 9-county Bay Area based on data provided by local Congestion Management Agencies (CMAs).  

### Define the Problem Statement  

In 2009, how many miles are in the Regional Bike Network?  
How much of the Regional Bike Network has been built since 2009?  
How many miles are in the San Francisco Bay Trail Network?  
How many miles of the SF Bay Trail are in the Regional Bike Network?  

Mapping support will summarize the provided bike network datasets obtained from CMAs in late 2018.

In terms of this request, the 2009 Regional Bike Network is refering to the Regional Bike Plan feature class and the 2009 Regional Bike Facilities is the union of all bicycle facilities regardless of regional significance. And both contained on MTC GIS AGOL
  
### Project Management 

- [Asana Project](https://app.asana.com/0/875072065401370/875078790897293) 
- [Box](https://mtcdrive.box.com/s/6441z731nw4np0j0yt13xk65nmebjtp5)

### Contents 

- [Data Sources](#data-sources)
- [Analysis Parameters](#analysis-parameters)
- [Methodology](#methodology)
- [Expected Outcomes](#expected-outcomes)
- [Results](#results)

## Data Sources  

[San Francisco Bay Trail](https://mtc.maps.arcgis.com/home/item.html?id=7555b7dd7da546db8196241292e58144)  
[Regional Bike Facilities](https://mtc.maps.arcgis.com/home/item.html?id=0329d440fe65420a9650215a9cae459a)  
[Regional Bike Plan](https://mtc.maps.arcgis.com/home/item.html?id=ba40dbfa8ac04e9c99bf07011deba08f)  
[Regional CMA-provided datasets](https://mtcdrive.box.com/s/1vi8qiagys5u5irt55pbipijzsrqvd2w)  

    
## Analysis Parameters  

Update the built and not built summaries for all 9 Bay Area Counties according to the data provided by the CMAs  

## Methodology  

1. Upload all 9 Bike Network datasets and update to common projection: UTM NAD 83 Zone 10N  
2. Upload [Regional Bike Facilities](https://mtc.maps.arcgis.com/home/item.html?id=0329d440fe65420a9650215a9cae459a)  -this is all bicycle facilities  
3. Upload [Regional Bike Plan](https://mtc.maps.arcgis.com/home/item.html?id=ba40dbfa8ac04e9c99bf07011deba08f)  
4. Upload [SF Bay Trail](https://mtc.maps.arcgis.com/home/item.html?id=7555b7dd7da546db8196241292e58144)  
5. Identify the facilities in 2009 Regional Bike Network and the SF Bay Trail in 2018.  
6. Identify the facilities in 2009 Regional Bike Network and current county bicycle facilities in 2018.  
7. Spatially erase 2018 data from the 2009 data (SF Bay Trail and county-level datasets)  
8. Then erase results from step 7 from 2009 data.  
9. Create attribute 'status2018' then flag resulting dataset from step 7 by field calculating as 'unbuilt'.  
10. Create attribute 'status2018' then flag resulting dataset from step 8 by field calculating as 'built'.  
11. Merge outputdatasets from steps 9 and 10.  
12. Spatial join the merge output fro step 11 to 2009 Regional Bike Plan dataset.  
13. Create attribute 'new2018status' then flag final results accordingly:  

|Query                                          | Flag                             |  
|---------------------------------------------- |--------------------------------- |  
|status in ('Built', 'Existing')                |new2018status = 'Existed in 2009' |  
|status = 'Unbuilt' And status2018 = 'unbuilt'  |new2018status = 'Unbuilt in 2018' |  
|status = 'Unbuilt' And status2018 = 'built'    |'Built since 2009'                |  

## Expected Outcomes  

Inform the Regional CMAs, Plan Bay Area and Bicycle and Pedstrian Commitees of updates to teh Regional Bicycle Newtork.  .  

## Results  
![San Francisco Bay Trail](https://github.com/BayAreaMetro/Spatial-Analysis-Mapping-Projects/blob/master/Project-Documentation/Regional%20Bike%20Network%20Summaries/img/SFBayTrail.pdf)  

|Dataset                           | Built Mileage      | Unbuilt Mileage      | Mileage |
|--------------------------------- |------------------- |--------------------- |------------- |
|Regional Bike Network (RBN)       |1,013               |1,156   |2,169   |
|San Francisco Bay Trail in RBN    |353                 |213     |566     |
|Percentage of SF Bay Trail in RBN |35%   |18%     |26%     |  

Source: [San Francisco Bay Trail](https://mtc.maps.arcgis.com/home/item.html?id=7555b7dd7da546db8196241292e58144)  

![2009 Regional Bike Network (Regional Bike Plan)](https://github.com/BayAreaMetro/Spatial-Analysis-Mapping-Projects/blob/master/Project-Documentation/Regional%20Bike%20Network%20Summaries/img/2009RegionalBikeNetwork.pdf)  

|County        |Total Built Mileage |Total Unbuilt Mileage |Total Mileage |Percent Built |
|--------------|------------------- |--------------------- |------------- |------------- |
|Alameda       |161 |187   |348   |46% |
|Contra Costa  |181 |138   |319   |57% |
|Marin         |37  |81    |118   |31% |
|Napa          |39  |61    |99    |39% |
|San Francisco |58  |47    |106   |55% |
|San Mateo     |141 |104   |245   |58% |
|Santa Clara   |241 |182   |423   |57% |
|Solano        |71  |110   |180   |39% |
|Sonoma        |59  |214   |273   |22% |
|Total         |988 |1,124 |2,111 |47% |  

Source: [2009 Regional Bike Network (Regional Bike Plan)](https://mtc.maps.arcgis.com/home/item.html?id=0329d440fe65420a9650215a9cae459a)  

![2018 Regional Bike Network (Regional Bike Plan)](https://github.com/BayAreaMetro/Spatial-Analysis-Mapping-Projects/blob/master/Project-Documentation/Regional%20Bike%20Network%20Summaries/img/2018RegionalBikeNetwork_v3.pdf)  

|County        |Total Built Mileage |Total Unbuilt Mileage |Total Mileage |Percent Built |
|--------------|------------------- |--------------------- |------------- |------------- |
|Alameda       |251   |102   |353   |71% |
|Contra Costa  |227   |110   |337   |67% |
|Marin         |82    |43    |125   |66% |
|Napa          |84    |40    |124   |68% |
|San Francisco |95    |11    |106   |90% |
|San Mateo     |167   |78    |245   |68% |
|Santa Clara   |331   |93    |424   |78% |
|Solano        |126   |57    |183   |69% |
|Sonoma        |82    |191   |273   |30% |
|Total         |1,445 |1,124 |2,170 |67% |  

Source: [2018 Updated Regional Bike Network](https://mtc.maps.arcgis.com/home/item.html?id=0329d440fe65420a9650215a9cae459a)  
