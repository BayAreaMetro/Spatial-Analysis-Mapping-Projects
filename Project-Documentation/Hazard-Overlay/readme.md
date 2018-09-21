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
QUERY:  
usgs_liquefaction_susceptibility  
cgs_landslide_study_areas  
cgs_liquefaction_study_areas  
alquist_priolo_zones  
cgs_landslide susceptibilty  

UNION  
cgs_liquefaction_study_areas  
cgs_landslide_study_areas  
usgs_liquefaction_susceptibility  
alquist_priolo_zones  
cgs_landslide susceptibilty  

TABULATE INTERSECTION

SUMMARY STATISTICS  

## Expected Outcomes (if any)?


## Results


