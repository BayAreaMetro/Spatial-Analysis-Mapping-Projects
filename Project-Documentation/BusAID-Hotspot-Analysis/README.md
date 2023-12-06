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
3. For each hotspot, provide demographic data for all census tracts served by all transit routes passing through the hotspot. 

# Project Resources

| Purpose | Resource | Description | Location | Link (if any) | Access | Notes |
|--------|-----------|-------------|----------|---------------|--------|-------|
| Input | Source Data | Hotspot geospatial data (KMZ points/lines) | Box | [BusAID Hotspot Inventory_v2 (October).kmz ](https://mtcdrive.box.com/s/8sfwj4rcpc1uplg588tp3hxznc83j9m1) | Internal Only  | |
| Input | Source Data | Hotspot tabluar data (Excel spreadsheet) | Box | [BusAID Hotspot Master List_112823.xlsx](https://mtcdrive.box.com/s/tyl4c2yinhtgp42kzfdqohcg5kzy1kwh) | Internal Only | |
| Input | Source Data | Individual operator hotspot data (Excel spreadsheets) | Box | [Individual Operator Spreadsheets](https://mtcdrive.box.com/s/a60zuajafmaisllxhi7unwbbnlh48qql) | Internal Only | |
| Data Catalog | Published Datasets | ArcGIS Online working roup for managing working and draft content | ArcGIS Online | [Bus AID (Private - Working)](https://mtc.maps.arcgis.com/home/group.html?id=0ebbbd31731f41558becf30d5a210752#overview) | Project Collaborators | |

# Methodology