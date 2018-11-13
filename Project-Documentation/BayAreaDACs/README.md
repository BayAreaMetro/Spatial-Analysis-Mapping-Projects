# Documentation
Geospatial procedure and tabular analysis of Cal EnviroScreen 3.0 Total Population in the Bay Area.  

### Define the Problem Statement  

Where are the Bay Area Disadvantaged Communities (DACs) and what is the associated population in those communities?  

According to the [CalEnviroScreen 3.0 mapping tool](https://oehha.maps.arcgis.com/apps/webappviewer/index.html?id=4560cfbce7c745c299b2d0cbb07044f5)by way of the [Office of Environmental Health Hazard Assessment (OEHHA)](https://oehha.ca.gov/), roughly 460,00 Bay Area resident are at risk to pollutants, poor environmental conditions and less than diresable economic conditions.  

[CalEnviroScreen 3.0](https://oehha.ca.gov/calenviroscreen/report/calenviroscreen-30) ranks census tracts in California based on potential exposures to pollutants, adverse environmental conditions, socioeconomic factors and prevalence of certain health conditions. Data used in the CalEnviroScreen model come from national and state sources.  

[Disadvantaged communities in California](https://oehha.ca.gov/calenviroscreen/sb535) are specifically targeted for investment of proceeds from the State’s cap-and-trade program. These investments are aimed at improving public health, quality of life and economic opportunity in California’s most burdened communities at the same time reducing pollution that causes climate change.  

### Project Management 

- [Asana Project](https://app.asana.com/0/inbox/797943099119524/835368168562377/835368168562378) 
- [Box](https://mtcdrive.box.com/s/89x2ysamyj1u3kd4hettly9ydb8xhk0a)

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


## Results  

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


### Final Tabular Data Summaries  

[Bay Area DACs](https://mtc.maps.arcgis.com/home/webmap/viewer.html?webmap=fb249db7b20644f7b94ecd8a0d8c2207&extent=-124.0323,37.1176,-120.6567,38.5514)  


