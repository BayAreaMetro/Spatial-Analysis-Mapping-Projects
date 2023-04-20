# Language Access Plan Limited-English Proficiency Analysis

Develop maps in support of the Air District's Language Access Plan that highlight Limited-English Proficient populations through the Bay Area region. 

### Project Resources 

Add links to:
- [Asana](https://app.asana.com/0/304776046055605/1204416902830069/f)
- [Box](https://mtcdrive.box.com/s/07l3ww2yvlwgyugugrkv59p8uqbrm63x)

## Analysis Parameters

1. Map 1: The Air District would like to develop a GIS map similar to the map developed in MTC’s 2019 Plan for Providing Special Language Services to LEP Populations that utilizes most recently available census data (see page 14: https://mtc.ca.gov/sites/default/files/MTC_2019_Plan_for_Providing_Special_Language_Services_to_LEP_Population_-_Final.pdf). 
2. Maps 2-6: In addition, like in MTC’s report, the Air District would like to develop maps like that of A-1 through A-6 in the appendix, utilizing most recently available census data (see Appendix A in the MTC report linked above).

## Methodology

- Notebook: [Pull LEP Data (Github)](pull_lep_data_acs.ipynb)
- ArcGIS Pro Project: [Zip File (Box)](https://mtcdrive.box.com/s/6simjjunzpceeh5osibm179x8lie5yo6)

Input:
> - Source: `U.S. Census Bureau, American Community Survey`
> - Product: `2021: ACS 5-Year Estimates Detailed Tables`
> - Sourced From: `API`
> - Table Name: `LANGUAGE SPOKEN AT HOME FOR THE POPULATION 5 YEARS AND OVER`
> - Table ID: `C16001`
> - Census Geography: `Tract`
> - Universe: `Population 5 years and over`
> 
Output: 
> - [Data (Box)](https://mtcdrive.box.com/s/t18hixjmevjpncfs3fqspdxpfg8pmun8)
> - [PDF Maps (Box)](https://mtcdrive.box.com/s/7znbkr7ivrt8mcjfrfv0flxq82t7u7as)



