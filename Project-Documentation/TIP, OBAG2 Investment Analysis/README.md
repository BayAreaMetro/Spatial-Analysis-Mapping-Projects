# Draft Documentation
Geospatial procedure and tabular analysis of OBAG and TIP investments in PDAs/TPAs vs. investments outside of those areas.

% OBAG 2 funds in PDAs / outside of PDAs (using a distance buffer that we determine, rather than relying on the CMA’s judgment for whether or not a project supported a PDA)
% TIP funds in PDAS (includes OBAG) / outside of PDAs
$ invested (OBAG and/or TIP) in each PDA (so we can see what PDAs are actually being heavily invested in, vs those that are not).

For example:  

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


Identity TIP project points, lines, polgons in PDAs  
Calculate proportion of TIP projects within each PDA  
Identity resulting TIP/PDA identity in Bay Area counties  
Calculate proportion of TIP projects within each county  


## Expected Outcomes

### Maps  

### Data Summaries   

## Results

### Final Tabular Data Summaries

### Intermediate Data 

### Final Data 


### Maps 

