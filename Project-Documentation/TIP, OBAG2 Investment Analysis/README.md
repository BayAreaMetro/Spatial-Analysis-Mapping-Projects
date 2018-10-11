# Documentation
Geospatial procedure and tabular analysis of TIP & OBAG2 INSIDE PDAs/TPAs investments vs. OUTSIDE PDAs/TPAs investments.

### Define the Problem Statement  

Where are the majority of One Bay Area Grant cycle 2 (OBAG2) Funds being invested?
Percentage of OBAG2 funds in PDAs / outside of PDAs (using a distance buffer that we determine, rather than relying on the CMA’s judgment for whether or not a project supported a PDA)  
Where are the majority of Transportation Improvment Program (TIP) Funds being invested?  
Percentage of TIP funds in PDAS (includes OBAG) / outside of PDAs
Funds invested (OBAG and/or TIP) in each PDA (so we can see what PDAs are actually being heavily invested in, vs those that are not).

### Project Management 

- [Asana Project](https://app.asana.com/0/inbox/797943099119524/835368168562377/835368168562378) 
- [Box](https://mtcdrive.box.com/s/89x2ysamyj1u3kd4hettly9ydb8xhk0a)

### Contents 

- [Data Sources](#data-sources)
- [Analysis Parameters](#analysis-parameters)
- [Methodology](#methodology)
- [Expected Outcomes](#expected-outcomes)
- [Results](#results)

## Data Sources
[Transportation Improvement Program (TIP) project point data](https://services3.arcgis.com/i2dkYWmb4wHvYPda/arcgis/rest/services/TIP_2019_PDA_Investment_Analysis_Points_WGS84/FeatureServer)  
[Transportation Improvement Program (TIP) project line data](https://services3.arcgis.com/i2dkYWmb4wHvYPda/arcgis/rest/services/TIP_2019_PDA_Investment_Analysis_Lines_WGS84/FeatureServer)  
[One Bay Area Grant 2 (OBAG2) project point data](https://services3.arcgis.com/i2dkYWmb4wHvYPda/arcgis/rest/services/OBAG_PDA_Investment_Analysis_Points_WGS84/FeatureServer)  
[One Bay Area Grant 2 (OBAG2) project line data](https://services3.arcgis.com/i2dkYWmb4wHvYPda/arcgis/rest/services/OBAG_PDA_Investment_Analysis_Lines_WGS84/FeatureServer)  
[Priority Development Areas (PDA)](https://services3.arcgis.com/i2dkYWmb4wHvYPda/arcgis/rest/services/priority_development_areas_current/FeatureServer)  
[Regional Counties of the Bay Area](https://services3.arcgis.com/i2dkYWmb4wHvYPda/arcgis/rest/services/county_region/FeatureServer)  

## Analysis Parameters
The final deliverable will be a table including summaries of TIP & OBAG projects by PDA and by County. To determine the PDA designation, the project is deemed in/out of a PDAs based solely on if the project touches the PDA (GIS operation intersect/identity). For instance, if a TIP/OBAG project touches more than one PDA (a road corridor project cross multiple PDA geographies) then the project will be associated with as many PDAs as the project 'touches'; thus, the proportionality of the line segment must be considered in order to determine its proportion in the PDA. Careful geometric calculations must be made prior to performing any spatial analyses so the total length/area (area in terms of the 1/2- & 1-mile buffers on the projects) of a project can be split proportionally to determine the PDA's respective grant size amount, TIP amount, and total cost.   

## Methodology
Gather all data layers [see data sources](#data-sources) into GIS  
Project all layers to NAD 83 Zone 10N  
Delete all columns from all data layers expect the following:  

    Transportation Improvement Program (TIP) project point and line data  
        Object ID
        Shape
        TIP ID
        Project Name
        Total Cost
        TIP cost 2019
        Calculate geometry as Length in miles (not point; only lines) and round to 3 significant digits  

    One Bay Area Grant 2 (OBAG2) project point and line data  
        Object ID
        Shape
        TIP ID
        Project Name
        Total Cost
        TIP cost 2019
        Calculate geometry as Length in miles (not point; only lines) and round to 3 significant digits  

    Priority Development Areas (PDA)  
        Object ID
        Shape
        joinkey
        Name
        Calculate geometry as area in sqmi and round to 3 significant digits  

    Regional Counties of the Bay Area  
        Name
        Calculate geometry as area in sqmi and round to 3 significant digits

Select by location the OBAG point projects which intersect the PDAs  
    Flag the resulting projects  
Select by location the OBAG line projects which intersect the PDAs  
    Flag the resulting projects  
Select by location the TIP point projects which intersect the PDAs  
    Flag the resulting projects  
Select by location the TIP line projects which intersect the PDAs  
    Flag the resulting projects  

Identity OBAG project points and lines with Bay Area Counties (relationships unchecked)  
    Delete resulting columns like 'FID%'    
    Calculate geometry (for lines only) as length in miles and round to 3 significant digits  
Identity TIP project points and lines with Bay Area Counties (relationships unchecked)  
    Delete resulting columns like 'FID%'  
    Calculate geometry (for lines only) as length in miles and round to 3 significant digits   
Export to tabular format all resulting identity data layers  
(NOTE: For now, keep TIP & OBAG points and lines datasets separated; should have four individual tables)  
Calculate proportions (resulting identity line shape length (mi)/Total length of line project (mi)) of TIP & OBAG line projects within each county  
Calculate the proportional TIP/OBAG (MAP_grant_size) cost by multiplying the portion by the TIP/OBAG cost  
Confirm same number and order of columns existing in TIP/OBAG point and line tables then marry point and lines to result in only two tables  
Sort the two tables by County then by (In/Out flags)  
Excel-based subtotal function applied to both counties then in/out  
Percent error calculated then refined regional total for original funding amount equivalencies  

## Expected Outcomes

| PDAs only - No Buffer	| OBAG $ 100% within, partially within, or adjacent to a PDA | OBAG $ outside of PDA |	Total |
|-----------------------|------------------------------------------------------------|-----------------------|--------|
| Alameda               |	 	 	                                                 |                       |        |
| Contra Costa	 	 	|	 	 	                                                 |                       |        | 
| Etc.	 	 	        |	 	 	                                                 |                       |        |

| ½ Mile analysis   	| OBAG $ 100% within, partially within, or adjacent to a PDA | OBAG $ outside of PDA |	Total |
|-----------------------|------------------------------------------------------------|-----------------------|--------|
| Alameda               |	 	 	                                                 |                       |        |
| Contra Costa	 	 	|	 	 	                                                 |                       |        | 
| Etc.	 	 	        |	 	 	                                                 |                       |        |

| 1 Mile analysis   	| OBAG $ 100% within, partially within, or adjacent to a PDA | OBAG $ outside of PDA |	Total |
|-----------------------|------------------------------------------------------------|-----------------------|--------|
| Alameda               |	 	 	                                                 |                       |        |
| Contra Costa	 	 	|	 	 	                                                 |                       |        | 
| Etc.	 	 	        |	 	 	                                                 |                       |        |  


### Data Summaries   

## Results
Sample Output:

| PDAs only - No Buffer	| OBAG $ 100% w/in, partially w/in, or adjacent to a PDA | OBAG $ outside of PDA |	Total        |
|-----------------------|--------------------------------------------------------|-----------------------|---------------|
| Alameda               | 1,936,948,516	 	 	                                 | 555,059,850           | 2,492,008,365 |
| Contra Costa	 	 	| 906,955,386	 	 	                                 | 255,451,368           | 1,162,406,753 | 
| Marin	 	 	        | 47,079,418	 	 	                                 | 67,145,927            | 114,225,345   |
| Napa                  | 9,771,649 	 	                                     | 42,723,437            | 52,495,086    |
| San Francisco	 	 	| 1,104,663,376 	 	                                 | 327,447,740           | 1,432,111,116 | 
| San Mateo	 	        | 1,039,493,456	 	                                     | 152,854,199           | 1,192,347,655 |
| Santa Clara           | 3,082,045,726 	 	                                 | 175,705,371           | 3,257,751,096 |
| Solano    	 	 	| 16,227,700 	 	                                     | 120,791,034           | 137,018,734   | 
| Sonoma 	 	        | 115,938,253	 	                                     | 11,700,080            | 127,638,332   |
| Regional total        | 8,259,123,478	 	                                     | 1,708,879,005         | 9,968,002,483 |


### Final Tabular Data Summaries
[Percentage of OBAG2 funds in PDAs / outside of PDAs](https://mtcdrive.box.com/s/jwooy7ay6wqlot79n5d9fm0ew0etm6j2)  
[Percentage of TIP funds in PDAS (includes OBAG) / outside of PDAs](https://mtcdrive.box.com/s/nj110buzt6b85nrtdz66nd2niwgfq9v8)


