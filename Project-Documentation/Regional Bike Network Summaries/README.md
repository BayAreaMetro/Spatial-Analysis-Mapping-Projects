# Documentation  

Bicycle and Pedestrian Program and Active Tranpsortaion Planning (https://mtc.ca.gov/our-work/plans-projects/casa-committee-house-bay-area) is requesting mapping support from MTC to identify areas of concern or “sensitive communities” in the 9-county Bay Area that could be exempted from certain CASA Compact policies.  

### Define the Problem Statement  

In 2009, how many miles are in the Regional Bike Network?
How much of the Regional Bike Network has been built since 2009?
How many miles are in the San Francisco Bay Trail Network?
How many miles are in both the SF Bay Trail and Regional Bike Network?
In 2019, how many miles are in the Regional Bike Network?

Congestion Management Agency (CMA)

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

[Regional Bike Facilities](https://mtc.maps.arcgis.com/home/item.html?id=0329d440fe65420a9650215a9cae459a)  
[Regional Bike Plan](https://mtc.maps.arcgis.com/home/item.html?id=ba40dbfa8ac04e9c99bf07011deba08f)  
[Regional CMA-provided datasets](https://mtcdrive.box.com/s/1vi8qiagys5u5irt55pbipijzsrqvd2w)    
    
## Analysis Parameters  

Update the built and not built summaries for all 9 Bay Area Counties according to the data provided by the CMAs  

## Methodology  

1. Upload all 9 Bike Network datasets and update to common projection: UTM NAD 83 Zone 10N  
2. Upload [Regional Bike Facilities](https://mtc.maps.arcgis.com/home/item.html?id=0329d440fe65420a9650215a9cae459a)  -this is all bicycle facilities 
3. Upload [Regional Bike Plan](https://mtc.maps.arcgis.com/home/item.html?id=ba40dbfa8ac04e9c99bf07011deba08f)  
4. Identify the facilities which are present in both 2009 Regional Bike Network and the CMA-provided current bicycle facltiies in 2019.
5. 

## Expected Outcomes  

Inform the Regional CMAs, Plan Bay Area and Bicycle and Pedstrian Commitees of updates to teh Regional Bicycle Newtork.  .  

## Results  
![San Francisco Bay Trail](https://github.com/BayAreaMetro/Spatial-Analysis-Mapping-Projects/blob/master/Project-Documentation/Regional%20Bike%20Network%20Summaries/img/2009RegionalBikeNetwork.pdf)

Summary

|Dataset                           | Built Mileage      | Unbuilt Mileage      | Mileage |
|--------------------------------- |------------------- |--------------------- |------------- |
|Regional Bike Network (RBN)       |1,013               |1,156   |2,169   |
|San Francisco Bay Trail in RBN    |353                 |213     |566     |
|Percentage of SF Bay Trail in RBN |35%   |18%     |26%     |




Bicycle Network 
2009 Summary

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

2019 Summary

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


