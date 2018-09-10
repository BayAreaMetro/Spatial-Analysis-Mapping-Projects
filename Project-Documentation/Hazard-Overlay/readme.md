**Draft Status: (Draft)**

## Define the Problem Statement
The purpose of this project is to build an application that allows users to search for an address, and receive feedback on whether that address is impacted by certain geological hazards.

The goal is to be able to say that an address is positively impacted by a geological hazard if all or part of the parcel intersects that hazard.

In order to accomplish this, a dataset needs to be developed based on parcel features, with attributes indicating whether each parcel is in/out of a specific hazard. 

### Project Management 
- [Task on Asana](https://app.asana.com/0/412103232252676/795829633431058/f)

## Data Sources
Zonal Geography:
1. [Parcels 2010](https://mtc.maps.arcgis.com/home/group.html?id=66c3ed0ebab0480788a9d2cf49afb57d#overview)

Hazards include: 
1. [Alquist-Priolo Fault Zone](https://mtc.maps.arcgis.com/home/item.html?id=1935ec41c8b04a21bff1ebb1e5c050ca)
2. [USGS Liquefaction Study Zone](https://mtc.maps.arcgis.com/home/item.html?id=044546a891414c90a17a54bb2aa594bb)
3. [Liquefaction Susceptibility Zones](https://mtc.maps.arcgis.com/home/item.html?id=b88a7506b3054189b2cbd475371b1199)
4. [Earthquake Induced Landslide Study Zones](https://mtc.maps.arcgis.com/home/item.html?id=2b40285fe87a402db105de31dd124dc0#overview)

## Analysis Parameters


## Methodology applied to solve problem
usgs_liquefaction_susceptibility  
Definition query out unnecessary classifications or display only relevant classifications  
	Ie1. Liq Not in (‘NM’,’L’,’VL’,’W’)  
	Ie2. Liq in (‘VH’,’H’,’M’)  
Field calculate new field to denote 1 = susceptibility while -1 = no liquefaction susceptibility.  

cgs_landslide_study_areas  
Definition query out unnecessary classifications or display only relevant classifications  
	Ie1. Mapping Not In (‘Area not…’,’Mapping Planned…’,’Mapping in Progress…’)  
	Ie2. Mapping = ‘Earthquake induced…'    
Field calculate new field to denote 1 = inside a landslide study area while -1 = outside landslide study areas.  

cgs_liquefaction_study_areas  
Definition query out unnecessary classifications or display only relevant classifications  
	Ie1. Mapping Not In (‘Area not…’,’Mapping Planned…’,’Mapping in Progress…’)  
	Ie2. Mapping = ‘Liquefaction Hazard…’  
Field calculate new field to denote 1 = inside liquefaction study area while -1 = outside liquefaction study areas.  

alquist_priolo_zones  
Definition query out unnecessary classifications or display only relevant classifications  
	Ie1. Ap_zone Not Null  
Field calculate new field to denote 1 = inside ap_zone while -1 = outside ap_zone.  

Once all four hazard layers have been formatted (all unnecessary classifications have been removed) then combine the four layers into a single hazard layer.

UNION  
cgs_liquefaction_study_areas  
cgs_landslide_study_areas  
usgs_liquefaction_susceptibility  
alquist_priolo_zones  

TABULATE INTERSECTION
	Zones:	Parcels2010  
	Zone Fields:	Parcel ID  
	Class Features:	Output of Union for all four hazard layers  
	Class Fields:  
		Binary new field denoting inclusion/exclusion of cgs_liquefaction_study_areas (liqcode)  
		Binary new field denoting inclusion/exclusion of cgs_landslide_study_areas (landcode)  
		Binary new field denoting inclusion/exclusion of usgs_liquefaction_susceptibility (liqsuscode)  
		Binary new field denoting inclusion/exclusion of alquist_priolo_zones (alqpricode)  
Sum Fields:	[leave blank]  
Output Units:	SQ METERS  

SUMMARY STATISTICS 
    Input:	Tabulate Intersections Output  
    Statistics Field:	Area SUM  
    Case field:	Parcel 2010  

PIVOT TABLE 1  
	Input:	Summary Statistics Output  
	Input fields:  
		Parcel ID, liqcode  
	Pivot field:	liqcode  
	Value field:	Area  

PIVOT TABLE 2  
	Input:	Summary Statistics Output  
	Input fields:  
		Parcel ID, landcode  
	Pivot field:	landcode  
	Value field:	Area  

PIVOT TABLE 3  
	Input:	Summary Statistics Output  
	Input fields:  
		Parcel ID, liqsuscode   
	Pivot field:	liqsuscode  
	Value field:	Area  

PIVOT TABLE 4  
	Input:	Summary Statistics Output  
	Input fields:  
		Parcel ID, alqpricode  
	Pivot field:	alqupricode  
	Value field:	Area  

## Expected Outcomes (if any)?


## Results


