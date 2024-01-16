# Bus AID Hotspot Analysis <!-- omit in toc -->

Documentation Status: **DRAFT**

- [Purpose](#purpose)
- [Description](#description)
- [Parameters](#parameters)
- [Project Resources](#project-resources)
- [Methodology](#methodology)

# Purpose
The purpose of this repository is to document the geospatial analyses being conducted as part of the Bus Accelerated Infrastructure Delivery (BusAID) program.  

# Description
BusAID geospatial analyses are being carried out collaboratively between the DataViz and Regional Network Management (RNM) teams. The RNM team, leading the BusAID program, is working to inventory transit operator-identified "hotspot" locations throughout the Bay Area with transit speed and reliability issues, score these hotspot locations, and fund quick-build projects at the highest scoring locations. To score projects, the team is using criteria related to transit ridership, potential delay reduction, equity considerations, and presence of Priority Development Areas (PDAs). 

The goal of this project is to develop an automated, repeatable geospatial analysis process related to the equity and PDA criteria mentioned above. 

# Parameters

1. For each hotspot, provide the number of Equity Priority Area (EPC) census tracts served by all transit routes passing through the hotspot as a share of total census tracts served by all transit routes passing through the hotspot. Break out EPC census tracts served into “high”, “higher”, and “highest” EPC classifications. 
2. For each hotspot, provide the number of transit routes that serve PDA(s) as a share of total transit routes passing through the hotspot.
3. For each hotspot, summarize the following [Equity Priority Community (EPC)](https://github.com/BayAreaMetro/Spatial-Analysis-Mapping-Projects/tree/master/Project-Documentation/Equity-Priority-Communities#summary-of-mtc-epc-demographic-factors--demographic-factor-definitions) population demographic factors for all census tracts served by transit routes passing through hotspots:
   1. People of Color
   2. Low Income (< 200% Federal Poverty Level -FPL)
   3. Limited English Proficiency
   4. Zero-Vehicle Household
   5. Seniors 75 Years and Over
   6. People with Disability	
   7. Single Parent Families	
   8. Rent-Burdened
   
   Additionally, summarize the following:
   1. Total population
   2. Total population over 5 years old
   3. Total households
   4. Total families

Remove the following hotspots from the analysis:
- Remove hotspots #108, 109, 110 (WestCAT-identified hotspots) and any routes that only pass through these hotspots. These are being addressed via a DPD Forwards project.
- Remove hotspots #82, 84, 85 (SFMTA-identified hotspots) and any routes that only pass through these hotspots. SFMTA has decided to withdraw these from consideration for the BusAID program.

# Project Resources

| Purpose | Resource | Description | Location | Link (if any) | Access | Notes |
|--------|-----------|-------------|----------|---------------|--------|-------|
| Input | Source Data | Hotspot geospatial data (KMZ points/lines) | Box | [Spatial Data](https://mtcdrive.box.com/s/sg1xnjo4vo9m6khs9cmum70r6yhndgbh) | Internal Only  | |
| Input | Source Data | Hotspot tabular data (Excel spreadsheet) | Box | [BusAID Hotspot Master List_112823.xlsx](https://mtcdrive.box.com/s/tyl4c2yinhtgp42kzfdqohcg5kzy1kwh) | Internal Only | |
| Input | Source Data | Individual operator hotspot data (Excel spreadsheets) | Box | [Individual Operator Spreadsheets](https://mtcdrive.box.com/s/a60zuajafmaisllxhi7unwbbnlh48qql) | Internal Only | |
| Input | Source Data | Equity Priority Communities - Plan Bay Area 2050 (EPCs) | ArcGIS Online | [EPCs](https://mtc.maps.arcgis.com/home/item.html?id=28a03a46fe9c4df0a29746d6f8c633c8) | Public | |
| Input | Source Data | Priority Development Areas - Plan Bay Area 2050 (PDAs) | ArcGIS Online | [PDAs](https://mtc.maps.arcgis.com/home/item.html?id=4df9cb38d77346a289252ced4ffa0ca0) | Public | |
| Input | Source Data | 511 GTFS Data - November 2023 | Online | [511 GTFS Data](https://511.org/open-data/transit) | Public | Data pulled from the historic feed for November 2023 |
| Data Catalog | Published Datasets | ArcGIS Online working roup for managing working and draft content | ArcGIS Online | [Bus AID (Private - Working)](https://mtc.maps.arcgis.com/home/group.html?id=0ebbbd31731f41558becf30d5a210752#overview) | Project Collaborators | |
| Output | Data Products | BusAID Hotspots Summary Data | Box | [BusAID Hotspot Master List_112823.xlsx](https://mtcdrive.box.com/s/tyl4c2yinhtgp42kzfdqohcg5kzy1kwh) | Internal Only | Data summaries were added to the tabular excel workbook as the following tabs: hotspot_epc_summary; hotspot_pda_summary; hotspot_demographic_summary |

# Methodology

[Build Busaid Datasets (Jupyter Notebook)]("build_busaid_datasets.ipynb")

   1. Read input datasets
   2. Pre-process hotspot datasets
      1. Drop hotspot records with missing ids from hotspot master list
      2. Remove hotspots no longer under consideration
      3. Create point and line datasets from KML data
      4. Extract hotspot ids from hotspot name column to prepare for join of spatial and tabular data
      5. Merge master list tabular data to spatial data (points and lines)
      6. Remove whitespace from transit routes column in master list
      7. Split comma separated values into a list of transit routes for each hotspot in master list
      8. Add transit agency ids that match GTFS data in master list
      9. Explode transit routes into individual rows (one row per transit route) in master list
      10. Manually correct transit route ids that do not match GTFS data in master list
   4. Pre-process GTFS transit datasets 
      1. Check that all agencies represented in the hotspot master list are included in the GTFS data
      2. Join GTFS agency, route, trip, and shape data into a single dataset
      3. Filter to only include bus and Tram, Streetcar, Light Rail transit modes      
   5. Merge hotspot tabular data with spatial data
  1.  Publish datasets to ArcGIS Online for review
   2. Perform spatial overlays
      1. Overlay hotspots with EPCs
      2. Overlay hotspots with PDAs
   3. Summarize data
      1. Summarize tracts by hotspot, epc classification
      2. Summarize routes by hotspot, pda
      3. Summarize demographic data by hotspot