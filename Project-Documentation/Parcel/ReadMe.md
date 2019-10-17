# San Francisco Bay Region Parcels (2019) 

Parcels form the base unit of much of the analysis performed by the Metropolitan Transportation Commission (MTC) Regional Planning Program (RPP), specifically the Data & Visualization and Modeling groups.


### Contents 

[Problem Statement](#problem-statement)

[Data Sources](#data-sources) 

[Analysis Parameters](#analysis-parameters)

[Methodology](#methodology)

[Expected Outcomes](#expected-outcomes)

[Results](#results) 


## Problem Statement
The purpose of this project is to create 2019 parcel feature sets for the San Francisco Bay Region and each of its nine counties. 


## Data Sources 
All datasets downloaded on August 26, 2019

| County | Download Location | Source Data Date |
| --- | --- | --- |
| Alameda County | [Alameda County Data Sharing Initiative](https://data.acgov.org/Geospatial-Data/Alameda-County-Parcel-Boundaries/2m43-xsic) | 23 Apr 2019 |
| Contra Costa County | [Contra Costa County public, web data directory](https://gis.cccounty.us/Downloads/Assessor/) | Mar 2019 |
| Marin County | [Marin GeoHub](https://gisopendata.marincounty.org/datasets/MarinCounty::parcel) | 23 Aug 2019 |
| Napa County | [Napa County GIS Data Catalog](http://gis.napa.ca.gov/giscatalog/catalog_xml.asp) | 03 Jul 2019 |
| San Francisco | [DataSF](https://data.sfgov.org/Geographic-Locations-and-Boundaries/Parcels-Active-and-Retired/acdm-wktn) | 25 Aug 2019 |
| San Mateo County | [County of San Mateo Information Services - GIS Data Download](https://isd.smcgov.org/gis-data-download) | 26 Aug 2019 |
| Santa Clara County | [County of Santa Clara Open Data Portal](https://data.sccgov.org/Government/Parcels/6p99-rtwk) | 26 Aug 2019 |
| Solano County | Solano GeoHub - [Parcels 2019](http://geohub-doitgis.opendata.arcgis.com/datasets/parcels2018-2) and [Parcels 2018](http://geohub-doitgis.opendata.arcgis.com/datasets/parcels2018) | 07 Aug 2019 and 20 Jul 2018 |
| Sonoma County | [County of Sonoma public, web data directory](https://links.sonoma-county.org/nlhrCoQbqzY/) | 20 Aug 2019 |


## Analysis Parameters

As part of the development of these feature sets, the number of parcel attributes was kept to a minimum. The final attribute tables have the following fields:
  + **joinid** - Identification value for joining external tables to parcel features
  
  + **fipco** - Federal Information Processing Standards (FIPS) code for the county containing the parcel
  
  + **jurisdict** - Incorporated jurisdiction, or unincorporated area, containing the parcel
  
  + **apn** - Unformatted Assessor's Parcel Number (APN)
  
  + **apn_frm** - Formatted APN
  
  + **acres** - Parcel size in gross acres
  
  + **wtrprcl** - Identifies whether parcel is on land or in water (this field is only included in the regional feature set on Socrata)

The APN fields are the only attribute fields included from the source data. The values in these fields were not altered from the source data. The exception is where APN values could be calculated from one or more columns in the source table without modifying the numbers, if the source column had leading zeros there were leading zeros in the calculated value, if leading zeros were not provided, there are none in the calculated value.

  + If the attribute table only provided formatted APNs, then values were calculated for the unformatted APN column by removing the connection character from the formatted column
  
  + If the attribute table included multiple fields that cleanly separated the APN components, then values for the formatted APN column were calculated by joining them together with the connecting character added between the components


## Methodology 

***Feature Set Preparation***

__Contra Costa__ - The source feature set of parcel polygons did not include APN values for the parcels. The only attibute was a join value. As a result, a parcel point feature set also needed to be downloaded. The point feature set contained the APN, and other attributes, for the parcel polygons. As there were more points than polygons, this seemed to be done to prevent the inclusion of stacked polygons in the polygon feature set. Since Contra Costa County was the only county to do this. County data preparation was:
  + Join parcel points to parcel polygons using the PARC_PY_ID field
  + Export new polygon feature set
  + Delete duplicate join field

__San Francisco__ - The source feature set of San Francisco parcels included both active and inactive parcels. County data preparation was:
  + Select parcels with a value of 1 in the active_ret field. Available values were 1 - active and 0 - retired
  + Export selected parcels as new feature set

__Solano__ - The parcel feature set released in 2019 had hundreds of missing parcels. To address this, the 2018 release was also downloaded so a, mostly (both versions had missing parcels), complete parcel coverage for the county could be created. County data preparation was:
  + Erase areas in 2018 release using features from the 2019 release
  + Run Repair Geometry tool on remaining areas from 2018 release with OGC and Delete Features with Null Geometry parameters selected
  + Merge remaining areas from 2018 release with the 2019 release
  + Calculate APNs from each release into a single field. One of the releases had two APN fields, both of which were incomplete. However, each parcel had an APN if the fields were combined
  + Run Dissolve tool, using the new, complete APN field, to create a new multipart feature set



***Process County Feature Sets*** _(Except where noted, all work was done in ArcGIS Pro 2.4.1)_

For each county:
1. Run Repair Geometry tool with OGC and Delete Features with Null Geometry parameters selected

2. Check projection of source feature set. Projection used at MTC is GCS WGS 1984:
>  + If feature set needs to be projected, have Project tool create output feature set in working file geodatabase
>    + Alameda County was projected from WGS 1984 Web Mercator Auxiliary Sphere without a transformation
>    + Contra Costa County was projected from NAD 1983 StatePlane California III FIPS 0403 Feet using the NAD_1983_HARN_To_WGS_1984_2 transformation
>    + Marin County was projected from NAD 1983 HARN StatePlane California III FIPS 0403 (US Feet) using the NAD_1983_HARN_To_WGS_1984_2 transformation
>    + Napa County was projected from NAD 1983 HARN StatePlane California II FIPS 0402 Feet using the WGS_1984_(ITRF00)_To_NAD_1983 transformation
>    + City & County of San Francisco was projected from WGS84(DD) without a transformation
>    + San Mateo County was projected from NAD 1983 HARN StatePlane California III FIPS 0403 Feet using the WGS_1984_(ITRF00)_To_NAD_1983 transformation
>    + Santa Clara County was projected from WGS84(DD) without a transformation
>    + Solano County distributes their data as GCS WGS 1984 so did not need to be projected
>    + Sonoma County was projected from NAD 1983 HARN StatePlane California II FIPS 0402 Feet using the WGS_1984_(ITRF00)_To_NAD_1983 transformation
>
>  + If feature set does not need to be projected, export features to working file geodatabase
  
3. If feature set was projected, run Repair Geometry tool with OGC and Delete Features with Null Geometry parameters selected

4. Delete unnecessary fields from attribute table

5. Add fields for final feature set attribute table

6. Calculate joinid field:
>  + Add temporary field (six character text field) for number portion of joinid field
>  + Calculate sequential numbers in temporary field for all parcels:
>    + Type autoIncrement() into the *fieldName*= box
>    + Type the following into the Code Block section:
>        ```python
>        rec = 0
>        def autoIncrement():
>          global rec
>          pStart = 1
>          pInterval = 1
>          if (rec == 0):
>            rec = pStart
>          else:
>            rec = rec + pInterval
>          return rec
>        ```
>  + Calculate joinid field by combining two-letter county abbreviation and numbers from temporary field
>    + Two-letter county abbreviations, displayed as XX in expression below, are: AL (Alameda County), CC (Contra Costa County), MA (Marin County), NA (Napa County), SF (City & County of San Francisco), SM (San Mateo County), SC (Santa Clara County), SL (Solano County), and SN (Sonoma County)
>    + Type `"XX" + !tempField!.zfill(6)` into joinid= box
>  + Delete temporary field

7. With the exception of San Francisco, which is both a city and county (each entity has the same boundary as the other), the jurisdiction values provided in the source data (when provided) was not useable. This was because the provided jurisdiction information either assigned parcels in a jurisdiction's sphere of influence (SOI) to the jurisdiction itself or included the names of unincorporated communities recognized by the United States Postal Service and United States Census Bureau, or a combination of the two. The purpose of the jurisdict field in the parcel feature sets is to identify parcels that are actually located within the jurisdiction boundaries they are labeled as being in. All other parcels are listed as being on unincorporated county land. The following was used to Calculate the jurisdict field:
>  + Run Feature to Point tool, with Inside parameter selected, to create parcel centroids that are forced to be within the parcel boundary
>  + Spatial Join parcel centroids to incorporated jurisdictions, from TomTom base data, for county. This will create a new feature set
>  + Create definition query for new parcel centroid feature set so only features where name Is Not Null are returned
>  + Join new parcel centroids to parcel polygons, using joinid field, with Keep All Target Features unchecked
>  + Calculate jurisdict field using values from new parcel centroid feature set
>  + Remove join so all parcel polygon features are available again
>  + Select parcel polygon features where jurisdict value is null
>  + Calculate "Unincorporated _countyName_" as value. Values used were: Unincorporated Alameda, Unincorporated Contra Costa, Unincorporated Marin, Unincorporated Napa, Unincorporated San Mateo, Unincorporated Santa Clara, Unincorporated Solano, and Unincorporated Sonoma. As city and county boundaries are the same, there are not unincorporated areas in San Francisco.

8. Calculate remaining new fields:
>  + __fipco__ - Calculate using same county value as the TomTom base data: CA001 (Alameda County), CA013 (Contra Costa County), CA041 (Marin County), CA055 (Napa County), CA075 (City & County of San Francisco), CA081 (San Mateo County), CA085 (Santa Clara County), CA095 (Solano County), and CA097 (Sonoma County)
>  + __apn__ - Calculate using either the source field, when provided, or by deleting the connecting character from a formatted APN field
>  + __apn_frm__ - Calculate using source field, when provided as either a single field or could be assembled from multiple source fields without changing values of those fields. If neither of those options were available, this field was left blank
>  + __acres__ - Calculate using Calculate Geometry Attributes tool with area selected as the Target Field property and NAD 1983 UTM Zone 10N as the coordinate system used to calculate the area of the parcel feature

9. Delete original, source fields

10. Run Repair Geometry tool with OGC and Delete Features with Null Geometry parameters selected

11. Run Clip tool to make parcel feature set conform to county boundary in TomTom base data. This is done because of differences in base data sources and projections utilized by counties in the region. The lack of base data and projection standards in the region results in parcels for one county appearing in a neighboring county
>  + This does result in the loss of some parcels, but the loss is insignificant enough that it is acceptable
>  + This also results in some parcels becoming smaller because they are partially within a neighboring county. Acres were calculated using the original features so the value reflects the size of the feature provided by the county

12. Run Multipart To Singlepart tool on clipped feature set

13. Delete ORIG_FID field

14. Run Repair Geometry tool, with OGC and Delete Features with Null Geometry parameters selected, to correct errors exposed/created by either the Clip and/or Multipart To Singlepart tool

15. Run Dissolve tool, selecting all non-ESRI fields, to create replacement multipart, parcel feature set

16. Run Repair Geometry tool, with OGC and Delete Features with Null Geometry parameters selected, on new multipart feature set

17. Export county, multipart (dissolved) feature sets to the project file geodatabase (project file geodatabase automatically created by ArcGIS Pro when first creating the project)

18. Export county, singlepart (exploded) feature sets to the project file geodatabase


***Assemble Regional Feature Sets***

19. Run Merge tool to assemble multipart, county-specific feature sets into a regional feature set in the project file geodatabase

20. Run Merge tool to assemble singlepart, county-specific feature sets into a regional feature set in the project file geodatabase

21. For regional, singlepart feature set only, add wtrprcl field to the attribute table so parcels can be designated as being either on land or in water. The need for this field is specific to a use required by the RPP Data & Visualization group. Values calculated by:
>    + Run Select Layer By Location tool on parcel feature set, with major water features from TomTom base data as the Selecting Features and the Relationship parameter set to Within. The Within parameter is used so parcels that are mostly over water, but still have a portion on land are not excluded when querying out water parcels.
>    + Enter 1 (water parcel) in field for all selected features
>    + Right-click layer and select Switch Selection from Selection section of menu
>    + Enter 0 (land parcel) in field for all selected features
>    + Clear all selected features

22. Upload all parcel feature sets (county, multipart region, singlepart region) to enterprise database using OSGeo4W Shell from QGIS

23. Upload county feature sets to ArcGIS Online using Share As Web Layer function

24. Convert regional, singlepart feature set to GeoJSON using Features To JSON tool

25. Upload regional, singlepart feature set to Socrata using GeoJSON file


## Expected Outcomes
The expectation was there would be updated parcel feature sets that MTC planning staff could import into their own analysis, mapping, and web application projects. The county feature sets available on ArcGIS Online are intended for use by planners in their analysis and mapping projects. This was done to reduce the amount of time they would need to wait for features to load from ArcGIS. If they need parcels for the full region, it is expected they would either run their analyses on each county and then merge their results or they would download each county and assemble them into a regional feature set for their project. The regional feature sets on the enterprise database are intended for projects conducted by the Data & Visualization group. The singlepart feature set on Socrata is intended for projects conducted by the Data & Visualization and Modeling groups.


## Results 
All final, parcel feature sets were placed on ArcGIS Online and Socrata, with access permission limited to Metropolitan Transportation Commission staff. The feature sets on the enterprise database are restricted to the Data & Visualization group.

#### Socrata
- [San Francisco Bay Region Parcels (2019)](https://data.bayareametro.gov/Cadastral/Parcels-2019/kah7-2qc6)

#### ArcGIS Online
- [Alameda County Parcels (2019)](https://mtc.maps.arcgis.com/home/item.html?id=63b8cd008c7242a6b18935412f90b24e)
- [Contra Costa County Parcels (2019)](https://mtc.maps.arcgis.com/home/item.html?id=b8c2b80f82c44ef796a1c5b589ccd0ea)
- [Marin County Parcels (2019)](https://mtc.maps.arcgis.com/home/item.html?id=cf5a2952561d4bb38a84a60aaef6c8b3)
- [Napa County Parcels (2019)](https://mtc.maps.arcgis.com/home/item.html?id=85cb0e6aedb140178eab990d89841c70)
- [San Francisco Parcels (2019)](https://mtc.maps.arcgis.com/home/item.html?id=133adef01b8c44688230657cd839da78)
- [San Mateo County Parcels (2019)](https://mtc.maps.arcgis.com/home/item.html?id=d99b89e9834c43a4bad5396fa4187066)
- [Santa Clara County Parcels (2019)](https://mtc.maps.arcgis.com/home/item.html?id=88143a84f4914d48a6bb411e4b6d9d1b)
- [Solano County Parcels (2019)](https://mtc.maps.arcgis.com/home/item.html?id=1f2f4e27caa348a7bb2457d1fc97cc4b)
- [Sonoma County Parcels (2019)](https://mtc.maps.arcgis.com/home/item.html?id=6b99f78c64cf4e11a12ea38ccf612e1a)
