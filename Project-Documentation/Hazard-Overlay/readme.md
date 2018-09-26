**Draft Status: (Draft)**

## Define the Problem Statement
The purpose of this project is to build an application that allows users to search for an address, and receive feedback on whether that address is impacted by certain geological hazards.

The goal is to determine if an address is positively impacted by a geological hazard if all or part of the parcel intersects that hazard.  

### Project Management 
- [Task on Asana](https://app.asana.com/0/412103232252676/795829633431058/f)  
- [Data on Box](https://mtcdrive.app.box.com/folder/53006798123)  

## Data Sources
Zonal Geography:
1. [Parcels 2010](https://mtcdrive.app.box.com/s/ny0olvpw64x6ftxwhbi34m2phm6hqzce)

Hazards include: 
1. [Alquist-Priolo Fault Zone](https://mtc.maps.arcgis.com/home/item.html?id=1935ec41c8b04a21bff1ebb1e5c050ca)
2. [USGS Liquefaction Study Zone](https://mtc.maps.arcgis.com/home/item.html?id=044546a891414c90a17a54bb2aa594bb)
3. [Liquefaction Susceptibility Zones](https://mtc.maps.arcgis.com/home/item.html?id=b88a7506b3054189b2cbd475371b1199)
4. [Earthquake Induced Landslide Study Zones](https://mtc.maps.arcgis.com/home/item.html?id=2b40285fe87a402db105de31dd124dc0#overview)  
5. [Landslide Susceptibility Zones](https://mtcdrive.app.box.com/s/6qa52hq69ifk15hk3bi1xjyey22bombl)

## Analysis Parameters
Dataset needs to be developed based on parcel features, with attributes indicating whether each parcel is in/out of a specific hazard. 


## Methodology applied to solve problem
###GIS & Tabular Analysis
####GIS Analysis:
1. Download Parcels 2010 & Hazard Layers  
    [Parcels 2010](https://mtcdrive.app.box.com/s/ny0olvpw64x6ftxwhbi34m2phm6hqzce)  
    [Alquist-Priolo Fault Zone](https://mtc.maps.arcgis.com/home/item.html?id=1935ec41c8b04a21bff1ebb1e5c050ca)  
    [USGS Liquefaction Study Zone](https://mtc.maps.arcgis.com/home/item.html?id=044546a891414c90a17a54bb2aa594bb)  
    [Liquefaction Susceptibility Zones](https://mtc.maps.arcgis.com/home/item.html?id=b88a7506b3054189b2cbd475371b1199)  
    [Earthquake Induced Landslide Study Zones](https://mtc.maps.arcgis.com/home/item.html?id=2b40285fe87a402db105de31dd124dc0#overview)  
    [Landslide Susceptibility Zones](https://mtcdrive.app.box.com/s/6qa52hq69ifk15hk3bi1xjyey22bombl)  
2. Project all layers to consistent coordinate system
3. Query all five hazard layers for only relevent geographies
    Ie. Landslide Susceptibility GRIDCODE>=7 (all areas with high landslide susceptibility or greater)
4. Export queried hazard layer feature to project geodatabase
5. Union new hazard layers to create single data layer feature class
    a. cgs_liquefaction_study_areas  
    b. cgs_landslide_study_areas  
    c. usgs_liquefaction_susceptibility  
    d. alquist_priolo_zones  
    e. cgs_landslide susceptibilty 
6. Run identity operation on [Parcels 2010](https://mtcdrive.app.box.com/s/ny0olvpw64x6ftxwhbi34m2phm6hqzce) features and single layer hazard feature class; output to project geodatabase  
7. Field Calculate new binary attribute denoting whether a parcel is either in/out of a specfic hazard layer.
8. Run dissolve function on Parcel_Id and sum the shape area for each associated hazard (5 fields in attribute table) for each record in order to determine shape area in/out of specific hazards in individual parcels.

####Tabular Analysis
9. Resulting dissolve table

  
SUMMARY STATISTICS  

## Expected Outcomes (if any)?


## Results

