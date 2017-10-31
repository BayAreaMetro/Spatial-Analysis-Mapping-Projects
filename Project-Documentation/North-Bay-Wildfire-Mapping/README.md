**Draft**

## North Bay Wildfire Mapping 

Perform spatial analysis of areas affected by the recent North Bay Fires which provides context through the lense of MTC policy layers. The analysis should also provide useful summaries related to impact on the build environment as well as the socio-economic inpact.  

### Project Management 

- [Asana Project](https://app.asana.com/0/461824428269313/461824428269323)
- [Box](https://mtcdrive.box.com/s/89urlw9t9q9mf9l2bkufk60q07twz4on)
- [AGOL](http://mtc.maps.arcgis.com/home/group.html?id=c51fa2042a1949f0b60a560eaddb7dfe&start=1#members)

### Contents 

- [Data Sources](#data-sources)
- [Analysis Parameters](#analysis-parameters)
- [Methodology](#methodology)
- [Expected Outcomes](#expected-outcomes)
- [Results](#results)

## Data Sources

- [Calfire 2017 Statewide Fire Map](https://www.google.com/maps/d/viewer?mid=1TOEFA857tOVxtewW1DH6neG1Sm0&hl=en&ll=38.875582273874265%2C-122.70712978515627&z=9)
  - Download as kml
- [SB35 Map Overlay (Draft)](http://mtc.maps.arcgis.com/home/item.html?id=db31a2a5392f479e976e39fbee80e82e)
- [Communities of Concern 2017](http://opendata.mtc.ca.gov/datasets/communities-of-concern-2017)
- [Priority Development Areas Current](http://opendata.mtc.ca.gov/datasets/priority-development-areas-current)
- [RHNA Sites](#intermediate-data)
- [ESRI Demographics](http://doc.arcgis.com/en/esri-demographics/)

## Analysis Parameters

## Methodology

### Calfire Active Fire Perimeters

1. Downloaded [Calfire Active Fires Data as kml](#data-sources)
2. Ran KML to Layer 
3. Exported perimeter features to project FGDB as [CalFire_Active_Fire_Perimeters_2017](#intermediate-data)
4. Run identity operation on perimeter features and Bay Area Counties and output to FGDB as [Calfire_Active_Fire_Perimeters_2017_County](#intermediate-data)

  4A. Delete water areas (FID_Bay_Area_Counties = -1) 
5. Run identity operation on perimeter features / counties & Bay Area Jurisdictions and output to FGDB as 
[Calfire_Active_Fire_perimeters_2017_County_Jurisdictions](#intermediate-data) 
6. Dissolve perimeter features by fire name and county, and jurisdiction & output new feature to FGDB as [Calfire_Active_Fire_Perimeters_2017_disso](#final-data)

### Calfire Active Fire Perimeters Demographics 

1. Run [North_Bay_Wildfire_Analysis.py script](scripts/North_Bay_Wildfire_Analysis.py) to add demographic data. Script uses enrich layer function which leverages [Esri Demographics](#data-sources)

### Calfire Active Fire Perimeters Policy 

1. Run identity function on [Calfire_Active_Fire_Perimeters_2017_disso](#final-data) and each policy layer
  - [RHNA](#intermediate-data)
  - [Priority Development Areas](#intermediate-data)
  - [SB35 Exclusion Areas](#intermediate-data)
  - [Communities of Concern](#intermediate-data)
2. Create new column called 'Policy_Intersect' 

|Value    |Description                      |
|---------|---------------------------------|
|0        |Not within policy area           |
|1        |Within policy area               |

3. Dissolve on fire perimeter name, county name, jurisdiction, and policy output as [Calfire_Active_Fire_Perimeters_2017_Policy](#final-data)
4. Add geometry attributes (acres) 

### Calfire Active Fire Demographics Land Use 

tbd

### Sonoma Co Structure Status
Feature Service for Structures that were either damaged or destroyed by the wildfires in Sonoma Co: 
[AGOL Feature Service](https://services1.arcgis.com/jUJYIo9tSA7EHvfZ/arcgis/rest/services/SonomaCounty_StructureStatus/FeatureServer/0)

[AGOL Map Layer](http://mtc.maps.arcgis.com/home/item.html?id=0e426949c4334fc7ba962086bfdaf7ac)

### Napa County Bldg Dept. Structures (Inspections)
Feature Service showing locations where structures were damaged in Napa County.  Includes All Buildings within Napa County
[](https://services1.arcgis.com/Ko5rxt00spOfjMqj/arcgis/rest/services/Building_Inspections_Fire_2017/FeatureServer/0/)

## Expected Outcomes

### Maps  

- Print Map of North Bay Areas affected by wildfire overlain with PDAs, CoCs, SB35 Excluded Areas

### Data Summaries 

- Parcels 
   - total number of affected parcels  
   - Parcel type (single family, multi-family, public land, other?)
- Amount of housing growth projected by PBA2040
- Population affected 
   - Total population 
   - Racial composition 
   - Income 
   - Age 
   - Rent vs. Own 

## Results

### Final Tabular Data Summaries

- [NorthBay_Wildfire_Analysis](https://mtcdrive.box.com/s/cc8hyrye9324gov8xb5baqa33og71etj) 

### Intermediate Data 

- [Intermediate Data (Data not in a feature dataset)](https://mtcdrive.box.com/s/hydrtfxra68t7odey4wm0qyoej70r822)

### Final Data 

- [Final](https://mtcdrive.box.com/s/hydrtfxra68t7odey4wm0qyoej70r822)
  - Calfire_Active_Fire_Perimeters_2017_disso
  - Calfire_Active_Fire_Perimeters_2017_Demo
  - Calfire_Active_Fire_Perimeters_2017_Policy
  - Calfire_Active_Fire_Perimeters_2017_LandUse_disso

### Maps 

- [NorthBayWildfireMap_LandUse_V1](https://mtcdrive.box.com/s/1yq7p3lpc7ib4j2ppo2mp7kvo4uwv3a9)
- [NorthBayWildfireMap_Policy_V1](https://mtcdrive.box.com/s/ewewbabivx0b5s72j3rr2s3dgj3yka4f)
