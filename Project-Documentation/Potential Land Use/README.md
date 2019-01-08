# Documentation
Geospatial procedure and tabular analysis of Cal EnviroScreen 3.0 Total Population in 

### Define the Problem Statement  

How do we inform our 9-county regional land use model of the local land use plans?

This land use model feeds into the travel demand model thereby determining levels of transportation infrastructure investment. In order to capture Bay Area land use, MTC has developed a process for accounting for the small-scale decision-making at the jurisdictional level. Thanks to the BASIS (Bay Area Spatial Information System) effort we have been able to collect all 101 Bay Area jurisdiction's current planning documents and spatial datasets. For this particular effort, zoning, general plans, and specific plans were leveraged to determine the current land use for all 2.14 million parcels in the Bay Area region. Not only were we able to determine current land use, we constructed a decision tree to help land use modelers predict land development for various long-range planning scenarios.


### Project Management 

- [Asana Project](https://app.asana.com/0/797943099119526/901683629619975) 
- [Box](https://mtcdrive.box.com/s/x72b3z6uobofeo6k493m2j3xg0ewt7zb)

### Contents 

- [Data Sources](#data-sources)
- [Analysis Parameters](#analysis-parameters)
- [Methodology](#methodology)
- [Expected Outcomes](#expected-outcomes)
- [Results](#results)

## Data Sources  

[CalEnviroScreen 3.0 Data 'CES3FINAL_AGOL'](https://mtc.maps.arcgis.com/home/item.html?id=98b9a819a670470c96babc63d6857959)  
 
## Analysis Parameters  
  

## Methodology  

1. Open [CalEnviroScreen 3.0 Data 'CES3FINAL_AGOL'](https://mtc.maps.arcgis.com/home/item.html?id=98b9a819a670470c96babc63d6857959) in ArcPro.  
2.  Apply query to feature service layer:  
    CES2018Update_changingcolumns_2 = '75-80%' Or CES2018Update_changingcolumns_2 = '80-85%' Or CES2018Update_changingcolumns_2 = '85-90%' Or CES2018Update_changingcolumns_2 = '90-95%' Or CES2018Update_changingcolumns_2 = '95-100% (highest scores)'
3. Export as new feature service layer
4. Summarize by county

## Expected Outcomes

An interactive AGOL web map showcasing only Bay Area Disadvantaged Communities based on the [CalEnviroScreen 3.0](https://oehha.ca.gov/calenviroscreen/report/calenviroscreen-30) data contcreated by the [Office of Environmental Health Hazard Assessment (OEHHA)](https://oehha.ca.gov/).  


## Final Tabular Data Results  

Percentile Range ('CES_3_0Pctl_Range2018') greater than 75%

| Bay Area Counties  	| 2010 Total Population | 
|-----------------------|-----------------------|
| Alameda               | 148,268           	| 
| Contra Costa	 	 	| 140,335	            | 
| Marin	 	 	        | 0	                    | 
| Napa                  | 0 	                | 
| San Francisco	 	 	| 43,189                |  
| San Mateo	 	        | 34,954	            | 
| Santa Clara           | 71,936                | 
| Solano    	 	 	| 17,287 	            | 
| Sonoma 	 	        | 7,522	                | 
| Regional total        | 463,491               | 


### Final Web Map Data Results  

[Bay Area DACs](https://mtc.maps.arcgis.com/home/webmap/viewer.html?webmap=fb249db7b20644f7b94ecd8a0d8c2207&extent=-124.0323,37.1176,-120.6567,38.5514)  


