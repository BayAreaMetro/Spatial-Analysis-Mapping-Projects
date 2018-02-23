**Draft**

# Senate Bill 35 Affordable Housing Streamlining Analysis

## Define the Problem Statement

The purpose of this analysis is to develop a geographic feature overlay which represents geographies within the Bay Area which are excluded from the recently passed SB-35 Planning and zoning: affordable housing: streamlined approval process bill.  

## Analysis Parameters

### SB-35 Planning and zoning: affordable housing: streamlined approval process.(2017-2018)
- [Senate Bill No. 35](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=201720180SB35)

## Data Sources

### SB-35 Sec 3

#### 2. The development is located on a site that satisfies all of the following:

##### A) United States Census Urbanized Area / Urban Custer

A site that is a legal parcel or parcels located in a city if, and only if, the city boundaries include some portion of either an urbanized area or urban cluster, as designated by the United States Census Bureau, or, for unincorporated areas, a legal parcel or parcels wholly within the boundaries of an urbanized area or urban cluster, as designated by the United States Census Bureau.
   
[View Map Data](http://mtc.maps.arcgis.com/home/item.html?id=7ed44bd8d6964a21a88205b50fa7c9e7)

[2017 Urban Areas TIGER/Line Shapefile](https://www.census.gov/geo/maps-data/data/tiger-line.html)


#### 6. The development is not located on a site that is any of the following:

##### A) California Coastal Zones

A coastal zone, as defined in Division 20 (commencing with Section 30000) of the Public Resources Code.
   
[View Map Data](http://mtc.maps.arcgis.com/home/item.html?id=ff8001e7d2aa4dcbb56e0594fb6d7c9d)

##### B) Protected Agricultural Lands (FMMP)

Either prime farmland or farmland of statewide importance, as defined pursuant to United States Department of Agriculture land inventory and monitoring criteria, as modified for California, and designated on the maps prepared by the Farmland Mapping and Monitoring Program of the Department of Conservation, or land zoned or designated for agricultural protection or preservation by a local ballot measure that was approved by the voters of that jurisdiction.
   
[View Map Data](http://mtc.maps.arcgis.com/home/item.html?id=a1acb0ac981e4a70948ced1409d06120)

##### C) United States Fish and Wildlife Service Wetland Areas

Wetlands, as defined in the United States Fish and Wildlife Service Manual, Part 660 FW 2 (June 21, 1993).

[View Map Data](http://mtc.maps.arcgis.com/home/item.html?id=a9d61d4a89a04d949e0748e8e532e5cf)

##### D) Department of Forestry and Fire Protection Fire Hazard Areas

Within a very high fire hazard severity zone, as determined by the Department of Forestry and Fire Protection pursuant to Section 51178, or within a high or very high fire hazard severity zone as indicated on maps adopted by the Department of Forestry and Fire Protection pursuant to Section 4202 of the Public Resources Code. This subparagraph does not apply to sites excluded from the specified hazard zones by a local agency, pursuant to subdivision (b) of Section 51179, or sites that have adopted fire hazard mitigation measures pursuant to existing building standards or state fire mitigation measures applicable to the development.
   
[View Map Data](http://mtc.maps.arcgis.com/home/item.html?id=924f1ea2170f47feb54ad3a88da35414)

##### E) Hazardous Waste Sites 
(50 meter Buffer around location centroid)

A hazardous waste site that is listed pursuant to Section 65962.5 or a hazardous waste site designated by the Department of Toxic Substances Control pursuant to Section 25356 of the Health and Safety Code, unless the Department of Toxic Substances Control has cleared the site for residential use or residential mixed uses.
   
[View Map Data](http://mtc.maps.arcgis.com/home/item.html?id=e949a47152b64c0f823bb39a1502e07a)

##### F) Dilineated Earthquake Fault Zones (Alquist Priolo)

Within a delineated earthquake fault zone as determined by the State Geologist in any official maps published by the State Geologist, unless the development complies with applicable seismic protection building code standards adopted by the California Building Standards Commission under the California Building Standards Law (Part 2.5 (commencing with Section 18901) of Division 13 of the Health and Safety Code), and by any local building department under Chapter 12.2 (commencing with Section 8875) of Division 1 of Title 2.
   
[View Map Data](http://mtc.maps.arcgis.com/home/item.html?id=d5b110c4582f45f697bbe0b90b92c801)

##### G/H) Flood Zones and Floodways 

- G) Within a flood plain as determined by maps promulgated by the Federal Emergency Management Agency, unless the development has been issued a flood plain development permit pursuant to Part 59 (commencing with Section 59.1) and Part 60 (commencing with Section 60.1) of Subchapter B of Chapter I of Title 44 of the Code of Federal Regulations.
- H) Within a floodway as determined by maps promulgated by the Federal Emergency Management Agency, unless the development has received a no-rise certification in accordance with Section 60.3(d)(3) of Title 44 of the Code of Federal Regulations.

[View Map Data](http://mtc.maps.arcgis.com/home/item.html?id=01c95836d68e4867a09217f0bcad9c9c)

##### I) Conservation Lands

Lands identified for conservation in an adopted natural community conservation plan pursuant to the Natural Community Conservation Planning Act (Chapter 10 (commencing with Section 2800) of Division 3 of the Fish and Game Code), habitat conservation plan pursuant to the federal Endangered Species Act of 1973 (16 U.S.C. Sec. 1531 et seq.), or other adopted natural resource protection plan.
  
[View Map Data](http://mtc.maps.arcgis.com/home/item.html?id=125208c46aae476eb11a857dd222868d)

##### J) Habitat Lands

Habitat for protected species identified as candidate, sensitive, or species of special status by state or federal agencies, fully protected species, or species protected by the federal Endangered Species Act of 1973 (16 U.S.C. Sec. 1531 et seq.), the California Endangered Species Act (Chapter 1.5 (commencing with Section 2050) of Division 3 of the Fish and Game Code), or the Native Plant Protection Act (Chapter 10 (commencing with Section 1900) of Division 2 of the Fish and Game Code).
 
[View Map Data](http://mtc.maps.arcgis.com/home/item.html?id=c3ab3154473b4145a4e8d7c66694e244)
   
##### K) Lands under conservation easement.
   
[View Map Data](http://mtc.maps.arcgis.com/home/item.html?id=3e38d92bda55453799f854286cee079d)

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

[SB35 Map Overlay](http://mtc.maps.arcgis.com/home/item.html?id=bfb749aaa6354c02a451930b5429e058)

### Data Summaries

### Maps 

[SB 35 Development Exclusion Interactive Map Explorer](https://mtc.maps.arcgis.com/apps/webappviewer/index.html?id=8198cf51d0c5459484b95cea6d04e86d)

[Draft Map Illustrating Development Exclusion Areas (7.7 mb pdf)](https://mtcdrive.box.com/s/awhypc55gmhxvnp5z7i8ez8vx99b1t77)

![SB 35 Map](https://mtcdrive.box.com/shared/static/jkgmpace3hrqig8ycv6iuw47bbxb6rw8.png)

