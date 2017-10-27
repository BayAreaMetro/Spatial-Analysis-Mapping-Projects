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


## Methodology

### Create Accident / Incident Point Features 

1. Make XY Accident Layer from [SWITRS/TIMS (2006-2016)](Data/Bay-Area-Accidents-2006-2016.csv) (Make XY Event Layer Tool)
2. Copy XY Accident Layer to project GDB to create Feature Class 

### Create High Injury Network Polyline Features 
 
1. Definition Query on TomTom Street Network (FRC not in 8) 
2. Add TomTom road attributes to Accidident Feature Class (Near Command)
3. Run [VZ_Road_Network_Incident_Summary](Scripts/VZ_Road_Network_Incident_Summary.sql) script to create high injury network cooridors
   - Aggregate road geometries 
   - Group by: 
      - Road Name (where available from TomTom Street Network)
      - Highway shield # (Where available from TomTom Street Network)
      - KPH (Speed limits as provided by TomTom (Converted to MPH for final output))
      - Postal Code (Smallest available geographic identify where available from TomTom Street Network)
      - County Name (from TomTom Street Network)
      - County FIPS (from TomTom Street Network) 

### Create High Injury Polygons Features (Using Census Blocks)

TBD

## Expected Outcomes (if any)?

## Results

[vz_hin_2006_2017_mn_nw_bayarea (Draft)](http://mtc.maps.arcgis.com/home/item.html?id=7c3180199f8949e2861285dc2437b838)