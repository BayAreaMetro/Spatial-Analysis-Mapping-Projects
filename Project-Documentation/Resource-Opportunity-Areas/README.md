
# CTCAC/HCD Resource Opportunity Areas

Create Resource Opportunity Layer from statewide summary excel workbook published by California Tax Credit Allocation Committee in 2020. 

## Data Sources

[2020 Opportunity Maps](https://www.treasurer.ca.gov/ctcac/opportunity/2020.asp)

## Analysis Parameters

Summary data is provided at tract level for urban areas and block group level for rural areas. 

## Methodology

[Create CTCAC HCD Resource Areas Dataset Notebook](https://nbviewer.org/github/BayAreaMetro/Spatial-Analysis-Mapping-Projects/blob/master/Project-Documentation/Resource-Opportunity-Areas/Create%20CTCAC%20HCD%20Resource%20Areas%20Dataset.ipynb)

1. Pull block-group level data from Census TIGER API
2. Create tract id and block group id from GEOID 
2. Subset tracts (urban areas) and join summary data to urban areas track geography on tract id
3. Dissolve boundaries by block group id
3. Subset block-groups (rural areas), and join summary data to rural areas block group geography on block group id
4. Append track and block group data to create a a single, composite dataset comprised of tracks and block group geographies and data summaries

## Expected Outcomes

## Results

[CTCAC/HCD Resource Opportunity Areas (2020) (BAM Internal Portal)](https://arcgis.ad.mtc.ca.gov/portal/home/item.html?id=a6f295ce96df428f9b99542c089d9039)

## Tags