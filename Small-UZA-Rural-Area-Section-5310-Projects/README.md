# Small UZA/Rural Area Section 5310 Project Mapping 

### Problem Statement

Summarize small UZA/Rural Area Section 5310 project by county. 

### Data Sources

- [FY15, FY16, FY17 Small UZA/Rural Area Section 5310 Projects](https://github.com/MetropolitanTransportationCommission/Adhoc-Spatial-Analysis/blob/master/Small-UZA-Rural-Area-Section-5310-Projects/data/CTC_Draft_List_Small_UR_Projects.csv)
- [California Counties (TomTom m8)](https://mtcdrive.box.com/s/yoboeonzjvrzkqo3jb1z50ooibkbh2km)
- [County Abbreviation Lookup Table](https://github.com/MetropolitanTransportationCommission/Adhoc-Spatial-Analysis/blob/master/Small-UZA-Rural-Area-Section-5310-Projects/data/County_Abbrev_Lookup.csv)

### Methodology

Summarized project by county, generating view containing Project County, Project Total, and County Centroid:

- [Summarize_Funding_by_County.sql](https://github.com/MetropolitanTransportationCommission/Adhoc-Spatial-Analysis/blob/master/Small-UZA-Rural-Area-Section-5310-Projects/scripts/Summarize_Funding_by_County.sql)
	- Script generates point feature class view through a right join with a sub query, which maintains relationship only with counties where there are proposed investments  
	- Sub query joins [FY15, FY16, FY17 Small UZA/Rural Area Section 5310 Projects](https://github.com/MetropolitanTransportationCommission/Adhoc-Spatial-Analysis/blob/master/Small-UZA-Rural-Area-Section-5310-Projects/data/CTC_Draft_List_Small_UR_Projects.csv) to [County Abbreviation Lookup Table](https://github.com/MetropolitanTransportationCommission/Adhoc-Spatial-Analysis/blob/master/Small-UZA-Rural-Area-Section-5310-Projects/data/County_Abbrev_Lookup.csv) on County Abbreviations (string based join), grouping by County


Issues: 

California County abbreviations don't match Caltrains abbreviations - [County Abbreviation Lookup Table](https://github.com/MetropolitanTransportationCommission/Adhoc-Spatial-Analysis/blob/master/Small-UZA-Rural-Area-Section-5310-Projects/data/County_Abbrev_Lookup.csv) was created to create intermediary join table between California County Polygons and [FY15, FY16, FY17 Small UZA/Rural Area Section 5310 Projects](https://github.com/MetropolitanTransportationCommission/Adhoc-Spatial-Analysis/blob/master/Small-UZA-Rural-Area-Section-5310-Projects/data/CTC_Draft_List_Small_UR_Projects.csv) 

### Outcome 

Project collateral 

- [Project Maps(PDF, PNG)](https://mtcdrive.box.com/s/rl16u2xtqsrrgux4zooetnemuqv1ynf9)
- [Project Illustrator & InDesign Files](https://mtcdrive.box.com/s/a5457yumclbjumv8zd572mo0o1chio4e)
- [Summary of Proposed Project Investments By County (csv)](https://github.com/MetropolitanTransportationCommission/Adhoc-Spatial-Analysis/blob/master/Small-UZA-Rural-Area-Section-5310-Projects/data/Small_UR_Proj_County_Summary.csv)
