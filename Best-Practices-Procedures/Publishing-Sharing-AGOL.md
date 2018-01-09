
<a href="url"><img src="http://gis.mtc.ca.gov/mtcimages/mtcgisLogo.png" align="top" height="64" width="64" ></a>

# Publishing and Sharing Content with ArcGIS Online

## Table of contents

- [Publishing Draft or Intermediate Content to Internal or External Audiences](#publishing-draft-or-intermediate-content-to-internal-or-external-audiences)
  - [Draft Web layers](#draft-web-maps)
  - [Draft Web Maps](#draft-web-maps)
- [Publishing Curated Content to an External Audience](#publishing-curated-content-to-an-external-audience)
  - [Web Layers](#web-layers)
  - [Web Maps](#web-maps)
  - [PDF Maps](#pdf-maps)
- [Publishing Content to MTC's Open Data Portal](opendata/openDataSite.md)

## Publishing Draft or Intermediate Content to Internal or External Audiences

### Draft Web Layers

1. Publish web layer to AGOL through ArcGIS Pro, following guide on [sharing with ArcGIS Pro](AGOL-Technical-Resources.md#publishing-web-layers-to-agol-with-arcgis-pro)
2. Ensure web map meets minimum basic documentation requirements for draft content. See [basic documentation requirements](Documentation.md#basic-documentation) 
    - Name, summary, and tag field are required to be completed before you can publishing to AGOL from ArcGIS Pro.
3. Select sharing options:  
    - To share with **only** a select group of stakeholders, share content to a [working group](Creating-Groups.md#create-working-groups) only. Don't share with **organization** or **public**. If an appropriate working group does not exist, create one following guidelines for [creating working groups](Creating-Groups.md#create-working-groups) 
    - To share with a wider audience, or a stakeholder not part of the MTC AGOL Organization, share content to **organization**, **public**, or both if necessary. 
4. Confirm spatial extent for all web layers prior to publishing. If spatial extent is larger than your target extent (ex California extent when web layer is Bay Area centric), follow guide on [Recalculating Feature Class Extent](AGOL-Technical-Resources.md#recalculate-feature-class-extent) 

### Draft Web Maps 

1. Ensure web map meets minimum basic documentation requirements for draft content. See [basic documentation requirements](Documentation.md#basic-documentation)
2. Select sharing options:  
    - To share with **only** a select group of stakeholders, share content to a [working group](Creating-Groups.md#create-working-groups) only. Don't share with **organization** or **public**. If an appropriate working group does not exist, create one following guidelines for [creating working groups](Creating-Groups.md#create-working-groups) 
    - To share with a wider audience, or a stakeholder not part of the MTC AGOL Organization, share content to **organization**, **public**, or both if necessary. 

## Publishing Curated Content to an External Audience

**Any content that MTC indends to publish to external audiences via ArcGIS Online should be reviewed and shared publicly by the ArcGIS Online content administrator.**    

In the sections following, processes for publishing content to external audiences are documented. These processes are not final, and will likely be updated over time.

### Web Layers

***Steps to follow while publishing from ArcGIS Pro***
1. Coordinate with data owner to ensure layer(s) should be shared with a public audience
2. If layer not already available in AGOL, follow guide on [sharing with ArcGIS Pro](AGOL-Technical-Resources.md#publishing-web-layers-to-agol-with-arcgis-pro)
3. Ensure that content is tagged appropriately. See [tag strategy](https://mtcdrive.app.box.com/file/198480762097)
4. Share with [public group(s)](Creating-Groups.md#create-broadcast-groups) that best suites the content topic area(s). 

   | Content Topic Areas  |               |          |
   |----------------------|---------------|----------|
   | Administrative       | Demographic   | Policy   |
   | Transportation       | Environmental | Projects |
5. Add content to a relevant folder. 
6. Confirm spatial extent for all web layers prior to publishing. If spatial extent is larger than your target extent (ex California extent when web layer is Bay Area centric), follow guide on [Recalculating Feature Class Extent](AGOL-Technical-Resources.md#recalculate-feature-class-extent) 
***Steps to follow using ArcGIS Online once web layer is published***
7. Update ownership of web layer from current owner to content_MTC (if not already owned by that user)
8. Ensure that web layer meets minimum documentation requirements for curated content. See [detailed documentation requirements](Documentation.md##basic-documentation)
9.  Under feature layer settings, ensure that delete protection is enabled and editing is disabled 
10. Mark content status as **Authoratative**

### Web Maps

1. Ensure web layers used in web map have followed the process outlined in the [Web Layers Section](#web-layers)
2. Ensure web map is documented, following the basic documentation requirements. See [basic documentation requirements](Documentation.md#basic-documentation)
    - Detailed documentation not necessary for web maps as layers supporting the web map should be well - documented.
3. Ensure that content is tagged appropriately. See [tag strategy](https://mtcdrive.app.box.com/file/198480762097)
4. Share with [MTC Map Gallery Groups](http://mtc.maps.arcgis.com/home/group.html?id=4bb2944ff35348c3847859b48d28336d#overview)

### PDF Maps

1. Ensure web map is documented, following the basic documentation requirements. See [basic documentation requirements](Documentation.md#basic-documentation)
   - PDFs at minimum should have the following: 
     - Title 
     - Description (write up)
     - Link to project documentation github (if available) 
2. Ensure that content is tagged appropriately. See [tag strategy](https://mtcdrive.app.box.com/file/198480762097)
   - Ensure that month and year are included as seperate tags (ex July, 2017)
3. Share with [MTC Map Gallery Groups](http://mtc.maps.arcgis.com/home/group.html?id=4bb2944ff35348c3847859b48d28336d#overview)

