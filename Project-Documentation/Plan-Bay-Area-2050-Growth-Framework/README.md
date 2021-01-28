## Plan Bay Area 2050 Growth Framework Mapping and Analysis

The purpose of this page is to document working related to creating and analyzing Priority Development Areas (PDAs), Priority Conservation Areas (PCAs), and Priority Production Areas (PPAs) which will comprise [Plan Bay Area 2050's](https://www.planbayarea.org) Regional Growth Framework, the Bay Area's strategy for coordinating housing and job growth. 

### Project Management 

- [Box Directory](https://mtcdrive.box.com/s/37oi8htx8ljxmdxxrqh4qvl3d035r0j5)
- [PBA 2050 Growth Framework Group (Team Access Only)](https://mtc.maps.arcgis.com/home/group.html?id=a755c580bb9e459fa97cdb5817dc7da9#overview) 
- [PBA 2050 Growth Framework Exploratory Map (Team Access Only)](https://arcg.is/1Oa9HS0)

### Table of Contents
- [Data Sources](#data-sources)
	- [Priority Development Area Data](#priority-development-area-data)
	- [Priority Production Area Data](#priority-production-area-data)
	- [Transit Rich Area Data](#transit-rich-area-data)
	- [High Resource Area Data](#high-resource-area-data)
	- [PDA Eligible Area Data Sources](#pda-eligibile-area-data-sources)
	- [PPA Eligible Area Data Sources](#ppa-eligible-area-data-sources)
- [Analysis Parameters](#analysis-parameters)
	- [Regional Growth Framework Update](#regional-growth-framework-update)
	- [PDA Eligible Area Criteria](#pda-eligible-area-criteria)
- [Methdology](#methodology)
	- [PDA Eligibility Areas](#pda-eligibility-areas)
	- [Priority Development Areas](#priority-development-areas)
	- [Priority Production Areas](#priority-production-areas)
	- [Priority Conservation Areas](#priority-conservation-areas)
	- [Transit Rich Areas Blueprint Input](#transit-rich-areas-blueprint-input)
	- [High Resource Areas Blueprint Input](#high-resource-areas-blueprint-input)
	- [Final Blueprint Growth Geographies Combined](#final-blueprint-growth-geographies-combined)
		- [Methodology for All Bay Area Local Jurisdictions](#methodology-for-all-bay-area-local-jurisdictions)
		- [Methodology for Bay Area Local Jurisdictions that Nominated Less than 50 Percent of the PDA Eligible Areas as PDAs](#methodology-for-bay-area-local-jurisdictions-that-nominated-less-than-50-percent-of-the-pda-eligible-areas-as-pdas)
- [Results](#results)

## Data Sources

### Priority Development Area Data
- [Priority Development Areas (Plan Bay Area 2040)](https://opendata.mtc.ca.gov/datasets/priority-development-areas-plan-bay-area-2040)

### Priority Production Area Data

### Transit Rich Area Data
- [Major Transit Stops (2017)](https://arcgis.ad.mtc.ca.gov/portal/home/item.html?id=3ba9e3b29aa8457688a389a2ef69f162)
- [Transit Stops - Existing and Planned (2020)(Internal Access Only)](https://arcgis.ad.mtc.ca.gov/portal/home/item.html?id=2c25d8c01ea64a768329673721c42a0b) 

### High Resource Area Data
***California Tax Credit Allocation Committee (TCAC) & the Department of Housing and Community Development (HCD) Resource Opportunity Areas***
- [California Tax Credit Allocation Committee Opportunity Maps Website](https://www.treasurer.ca.gov/ctcac/opportunity.asp)
- [CTCAC/HCD Resource Opportunity Areas (2019) Web Layer (Internal Access Only)](https://arcgis.ad.mtc.ca.gov/portal/home/item.html?id=15c995dc46034e3ea3f44ecd08f19110)

### PDA Eligible Area Data
***MTC Data***
- [Bus Stop Headways During Peak Period in 2019](https://mtc.maps.arcgis.com/home/item.html?id=a47075cd3b864584b65811ad513cb28f)

### PPA Eligible Area Data
***University of California - Berkeley, ABAG, MTC Industrial Land Retention and Investment in the San Francisco Bay Area***
- [PPA Eligible Area Data](https://mtc.maps.arcgis.com/home/item.html?id=66a151ee5e6e453e9c5a19b31198554e)
- [Link to Study](https://mtcdrive.box.com/s/n005i0h3xyu301hdrepqjf8dz8qm73ih)

## Analysis Parameters 

### Regional Growth Framework Update

PDAs, PPAs and PCAs were created following the adopted Plan Bay Area 2050 Growth Framework Update. A summary of key changes to the Regional Growth Framework as well as an overview of current and updated Regional Growth Framework designations can be found at the link below. 

- [2019 Regional Growth Framework Update](https://www.planbayarea.org/sites/default/files/pdfs_referenced/2019_Regional_Growth_Framework_Update_-_Whats_Changed_1.pdf)

### PDA Eligible Area Criteria

| **Designation**                                  | **Criteria**                                                                                                                                                                     |
|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Transit-Rich                                     | Areas within 1/2 mile of:<br>- Passenger rail station<br>- Ferry terminal<br>- Bus service existing with peak headways of 15 minutes or less (included if in Plan Bay Area 2050) |
| Connected Community - High Resource Area         | - No overlap with Transit-Rich Areas<br>- Within state-designated TCAC/HCD High or Highest Resource Area<br>- Within 1/2 mile of bus stop with peak headways of 16-30 minutes   |
| Connected Community - Outside High Resource Area | - No overlap with Transit-Rich Areas<br>- Outside state-designated TCAC/HCD High or Highest Resource Area<br>- Within 1/2 mile of bus stop with peak headways of 16-30 minutes   |

### 

## Methodology

As part of the 2019 Priority Area Call for Letters of Interest, jurisdictions throughout the Bay Area submitted letters of interest for new or modified PDAs, PPAs, and PCAs. Jurisdictions submitted shapefiles, and in some cases, PDFs or image files, with the new or modified areas they had selected for evaluation against the Regional Growth Framework. 

Each shapefile received from jurisdictions was projected from the projection it was in to [EPSG:26910](https://spatialreference.org/ref/epsg/nad83-utm-zone-10n/) and added to an ESRI File Geodatabase. It should be noted that features were spatially modified in some cases based on feedback from jurisdictions. PDAs and PPAs features submitted by jurisdictions with right-of-ways clipped or erased out or jurisdictions that submitted parcel-based areas were modified by MTC/ABAG staff so the full extent of the project area, including right of way areas, were analyized. 

***Note: To run scripts, file paths should be updated and all file geodatabases referenced should be copied locally. Scripts should be run within the ArcGIS Pro Python Analysis Window. The ArcGIS Pro project along with project File Geodatabases can be found in the [project folder on Box](https://mtcdrive.box.com/s/37oi8htx8ljxmdxxrqh4qvl3d035r0j5) under Growth Framework Analysis.***

### PDA Eligibility Areas

PDA Eligibility areas were created following the [PDA Eligible Area Criteria](#pda-eligible-area-criteria). 

**Transit-Rich** 

[Transit Rich Areas Blueprint Input](#transit-rich-areas-blueprint-input)

**Connected Community/High Resource Area Feature**
1. Select bus stops with 16-30 minute headways from [Bus Stop Headways During Peak Period in 2019](#pda-eligible-area-data) layer. 
2. Create 1/2 mile buffer on selected features, with Geodestic (shape preserving) option selected.
3. Clip to [High Resource Areas](#high-resource-areas-blue-print-input)
4. Erase areas overlapping with Transit-Rich Areas.

**Connected Community/Outside High Resource Area Feature**
1. Select bus stops with 16-30 minute headways from [Bus Stop Headways During Peak Period in 2019](#pda-eligible-area-data) layer. 
2. Create 1/2 mile buffer on selected features, with Geodestic (shape preserving) option selected.
3. Erase areas overlapping with [Transit-Rich](#transit-rich-areas-blueprint-input) and Connected Community/High Resource Areas. 

### Priority Development Areas

Priority Development Areas were created by merging new and modified PDAs submitted by jurisdictions along with existing PDAs from Plan Bay Area 2040. The script referenced below provides more granular detail about the steps taken to develop the merged layer.  
- [PDA Merge Script](Scripts/PDA_Merge_Script.py)

Priority Development Area eligibility was determined following the [PDA Eligible Area Criteria](#pda-eligible-area-criteria). Additionally, PDAs met eligibility criteria if their area intersected the PDA Eligible Area by 50% or more. The script referenced below provides more granular detail about the analysis process. 
- [PDA Eligibility Analysis Script](Scripts/PDA_Eligibility_Analysis.py)

### Priority Production Areas

Priority Production Areas were created by merging PPAs submitted by jurisdictions. The script referenced below provides more granular detail about the steps taken to develop the merged layer. 
- [PPA Merge Script](Scripts/PPA_Merge_Script.py)

Priority Production Areas were summarized by [UC Berkeley Industrial Land Study Area](#ppa-eligible-area-data-sources) criteria and a weighted average calculated for PPAs within UC Berkeley Industrial Land Study areas. The Script referenced below provides more granular detail about the steps taken to perform the analysis. 
- [PPA UC Berkeley Industrial Lands Analysis](Scripts/PPA_Analysis.py)

### Transit Rich Areas Blueprint Input

Transit-Rich Areas were created primarily as an input to the [Final Blueprint Growth Geographies Combined](#final-blueprint-growth-geographies-combined) dataset. These data were also used as inputs to create [PDA Eligibility Areas](#pda-eligibility-areas). 

Transit-Rich Areas were created following the methodology listed below:
1. Select passenger rail stations, ferry terminals from [Major Transit Stop](#transit-rich-area-data) layer. Select bus stops on routes with with peak headways of 15 minutes or less during peak period from [Transit Stops - Existing and Planned (2020)](#transit-rich-area-data). These stations/stops were based on posted schedules in January 2020 or service enhancements in Plan Bay Area 2050. (Note that regional passenger rail systems include ACE, BART, CalTrain, SMART, and Capitol Corridor, but only BART and CalTrain include stops meeting the headway standard).
2. Create 1/2 mile buffer on selected features, with Geodesic (shape preserving) and dissolve options selected.
3. Clip to [High Resource Areas](#high-resource-areas-blue-print-input)
4. Erase areas overlapping with Transit-Rich Areas.

### High Resource Areas Blueprint Input
High-Resource Areas reas were created as an input to the [Final Blueprint Growth Geographies Combined](#final-blueprint-growth-geographies-combined) dataset. These data were also used as inputs to create [PDA Eligibility Areas](#pda-eligibility-areas)

High-Resource Areas were created following the methodology listed below:
1. Select High and Highest Resource Areas from [CTCAC/HCD Resource Opportunity Areas (2019)](#high-resource-area-data)
2. Intersect with areas 1/4 from bus stops with peak headways of 30 minutes or less, based upon a January 2020 extract of the Google Transit Feed Specification for all Bay Area transit providers, supplemented by published bus schedules where necessary.

### Final Blueprint Growth Geographies Combined 

The above datasets and inputs were processed and merged together following the detailed methodology below. The applicability of different Growth Geographies varies by local jurisdiction based upon the extent to which a jurisdiction has nominated Priority Development Areas (PDAs), as shown below: 

#### Methodology for All Bay Area Local Jurisdictions

[Priority Development Areas:](#priority-development-areas)
- Processing for growth geographies - features from source data were not modified further. Source data is the same as what is in the growth geographies data.

[Priority Production Areas:](#priority-production-areas)
- Processing for growth geographies - features from source data were not modified further. Source data is the same as what is in the growth geographies data.

[Transit Rich Areas:](#transit-rich-areas-blueprint-input)
- Processing for growth geographies - these input features were temporary data used to determine the designation, and were clipped to the “exclusion areas” shown below as well as Priority Development Areas and Priority Production Areas, so were not modified beyond their production.

#### Methodology for Bay Area Local Jurisdictions that Nominated Less than 50 Percent of the PDA Eligible Areas as PDAs

[Transit-Rich Areas](#transit-rich-areas-blueprint-input) that are not within a PDA, PPA, or within ½ mile of a regional rail station with 15 minute peak headways or less, as identified above. (This category includes both High-Resource Areas and places outside High-Resource Areas)

- Processing for growth geographies - These input features were temporary data used to determine the designation, and were clipped to the “exclusion areas” shown below as well as Priority Development Areas and Priority Production Areas, so were not modified beyond their production.

[High-Resource Areas:](#high-resource-areas-blueprint-input)
- Processing for growth geographies - these input features were temporary data used to determine the designation, and were clipped to all of the Growth Geographies highlighted above (PDAs, PPAs and Transit-Rich Areas), as well as the “exclusion areas” shown below, so were not modified beyond their production.

Exclusion Areas: 
The following areas are excluded from Growth Geographies. Also, these areas were not used in calculating the share of a jurisdiction’s PDA-eligible land locally nominated.
- County-adopted wildland urban interface areas, where available
- Areas of unmitigated sea level rise (i.e., areas at risk from sea level rise through year 2050 that lack mitigation strategies in Plan Bay Area 2050 Environment Element)
- Areas outside locally-adopted urban growth boundaries
- Parkland and other open spaces within urbanized areas identified in the California Protected Areas Database

## Results

[Plan Bay Area 2050 Growth Geographies](https://arcgis.ad.mtc.ca.gov/portal/home/item.html?id=3922afc70d3a4475a98e6ae9973f2bfb#overview)


