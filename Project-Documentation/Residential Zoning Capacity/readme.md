**Completetion Status: (Draft)**

## Define the Problem Statement
Using recently collected zoning data for jurisdictions in the San Francsico Bay Area Region, determine residential housing unit capacity within a half mile of existing rail stations across the region.

## Data Sources
[Jurisdiction Zoning](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/policy-mdm/land-use.md#zoning)   
[Passenger Rail Stations](https://mtc.maps.arcgis.com/home/item.html?id=efd75b7bb3c04dbda06c6e7cd73e9336)  


## Analysis Parameters
Using residenital zoning capacity (expressed as dwelling units per acre), estimate the number of residneital units that can be built based upon the max number of units that can be built on a parcel given the dwelling units per/acre densities reported by jurisdiction's zoning ordinances for locations within a half-mile of the nearest rail station.  

Also prepare estimate of housing units by year from 2010 to 2019.  This estimate will also contain estiamtes for the following demographic characteristics for housing:  

2019 Owner Occupied HUs.   
2019 Owner Occupied HUs: Percent.   
2019 Renter Occupied HUs.   
2019 Renter Occupied HUs: Percent.   
2010 Owner-occupied HUs.   
2010 Owner-occupied HUs: Percent.   
2010 Renter-occupied HUs.   
2010 Renter-occupied HUs: Percent.   
2019 Vacant Housing Units.   
2019 Vacant Housing Units: Percent.   
2010 Vacant Housing Units.   
2010 Vacant Housing Units: Percent.   

Create breakout by select transit providers (BART, Caltrain, MUNI, VTA).  

## Methodology applied to solve problem  
To determine residential capacity, each jurisdictions residential zoning data was used to calculate the number of allowable units by multiplying the metric **Dwelling Units/Acre X Total Acres** for each given parcel.

### Processing Steps
Create a BPM Diagram that illustrates the data processing steps used to generate the results. --Not Yet Done

## Expected Outcomes (if any)?
The outcome of this analysis should represent total residential capacities within a walkable distance around existing rail stations in the bay area.  

**Note:** As of this posting (October 7, 2019), the residential zoning data is still being confirmed by local jurisdictions.  There are numberous locations across this dataset that have missing or incomplete zoning capacity information.  We are working towards completing this collection and will rerun this analysis once we have a confirmed regional zoning dataset for the 9 county Bay Area region.

## Results  
The results have been uploaded to ArcGIS Online and can be viewed using the following links:  
[Interactive Web Map](https://arcg.is/00Lua5)  
[Excel Workbook](https://mtcdrive.box.com/s/2a6c4hwdl5eowq7hgkmysbyku8pf5jx2)
