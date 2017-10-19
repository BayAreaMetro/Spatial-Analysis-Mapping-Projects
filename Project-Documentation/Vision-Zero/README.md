## Define the Problem Statement

- Create a polyline feature class using TomTom road network data and SWITRS/TIMS data that joins 'high injury' attributes from SWITRS/TIMS data to the road network. 
- Provide a summary network which extracts 'high injury' cooridors from the entire TomTom road network for the Bay Area
- Summarize SWITRS/TIMS data by Census Block 

## Data Sources

- TomTom Other Areas (mn_oa03_BayArea)
- TomTom Street Network (mn_nw_BayArea)
- [SWITRS/TIMS (2006-2016)](Data/Bay-Area-Accidents-2006-2016.csv) 

## Analysis Parameters

- [SWITRS/TIMS (2006-2016)](Data/Bay-Area-Accidents-2006-2016.csv) 

|Variable         |Description                                                          |
|-----------------|---------------------------------------------------------------------|
|killed           |Number of people killed (includes pedestrians and motorists)         |
|Sevinj           |Number of people severly injured (includes pedestrians and motorists)|
|Accident Year    |Year accident was reported                                           |
|LongitudeFixed   |Longitude (X coordinate)                                             |
|Latitude         |Latitude (Y coordinate)                                              |



## Methodology applied to solve problem

### Create High Injury Network Polyline 

1. Make XY Accident Layer from [SWITRS/TIMS (2006-2016)](Data/Bay-Area-Accidents-2006-2016.csv) (Make XY Event Layer Tool)
2. Copy XY Accident Layer to project GDB to create Feature Class 
3. Definition Query on TomTom Street Network (FRC not in 8) 
4. Add TomTom road attributes to Accidident Feature Class (Near Command)
5. Summarize Accident Feature Class by killed & sevinj - case by TomTom Object ID
6. Add join between TomTom Network FC and Accident Feature Class summary (using objectid) - uncheck keep all features (inner join)  


### Create High Injury Polygons (Using Census Blocks)

1. Make XY Accident Layer from [SWITRS/TIMS (2006-2016)](Data/Bay-Area-Accidents-2006-2016.csv) (Make XY Event Layer Tool)
2. Copy XY Accident Layer to project GDB to create Feature Class
3. Add 


## Expected Outcomes (if any)?

## Results
