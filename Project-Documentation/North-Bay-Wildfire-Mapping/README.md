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

## Analysis Parameters

## Methodology

### Calfire Active Fire Perimeters

1. Downloaded [Calfire Active Fires Data as kml](#data-sources)
2. Ran KML to Layer 
3. Exported perimeter features to project FGDB as [CalFire_Active_Fire_Perimeters_2017](#intermediate-data)
4. Run identity operation on perimeter features and Bay Area Counties and output to FGDB as [Calfire_Active_Fire_Perimeters_2017_Ident](#intermediate-data)

  4A. Delete water areas (FID_Bay_Area_Counties = -1) 

5. Dissolve perimeter features by fire name and county and output new feature to FGDB as [Calfire_Active_Fire_Perimeters_2017_disso](#final-data)

### Calfire Active Fire Perimeters Demographics 


## Expected Outcomes

### Maps  

- Print Map of North Bay Areas affected by wildfire overlain with PDAs, CoCs, SB35 Excluded Areas
- Interactive Map of North Bay Areas affected by wildfire overlain with PDAs, CoCs, SB35 Excluded Areas

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

### Intermediate Data 

### Final Data 

### Maps 
