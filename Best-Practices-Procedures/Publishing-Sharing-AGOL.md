
<a href="url"><img src="http://gis.mtc.ca.gov/mtcimages/mtcgisLogo.png" align="top" height="64" width="64" ></a>

# Publishing and Sharing Content with ArcGIS Online

## Table of contents
- [Creating Groups](#creating-groups)
    - [Create Working Groups](#create-working-groups)
    - [Create Broadcast Groups](#create-broadcast-groups)
- [Publishing Draft or Intermediate Content to Internal or External Audiences](#publishing-draft-or-intermediate-content-to-internal-or-external-audiences)
- [Publishing Curated Content to an External Audience](#publishing-curated-content-to-an-external-audience)
- [Publishing Content to MTC's Open Data Portal](#publishing-content-to-mtcs-open-data-portal)

## Creating Groups 

Groups allow AGOL users to manage a collection of maps, scenes, layers, analytics, and apps. Groups can be created by theme, or topic, or project. When creating groups, the purpose and audience of the group is worth considering. At MTC, our audience(s) can generally be categorized into two groups – [working groups](#create-working-groups), and [broadcast groups](#create-broadcast-groups).

### Create Working Groups

Working Group – for sharing in-progress work with a specific group of collaborators (your work colleagues). These groups will be ad-hoc groups which will have owners other than the GIS Team or content curator. Audience for these groups will be limited to members of the group.

### Create Broadcast Groups 

**Broadcast groups are created and managed only by the DataViz team's content curator**

Broadcast Group – for sharing finished content with an identified audience (everyone, your organization, or a specific collection of individuals) Broadcast groups will be organized bythe following topic areas: 

   | Content Topic Areas  |               |          |
   |----------------------|---------------|----------|
   | Transportation       | Demographic   | Policy   |
   | Transportation       | Environmental | Projects |

**transfer content from strategy doc***
 

## Publishing Draft or Intermediate Content to Internal or External Audiences

### Web Layers

1. Publish web layer to AGOL through ArcGIS Pro, following guide on [sharing with ArcGIS Pro](AGOL-Technical-Resources.md#publishing-web-layers-to-agol-with-arcgis-pro)
2. Ensure web map meets minimum basic documentation requirements for draft content. See [basic documentation requirements](Documentation.md#basic-documentation) 
    - Name, summary, and tag field are required to be completed before you can publishing to AGOL from ArcGIS Pro.
3. Select sharing options:  
    - To share with **only** a select group of stakeholders, share content to a **working group only**. Don't share with **organization** or **public**. If an appropriate working group does not exist, create one following guidelines for [creating working groups](#create-working-group) 
    - To share with a wider audience, or a stakeholder not part of the MTC AGOL Organization, share content to **organization**, **public**, or both if necessary. 
4. Confirm spatial extent for all web layers prior to publishing. If spatial extent is larger than your target extent (ex California extent when web layer is Bay Area centric), follow guide on [Recalculating Feature Class Extent](AGOL-Technical-Resources.md#recalculate-feature-class-extent) 

### Web Maps 

1. Ensure web map meets minimum basic documentation requirements for draft content. See [basic documentation requirements](Documentation.md#basic-documentation)
2. Select sharing options:  
    - To share with **only** a select group of stakeholders, share content to a **working group only**. Don't share with **organization** or **public**. If an appropriate working group does not exist, create one following guidelines for [creating working groups](#create-working-group) 
    - To share with a wider audience, or a stakeholder not part of the MTC AGOL Organization, share content to **organization**, **public**, or both if necessary. 

## Publishing Curated Content to an External Audience

**Any content that MTC indends to publish to external audiences via ArcGIS Online should be reviewed and shared publicly by the ArcGIS Online content administrator.**    

In the sections following, processes for publishing content to external audiences are documented. These processes are not final, and will likely be updated over time.

### Web Layers

1. Coordinate with data owner to ensure layer(s) should be shared with a public audience
2. If layer not already available in AGOL, follow guide on [sharing with ArcGIS Pro](AGOL-Technical-Resources.md#publishing-web-layers-to-agol-with-arcgis-pro)
3. Update ownership of web layer from current owner to content_MTC (if not already owned by that user)
4. Ensure that web layer meets minimum documentation requirements for curated content. See [detailed documentation requirements](Documentation.md#detailed-documentation)
5. Ensure that content is tagged appropriately. See [tag strategy](https://mtcdrive.app.box.com/file/198480762097)
6. Share with public group(s) that best suites the content topic area(s). 

   | Content Topic Areas  |               |          |
   |----------------------|---------------|----------|
   | Transportation       | Demographic   | Policy   |
   | Transportation       | Environmental | Projects |
7. Confirm spatial extent for all web layers prior to publishing. If spatial extent is larger than your target extent (ex California extent when web layer is Bay Area centric), follow guide on [Recalculating Feature Class Extent](AGOL-Technical-Resources.md#recalculate-feature-class-extent) 

### Web Maps

1. Ensure web layers used in web map have followed the process outlined in the [Web Layers Section](#web-layers)
2. Ensure web map is documented, following the basic documentation requirements. See [basic documentation requirements](Documentation.md#basic-documentation)
    - Detailed documentation not necessary for web maps as layers supporting the web map should be well - documented.
3. Ensure that content is tagged appropriately. See [tag strategy](https://mtcdrive.app.box.com/file/198480762097)
4. Share with [MTC Map Gallery Groups](http://mtc.maps.arcgis.com/home/group.html?id=4bb2944ff35348c3847859b48d28336d#overview)

### PDF Maps

1. Ensure web map is documented, following the basic documentation requirements. See [basic documentation requirements](Documentation.md#basic-documentation)
2. Ensure that content is tagged appropriately. See [tag strategy](https://mtcdrive.app.box.com/file/198480762097)
3. Share with [MTC Map Gallery Groups](http://mtc.maps.arcgis.com/home/group.html?id=4bb2944ff35348c3847859b48d28336d#overview)

## Publishing Content to MTC's Open Data Portal 

1. Ensure content meets minimum requirements for [publishing curated content to an external audience](#publishing-curated-content-to-an-external-audience-with-arcgis-online)
2. If publishing a web layer, ensure coordinate reference system is set to WGS84 (EPSG/SRID: 4326) 
3. Tag with appropriate open data category tag - **Note: if content not tagged, content will not be organized by category on open data site**

   | Open Data Categories |               |          |
   |----------------------|---------------|----------|
   | Transportation       | Demographic   | Policy   |
   | Transportation       | Environmental | Projects |

4. Share with Open Data Group (Any content shared with this group will be made available on MTC's Open Data Portal). See [MTC Open Data Layer Library](http://mtc.maps.arcgis.com/home/group.html?id=354e5d5c541c46a985891de9bfaa9703#overview) to see content already shared within the group.
