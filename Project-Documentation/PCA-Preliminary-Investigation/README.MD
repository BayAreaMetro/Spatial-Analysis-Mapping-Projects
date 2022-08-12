**Draft Status: Finalized Draft KL 08/10/22**

# PCA Preliminary Investigation

This project is the Preliminary Investigation of existing Priority Conservation Areas (PCAs) and preceeds the larger PCA 2.0 Refresh project, which will kick off in Summer 2022. The Preliminary Investigation includes the following: 

1. Evaluates the current PCA polygons and points. 
2. Compares PCAs to other regional geographies, including (i) Officially conserved areas (OCAs), (ii) PBA 2050 Growth Geographies, (iii) 2019 Urban Growth Boundaries, (iv) Equity Priority Communities, and (v) Hazards (sea level rise and wildfire).
3. Evaluates the Greenprint tool and supporting data within the context of PCAs.          

The goal of this project is to arrive at qualitative questions and limited quantitative findings about the size, distribution, and characteristics of the current PCA framework. This preliminary investigation also explores PCA's relationship to potential future overlay layers and examines the PCA relationship to Greenprint to evaluate the feasibility of using the tool in the refresh process.

## Project Management

- [Box Directory](https://mtcdrive.box.com/s/xl9l21jq42esjrnnnzu73vspe0butrrf)
- [ArcGIS Project - Initial Investigation](https://mtcdrive.box.com/s/34yhe91fnk10htcuis1m8i8wxakd9bbu) - This project folder encompasses the ArcGIS project file and geodatabase that map PCAs against OCAs, regional geographies, and hazards.
- [ArcGIS Project - Greenprint Initial Investigation](https://mtcdrive.box.com/s/1so4dlxm8vp7vpsby60jto54ji161va2) - This project folder encompasses the ArcGIS project file and geodatabase that map PCAs against the Greenprint multi-benefit rasters supplied by the Greenprint data team.
- [Asana](https://app.asana.com/0/1200323879598920/1200323879598920)

## Data Sources

The following data was used to evaluate the PCA Polygons and their relationships with other regional geographies:

PCA Layers: 
- [PBA 2050 PCA Points](https://mtc.maps.arcgis.com/home/item.html?id=c750ba059b4340b7a34bb5aa365790db)
- [PCA Polygons - Obtained internally](https://mtcdrive.box.com/s/o2wip98bzlih24549mauskubmeir9zda)

Officially Conserved Areas (OCA) Layers: 
- [California Protected Areas Database (CPAD)](https://www.calands.org/cpad/)
- [California Conservation Easements Database (CCED)](https://www.calands.org/cced/)

Regional Land Use and Planning Geographies:
- [PBA 2050 Growth Geographies](https://mtc.maps.arcgis.com/home/item.html?id=d74d81cfce2a4bc9851858f087b78f49)
- [Urban Growth Boundaries - 2019](https://mtc.maps.arcgis.com/home/item.html?id=cee518ed990947de8d2290416306461f)
- [Equity Priority Communities - Plan Bay Area 2050](https://mtc.maps.arcgis.com/home/item.html?id=1501fe1552414d569ca747e0e23628ff)

Hazard Geographies:
- [CAL FIRE Fire Hazard Severity Zones](https://osfm.fire.ca.gov/divisions/community-wildfire-preparedness-and-mitigation/wildland-hazards-building-codes/fire-hazard-severity-zones-maps/)
- [NOAA Sea Level Rise Projections](https://coast.noaa.gov/slrdata/)

Bay Area Greenprint Data:
- [Greenprint Multi-Benefit Rasters - Obtained by contacting Greenprint team](https://mtcdrive.box.com/s/5f8b0zlrme98jpuizsbn3t7ntcp9qeao) - For more information about these layers, contact Chirag Rabari, Project Manager.
- [Greenprint Fishnet](https://www.bayareagreenprint.org/download/) - The Greenprint fishnet was downloaded but not used for this investigation due to processing constraints. The Greenprint Fishnet is a more detailed and comprehensive dataset than the Multi-Benefit Rasters that were used for this investigation.

## Analysis Parameters

### PCA Points and Polygons
- Distribution of PCAs, designations, and area by county and as a whole.
- How much of current PCA polygons are overlapping?
### Compare PCAs to Regional Geographies
- How much of PCA area overlaps with OCAs? What types of PCAs overlap with OCAs?
- How much of PCA area overlaps with Growth Geographies, Urban Growth Boundaries, and Equity Priority Communities? What types of PCAs overlaps with Growth Geographies, Urban Growth Boundaries, and Equity Priority Communities?
- How much of PCA area overlaps with sea level rise and wildfire hazard areas? What types of PCAs overlap with these hazards?
### Evaluate Greenprint Tool
- How much of the Greenprint rasters overlap with current PCAs? Which values and benefits are best represented by PCAs? Which are not?

## Methodology applied to solve problem

To view a detailed flowchart of the analysis performed to create each layer, see the [Lucid Chart](https://mtcdrive.box.com/s/xl9l21jq42esjrnnnzu73vspe0butrrf](https://lucid.app/lucidchart/e97886a1-3c7b-4d66-a2f9-c497153bcefa/edit?viewport_loc=46%2C182%2C2488%2C1438%2C0_0&invitationId=inv_2c269fd8-0498-4e36-84f4-90e9e7acc1db#) 

The OCA, growth geographies, urban growth boundaries, and hazard layers were unioned or intersected with the PCA polygons to visualize overlapping areas. The unioned or intersected layers were exported to geodatabases and mapped with the original layers to view how PCAs intersect with these layers.
The Greenprint multi-benefit rasters were converted to integer then to polygon and intersected with the PCA polygons to visualize overlapping areas.

#### Union City Analysis
Maps were also created for Union City to support a request from that jurisdiction. No additional analyses were performed for this request. Layers were simply cropped to the Union City jurisdiction boundary.

## Results

The investigation revealed a number of findings that will inform the PCA 2.0 Refresh project. For a summary of findings see the PCA Preliminary Investigation Findings Presentation: https://mtcdrive.box.com/s/ocpu6t4n4k2uqvg5bnkztvdpf6n911de 

To view the maps from Union City Analysis, see the Box Folder: https://mtcdrive.box.com/s/zc58rvncfuqoep7xkbfg2kxm7ks3rkj5
