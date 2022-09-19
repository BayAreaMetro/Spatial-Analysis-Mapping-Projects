**Draft**

# Senate Bill 35 Affordable Housing Streamlining Analysis

## Define the Problem Statement

The purpose of this analysis is to develop a geographic feature overlay which represents geographies within the Bay Area which are excluded from the recently passed SB-35 Planning and zoning: affordable housing: streamlined approval process bill.  

## Analysis Parameters

### SB-35 Planning and zoning: affordable housing: streamlined approval process.(2017-2018)
- [Senate Bill No. 35](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=201720180SB35)

## Data Sources

[SB35 Datasets File Geodatabase](https://mtcdrive.box.com/s/jzb2yr770oisekql24x0brf9f0svrsq3)

### SB-35 Sec 3

#### 2. The development is located on a site that satisfies all of the following:

##### A) United States Census Urbanized Area / Urban Custer

A site that is a legal parcel or parcels located in a city if, and only if, the city boundaries include some portion of either an urbanized area or urban cluster, as designated by the United States Census Bureau, or, for unincorporated areas, a legal parcel or parcels wholly within the boundaries of an urbanized area or urban cluster, as designated by the United States Census Bureau.
   
[View Map Data](http://mtc.maps.arcgis.com/home/item.html?id=7ed44bd8d6964a21a88205b50fa7c9e7)

[2017 Urban Areas TIGER/Line Shapefile](https://www.census.gov/geo/maps-data/data/tiger-line.html)


#### 6. The development is not located on a site that is any of the following:

##### A) California Coastal Zones

A coastal zone, as defined in Division 20 (commencing with Section 30000) of the Public Resources Code.
   
[View Map Data] (Needs updated URL)

##### B) Protected Agricultural Lands (FMMP)

Either prime farmland or farmland of statewide importance, as defined pursuant to United States Department of Agriculture land inventory and monitoring criteria, as modified for California, and designated on the maps prepared by the Farmland Mapping and Monitoring Program of the Department of Conservation, or land zoned or designated for agricultural protection or preservation by a local ballot measure that was approved by the voters of that jurisdiction.
   
[View Map Data] (Needs updated URL)

##### C) United States Fish and Wildlife Service Wetland Areas

Wetlands, as defined in the United States Fish and Wildlife Service Manual, Part 660 FW 2 (June 21, 1993).

[View Map Data] (Needs updated URL)

##### D) Department of Forestry and Fire Protection Fire Hazard Areas

Within a very high fire hazard severity zone, as determined by the Department of Forestry and Fire Protection pursuant to Section 51178, or within a high or very high fire hazard severity zone as indicated on maps adopted by the Department of Forestry and Fire Protection pursuant to Section 4202 of the Public Resources Code. This subparagraph does not apply to sites excluded from the specified hazard zones by a local agency, pursuant to subdivision (b) of Section 51179, or sites that have adopted fire hazard mitigation measures pursuant to existing building standards or state fire mitigation measures applicable to the development.
   
[View Map Data] (Needs updated URL)

##### E) Hazardous Waste Sites 
(50 meter Buffer around location centroid)

A hazardous waste site that is listed pursuant to Section 65962.5 or a hazardous waste site designated by the Department of Toxic Substances Control pursuant to Section 25356 of the Health and Safety Code, unless the Department of Toxic Substances Control has cleared the site for residential use or residential mixed uses.
   
[View Map Data] (Needs updated URL)

##### F) Dilineated Earthquake Fault Zones (Alquist Priolo)

Within a delineated earthquake fault zone as determined by the State Geologist in any official maps published by the State Geologist, unless the development complies with applicable seismic protection building code standards adopted by the California Building Standards Commission under the California Building Standards Law (Part 2.5 (commencing with Section 18901) of Division 13 of the Health and Safety Code), and by any local building department under Chapter 12.2 (commencing with Section 8875) of Division 1 of Title 2.
   
[View Map Data] (Needs updated URL)

##### G/H) Flood Zones and Floodways 

- G) Within a flood plain as determined by maps promulgated by the Federal Emergency Management Agency, unless the development has been issued a flood plain development permit pursuant to Part 59 (commencing with Section 59.1) and Part 60 (commencing with Section 60.1) of Subchapter B of Chapter I of Title 44 of the Code of Federal Regulations.
- H) Within a floodway as determined by maps promulgated by the Federal Emergency Management Agency, unless the development has received a no-rise certification in accordance with Section 60.3(d)(3) of Title 44 of the Code of Federal Regulations.

[View Map Data] (Needs updated URL)

** Amended on 2/20/18 to incllude only lnads within the 100yr. FEMA Floodplain. **

##### I) Conservation Lands

Lands identified for conservation in an adopted natural community conservation plan pursuant to the Natural Community Conservation Planning Act (Chapter 10 (commencing with Section 2800) of Division 3 of the Fish and Game Code), habitat conservation plan pursuant to the federal Endangered Species Act of 1973 (16 U.S.C. Sec. 1531 et seq.), or other adopted natural resource protection plan.
  
[View Map Data] (Needs updated URL)

##### J) Habitat Lands

Habitat for protected species identified as candidate, sensitive, or species of special status by state or federal agencies, fully protected species, or species protected by the federal Endangered Species Act of 1973 (16 U.S.C. Sec. 1531 et seq.), the California Endangered Species Act (Chapter 1.5 (commencing with Section 2050) of Division 3 of the Fish and Game Code), or the Native Plant Protection Act (Chapter 10 (commencing with Section 1900) of Division 2 of the Fish and Game Code).
 
[View Map Data] (Needs updated URL)
   
##### K) Lands under conservation easement.
   
[View Map Data] (Needs updated URL)

## Methodology applied to solve problem

### United States Census Urbanized Area / Urban Cluster Processing 

1. 2017 Urbanized Area shapefile downloaded
2. Urbanized Areas clipped to Bay Area Counties 
3. Urbanized Areas interesected with TomTom waterbodies erased 

### SB 35 Development Exclusion Areas

The following script was run within the ArcGIS Pro Arcpy window to create SB 35 Development Exclusion Areas: [Create SB35 Exclusion Area FC](Scripts/Create_SB35_Exclusion_Area_FC.py)

An Exclusion Area flag field was added to the resulting feature class using the following coded domain values: 

|Code    |Name                                                    |
|--------|--------------------------------------------------------|
|1       |Urbanized Area - Within One or More Exclusion Areas     |
|2       |Urbanized Area - Not Within Exclusion Areas             |


## Results 

### Data Sources and Concerns

This [document](https://mtcdrive.box.com/v/SB35DataSourcing) describes and sources the data used for this analysis.  It also includes data concerns that were raised by the Data Analyst's who performed this work.

### Final Datasets 

[SB35 Map Overlay] (Needs updated URL)

### File Geodatabases

-[SB35 Datasets](https://mtcdrive.box.com/s/1y23w9hnexhztcuebovqa3jdga3ckhkm)

### Maps 

[SB 35 Development Exclusion Interactive Map Explorer] (Needs updated URL)


