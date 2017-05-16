# Small UZA/Rural Area Section 5310 Project Mapping 

### Problem Statement

Summarize small UZA/Rural Area Section 5310 project by county. 

### Data Sources

- [FY15, FY16, FY17 Small UZA/Rural Area Section 5310 Projects](https://github.com/MetropolitanTransportationCommission/Adhoc-Spatial-Analysis/blob/master/Small-UZA-Rural-Area-Section-5310-Projects/data/CTC_Draft_List_Small_UR_Projects.csv)
- [California Counties (TomTom m8)](https://mtcdrive.box.com/s/yoboeonzjvrzkqo3jb1z50ooibkbh2km)

### Methodology

Summarize project by county, generating view containing Project County, Project Total, and County Centroid:

- [Summarize_Funding_by_County.sql](https://github.com/MetropolitanTransportationCommission/Adhoc-Spatial-Analysis/blob/master/Small-UZA-Rural-Area-Section-5310-Projects/scripts/Summarize_Funding_by_County.sql)

Issues: 

- California County abbreviations don't match Caltrains abbreviations - [County Abbreviation Lookup Table](https://github.com/MetropolitanTransportationCommission/Adhoc-Spatial-Analysis/blob/master/Small-UZA-Rural-Area-Section-5310-Projects/data/County_Abbrev_Lookup.csv) was created to create intermediary join table between California County Polygons and [FY15, FY16, FY17 Small UZA/Rural Area Section 5310 Projects](https://github.com/MetropolitanTransportationCommission/Adhoc-Spatial-Analysis/blob/master/Small-UZA-Rural-Area-Section-5310-Projects/data/CTC_Draft_List_Small_UR_Projects.csv) 

### Outcome 
