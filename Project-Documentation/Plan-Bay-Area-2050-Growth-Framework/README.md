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
- [Expected Outcomes](#expected-outcomes)
- [Results](#results)

## Data Sources

### Priority Development Area Data

- [Priority Development Areas (current)](http://opendata.mtc.ca.gov/datasets/priority-development-areas-current)

### Priority Production Area Data

### PDA Eligible Area Data Sources
***MTC Data***
- [Major Transit Stops](https://mtc.maps.arcgis.com/home/item.html?id=561dc5b42fa9451b95faf615a3054260)
- [Bus Stop Headways During Peak Period in 2019](https://mtc.maps.arcgis.com/home/item.html?id=a47075cd3b864584b65811ad513cb28f)

***California Tax Credit Allocation Committee (TCAC) & the Department of Housing and Community Development (HCD) Resource Opportunity Areas***
- [California Tax Credit Allocation Committee Opportunity Maps Website](https://www.treasurer.ca.gov/ctcac/opportunity.asp)
- [CTCAC/HCD Resource Opportunity Areas (2019) Web Layer](https://mtc.maps.arcgis.com/home/item.html?id=cfe23ff6e81d483f90c65fb0eba7db2e#overview)

### PPA Eligible Area Data Sources
***University of California - Berkeley, ABAG, MTC Industrial Land Retention and Investment in the San Francisco Bay Area***
- [PPA Eligible Area Data](https://mtc.maps.arcgis.com/home/item.html?id=66a151ee5e6e453e9c5a19b31198554e)
- [Link to Study](https://mtcdrive.box.com/s/n005i0h3xyu301hdrepqjf8dz8qm73ih)

## Analysis Parameters 

### Regional Growth Framework Update

PDAs, PPAs and PCAs were created following the adopted Plan Bay Area 2050 Growth Framework Update. A summary of key changes to the Regional Growth Framework as well as an overview of current and updated Regional Growth Framework designations can be found at the link below. 

- [2019 Regional Growth Framework Update](https://www.planbayarea.org/sites/default/files/pdfs_referenced/2019_Regional_Growth_Framework_Update_-_Whats_Changed.pdf)

### PDA Eligible Area Criteria

| **Designation**                                  | **Criteria**                                                                                                                                                                     |
|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Transit-Rich                                     | Areas within 1/2 mile of:<br>- Passenger rail station<br>- Ferry terminal<br>- Bus service existing with peak headways of 15 minutes or less (included if in Plan Bay Area 2040) |
| Connected Community - High Resource Area         | - No overlap with Transit-Rich Areas<br>- Within state-designated TCAC/HCD High or Highest Resource Area<br>- Within 1/2 mile of bus stop with speak headways of 16-30 minutes   |
| Connected Community - Outside High Resource Area | - No overlap with Transit-Rich Areas<br>- Outside state-designated TCAC/HCD High or Highest Resource Area<br>- Within 1/2 mile of bus stop with peak headways of 16-30 minutes   |

## Methodology

As part of the 2019 Priority Area Call for Letters of Interest, jurisdictions throughout the Bay Area submitted letters of interest for new or modified PDAs, PPAs, and PCAs. Jurisdictions submitted shapefiles, and in some cases, PDFs or image files, with the new or modified areas they had selected for evaluation against the Regional Growth Framework. 

Each shapefile received from jurisdictions was projected from the projection it was in to [EPSG:26910](https://spatialreference.org/ref/epsg/nad83-utm-zone-10n/) and added to an ESRI File Geodatabase. It should be noted that features were spatially modified in some cases based on feedback from jurisdictions. PDAs and PPAs features submitted by jurisdictions with right-of-ways clipped or erased out or jurisdictions that submitted parcel-based areas were modified by MTC/ABAG staff so the full extent of the project area, including right of way areas, were analyized. 

***Note: To run scripts, file paths should be updated and all file geodatabases referenced should be copied locally. Scripts should be run within the ArcGIS Pro Python Analysis Window. The ArcGIS Pro project along with project File Geodatabases can be found in the [project folder on Box](https://mtcdrive.box.com/s/37oi8htx8ljxmdxxrqh4qvl3d035r0j5) under Growth Framework Analysis.***

### PDA Eligibility Areas

PDA Eligibility areas were created following the [PDA Eligible Area Criteria](#pda-eligible-area-criteria).

**Transit-Rich**
1. Select passenger rail stations, ferry terminals, and bus stops on routes with with peak headways of 15 minutes or less during peak period from [Major Transit Stop](#pda-eligible-area-data-sources) layer. 
2. Create 1/2 mile buffer on selected features, with Geodesic (shape preserving) and dissolve options selected. 

**Connected Community/High Resource Area Feature**
1. Select bus stops with 16-30 minute headways from [Bus Stop Headways During Peak Period in 2019](#pda-eligible-area-data-sources) layer. 
2. Create 1/2 mile buffer on selected features, with Geodestic (shape preserving) option selected.
3. Clip to [CTCAC/HCD Resource Opportunity Areas](#pda-eligible-area-data-sources)
4. Erase areas overlapping with Transit-Rich Areas.

**Connected Community/Outside High Resource Area Feature**
1. Select bus stops with 16-30 minute headways from [Bus Stop Headways During Peak Period in 2019](#pda-eligible-area-data-sources) layer. 
2. Create 1/2 mile buffer on selected features, with Geodestic (shape preserving) option selected.
3. Erase areas overlapping with Transit-Rich and Connected Community/High Resource Areas. 

### Priority Development Areas

Priority Development Areas were created by merging new and modified PDAs submitted by jurisdictions along with existing PDAs from Plan Bay Area 2050.  
- [PDA Merge Script](Scripts/PDA_Merge_Script.py)
- [PDA Eligibility Analysis Script](Scripts/PDA_Eligibility_Analysis.py)

### Priority Production Areas

- [PPA Merge Script](Scripts/PPA_Merge_Script.py)
- [PPA UC Berkeley Industrial Lands Analysis](Scripts/PPA_Analysis.py)

### Priority Conservation Areas

## Expected Outcomes

## Results
