# Documentation  

The Geography Working Group of CASA is requesting mapping support from MTC to identify areas of concern or “sensitive communities” in the 9-county Bay Area that could be exempted from certain CASA Compact policies.  

### Define the Problem Statement  

How do we methodically capture/visualize/map the most vunerable of the Communities of Concern (COCs) in order to lift them above affordable housing development-related regulations?

Mapping support will entail mapping and conducting spatial analyses of geographically defined data layers based on input from the Geography Working Group until the Group decides on a finalized map.
  
### Project Management 

- [Asana Project](https://app.asana.com/0/inbox/797943099119524/840113458715896/840113458715905) 
- [Box](https://mtcdrive.box.com/s/mqgzpdqlfrofzdzkcmfx25b5pd6wx28p)

### Contents 

- [Data Sources](#data-sources)
- [Analysis Parameters](#analysis-parameters)
- [Methodology](#methodology)
- [Expected Outcomes](#expected-outcomes)
- [Results](#results)

## Data Sources  

[Plan Bay Area 2040](https://www.planbayarea.org/)  
[UCB "CASA Geographies" Mapping Tool](https://cci-displacement.carto.com/viz/d65da6ad-d32e-4500-99ca-f657286804ff/embed_map)  
[Communities of Concern (2018) with American Community Survey Data (2012-2016)](https://mtc.maps.arcgis.com/home/item.html?id=1501fe1552414d569ca747e0e23628ff)    
[Transit Priority Areas (2017)](https://mtc.maps.arcgis.com/home/item.html?id=d97b4f72543a40b2b85d59ac085e01a0)    


## Analysis Parameters  

Create a “slider” tool that identifies census tracts in the 9 county Bay Area based on whether or not they meet changeable thresholds for minority population and poverty (currently set at 30% of the population at 200% of the federal poverty level and 70% minority). The “slider” tool would help identify census tracts based on whether or not they meet different identified thresholds (i.e. 20% at 200% of poverty level and 60% minority).  

Identify census tracts that are within a ¼ mile and ½ mile from established “sensitive census tracts (30% of the population at 200% of federal poverty level and 70% minority).  

Identify the overlap of census tracts that are within a ¼ mile and a ½ mile radius from established sensitive census tracts (not the full census tract, but just the overlap with the radius) and clip all census tracts to urbanized areas.  

## Methodology  

1. Create new AGOL Web map containing the Feature layers [Communities of Concern* (2018) with American Community Survey Data (2012-2016)](https://mtc.maps.arcgis.com/home/item.html?id=1501fe1552414d569ca747e0e23628ff) and [Transit Priority Areas (2017)](https://mtc.maps.arcgis.com/home/item.html?id=d97b4f72543a40b2b85d59ac085e01a0) and save as a web map to be used in a ArcGIS Web AppBuilder.  
2. Create new mapping application with Dashboard theme and organization shared style.  
3. Choose the web map containing the COCs and TPAs.  
4. Add widgets. Main capabilities include: Filter (include create custom filter option), Analysis, and Info summary. Secondary functionality include: Attribute table, Full screen, Header, Home, My location, Scalebar, Address search, Zoom slider, Legend, and Layer list.  

5. Configure Filter capabilities to include 8 expressions:  
    Minorities percentage ask for values  
    Low-income percentage ask for values  
    Limited English Proficiency percentage ask for values  
    Zero-vehicle households percentage ask for values  
    Over 75 percentage ask for values  
    Single-parent family percentage ask for values  
    Severely rent-burdened households percentage ask for values  
    Disability percentage ask for values  
    
*See [MTC Communities of Concern](https://github.com/BayAreaMetro/Spatial-Analysis-Mapping-Projects/tree/master/Project-Documentation/Communities-of-Concern) for more info. [MTC Resolution No. 4217-Equity Framework for Plan Bay Area 2040](https://mtc.legistar.com/LegislationDetail.aspx?ID=2555452&GUID=575A6D3F-B8B8-44CF-9F2D-ABEF8B3C9F06&Options=ID%7CText%7C&Search=%22communities+of+concern%22)  

6. Configure Info summary capabilities to include:  
    Display Panel Settings:  
    Census tracts, Percent minorities, Percent low-income  

*NOTE*: In order to operationalize the original vision to include a dynamic, user-defined buffer based on resulting geographies of user-defined thresholds, geoprocessing packages/services need to be leveraged. ArcGIS Server host geoprocessing tools which can be implemented through AGOL. The procedures for implementing this vision are being evaluated currently only because GIS @ MTC phasing out ArcGIS Server-related hosting. More information regarding this ArcGIS Server capability available upon request

## Expected Outcomes  

Inform the CASA Geography Working Group on Bay Area census tracts that meet criteria identified by the working group for “sensitive communities" to inform the group’s decision on a finalized map.  

## Results  

[Sensitive Communities Threshold Analysis](https://mtc.maps.arcgis.com/apps/webappviewer/index.html?id=ade9682451cd49b0ba988abc38dbecb9)  




