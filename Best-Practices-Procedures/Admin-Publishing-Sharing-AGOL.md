<a href="url"><img src="http://gis.mtc.ca.gov/mtcimages/mtcgisLogo.png" align="top" height="64" width="64" ></a>

# Best Practices for ArcGIS Online Administrators

## Table of contents
- [Publishing Curated Content to an External Audience](#publishing-curated-content-to-an-external-audience)
   - [Web Layers](#web-layers)
   - [Web Maps](#web-maps)
   - [PDF Maps](#pdf-maps)
- [Publishing Content to MTC's Open Data Portal](opendata/openDataSite.md)

## Publishing Curated Content to an External Audience

**Any content that MTC indends to publish to external audiences via ArcGIS Online should be reviewed and shared publicly by the ArcGIS Online content administrators, not individual users.**    

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
6. Confirm spatial extent for all web layers prior to publishing. If spatial extent is larger than your target extent (ex California extent when web layer is Bay Area centric), follow guide on [Recalculating Feature Class Extent](AGOL-Technical-Resources.md#recalculate-feature-class-extent). For ArcGIS Pro layers formed using 'Make Layer From Selected Features' function, first export data to a temporary shapefile or file geodatabase feature class or resulting ArcGIS Online web layer will contain extent of source data, not the selected subset.
7. Check the spatial reference of the layer - if layer's spatial reference is not EPSG 4326 (WGS 84), project layer using the [Project Geoprocessing Tool](http://pro.arcgis.com/en/pro-app/tool-reference/data-management/project.htm). If reprojecting from NAD 83, choose the Geographic Transformation **NAD_1983_To_WGS_1984_5** for datasets within the contitential United States. For more information on geographic transformations, see the ESRI Technical Support page on [How To: Determine which NAD_1983_To_WGS_1984 transformation to use](https://support.esri.com/en/technical-article/000005929) 

***Steps to follow using ArcGIS Online once web layer is published***

8. Update ownership of web layer from current owner to content_MTC (if not already owned by that user) for PDF maps and ArcGIS Online web maps; change current owner to orgData for enterprise and open data web layers
9. Ensure that web layer meets minimum documentation requirements for curated content. See [detailed documentation requirements](Documentation.md##basic-documentation)
10. Under feature layer settings, ensure that delete protection is enabled and editing is disabled
11. Under feature layer settings, check box next to layer name under Optimize Layer Drawing and click Save button to increase layer drawing performance
12. Mark content status as **Authoratative**

### Web Maps

1. Ensure web layers used in web map have followed the process outlined in the [Web Layers Section](#web-layers)
2. Ensure web map is documented, following the basic documentation requirements. See [basic documentation requirements](Documentation.md#basic-documentation)
    - Detailed documentation not necessary for web maps as layers supporting the web map should be well - documented.
    - Provide links to supporting layers in Description for quick access to their information
3. Ensure that content is tagged appropriately. See [tag strategy](https://mtcdrive.app.box.com/file/198480762097)
4. Share with [MTC Map Gallery Groups](http://mtc.maps.arcgis.com/home/group.html?id=4bb2944ff35348c3847859b48d28336d#overview)

### PDF Maps

1. Ensure web map is documented, following the basic documentation requirements. See [basic documentation requirements](Documentation.md#basic-documentation)
   - PDFs at minimum should have the following: 
     - Title
     - Summary
     - Description (write up)
     - Link to project documentation on github (if available) 
2. Ensure that content is tagged appropriately. See [tag strategy](https://mtcdrive.app.box.com/file/198480762097)
   - Ensure that month and year are included as seperate tags (ex July, 2017)
3. Share with [MTC Map Gallery Groups](http://mtc.maps.arcgis.com/home/group.html?id=4bb2944ff35348c3847859b48d28336d#overview)
