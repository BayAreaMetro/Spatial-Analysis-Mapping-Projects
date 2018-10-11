# Documentation  

[MTC Vital Signs](http://www.vitalsigns.mtc.ca.gov/) leverages TOMTOM and INRIX data to measure [Vehicle Hours of Delay](http://www.vitalsigns.mtc.ca.gov/time-spent-congestion) for the most congested segments in the 9-county Bay Area region. Our issues faced included many overlapping TMC segments and opposite directional vertices for polylines representing the congested segments. 

## Define the Problem Statement  
Below are two screenshots, one with the line and no offset, and one with the line with the offset applied. They show the line breaking into two directions when the offset is applied. It shows that while the line feature draws as a single line when no offset is applied, the line breaks into multiple segments when the offset is applied, as we were seeing in the [interactive map](https://mtc.carto.com/tables/t7_merge_17/public/map). We think this is attributed to a "To-From"/"From-To" problem. The vertices which make up a polyline draw from start to finish based on the direction of the roadway. ie For a northbound roadway, the first point/vertex in the polyline should be the southernmost, inversely the last vertex should be the northernmost thus the vertices are placed in a sequential order according to the direction of the roadway. This is not the case for this [Congested Segments* GEOJSON](https://mtcdrive.box.com/s/bwurv8cxu740szbbhs0cmj0y0y6s42np) dataset.  

### Project Management  

- [Task on Asana](https://app.asana.com/0/inbox/797943099119524/856267709523291/856267709523292)  
- [Data on Box](https://mtcdrive.box.com/s/2ehfea5lx485m3h2imdltfc9tfdg5qyn)  

## Data Sources  

[MTC Carto tool](https://mtc.carto.com/tables/t7_merge_17/public/map)    
[Congested Segments* GEOJSON](https://mtcdrive.box.com/s/bwurv8cxu740szbbhs0cmj0y0y6s42np)  
[*Based on previous request "Congested Segments 2017"](https://github.com/BayAreaMetro/Data-Analysis-Projects/tree/master/congested_segments/2017)  
[Screenshot 1](https://mtcdrive.box.com/s/hil3u7yis1kdu4aek3xpgxdu071kw0ze)  
[Screenshot 2](https://mtcdrive.box.com/s/defei7gzzej9l5rorkzj70uucxd0l16j)  

## Analysis Parameters  

Only one record per project  
Directionality must be correctly reflected in polyline vertices sequence (bc a CSS offset property is used in CARTO for Vital Signs reporting)

## Methodology applied to solve problem

## Expected Outcomes

## Results

