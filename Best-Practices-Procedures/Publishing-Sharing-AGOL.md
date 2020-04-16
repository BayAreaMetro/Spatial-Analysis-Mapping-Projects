
<a href="url"><img src="http://gis.mtc.ca.gov/mtcimages/mtcgisLogo.png" align="top" height="64" width="64" ></a>

# Publishing and Sharing Content to ArcGIS Online for All Users

## Table of contents
- [Publishing Content to ArcGIS Online](#publishing-content-to-arcgis-online)
    - [Web Layers](#draft-web-maps)
    - [Web Maps](#draft-web-maps)

## Publishing Content to ArcGIS Online

### Web Layers

1. Publish web layer to AGOL through ArcGIS Pro, following guide on [sharing with ArcGIS Pro](AGOL-Technical-Resources.md#publishing-web-layers-to-agol-with-arcgis-pro)
2. Ensure web layer meets minimum basic documentation requirements for draft content. See [basic documentation requirements](Documentation.md#basic-documentation) 
    - Name, summary, and tag field are required to be completed before you can publish to AGOL from ArcGIS Pro.
3. Select sharing options:  
    - To share with **only** a select group of stakeholders, share content to a [working group](Creating-Groups.md#create-working-groups) only. Do not share with **organization** or **public**. If an appropriate working group does not exist, create one following guidelines for [creating working groups](Creating-Groups.md#create-working-groups) 
    - To share with a wider audience, or a stakeholder not part of the MTC AGOL Organization, share content to **organization**, **public**, or both if necessary. 
4. Confirm spatial extent for all web layers prior to publishing. If spatial extent is larger than your target extent (ex California extent when web layer is Bay Area centric), follow guide on [Recalculating Feature Class Extent](AGOL-Technical-Resources.md#recalculate-feature-class-extent). For ArcGIS Pro layers formed using 'Make Layer From Selected Features' function, first export data to a temporary shapefile or file geodatabase feature class or resulting ArcGIS Online web layer will contain extent of source data, not the extent of the selected subset of features.

### Web Maps 

1. Ensure web map meets minimum basic documentation requirements for draft content. See [basic documentation requirements](Documentation.md#basic-documentation)
2. Select sharing options:  
    - To share with **only** a select group of stakeholders, share content to a [working group](Creating-Groups.md#create-working-groups) only. Do not share with **organization** or **public**. If an appropriate working group does not exist, create one following guidelines for [creating working groups](Creating-Groups.md#create-working-groups) 
    - To share with a wider audience, or a stakeholder not part of the MTC AGOL Organization, share content to **organization**, **public**, or both if necessary. 
