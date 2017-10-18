## Define the Problem Statement

Map OBAG 2.0 projects and prepare maps for public dissemination.

## Data Sources

#### Federal - Aid Elligible Roads (show in in project mapper tool) 
- Federal Highway Administration - Office of Highway Policy Information 
   - [Highway Performance Monitoring System (HPMS) Shapefiles - 2014](https://www.fhwa.dot.gov/policyinformation/hpms/shapefiles.cfm)

#### Excel file for mapping status: 
- [OBAG 2 Project List](https://mtcdrive.app.box.com/file/213843146655)
#### Mapping tool project records:
- Database Server: GISDB2
- Database: WebGIS
    - Table: rpd.MapApplicationData
#### Project views for export to fileGDB
- Database Server: GISDB2
- Database: WebGIS
    - Polyline View: RPD_OBAG_2_Project_Lines 
    - Point View: RPD_OBAG_2_Project_Points
    - Polygon View: RPD_OBAG_2_Project_Polygon

## Analysis Parameters

Projects are classified as IN/OUT of PDAs

**Federal - Aid Elligible Roads** 

Federal - Aid Elligible roads are highways that are part of the HPMS-defined Federal-Aid System. HPMS - California shapefile contains a field which holds applicable Federal Functional Classifications called **F_System**. For our purposes, we're only interested in **Urban** Federal Aid Roads. Urban Federal Aid Roads are all roads that are not equal to **'99999'**. This number represents rural area highway sections as defined by U.S. Census Urban Rural Area Codes. Urban Codes are stored within the **Urban_Code** field. The table below summarizes the values which should be selected to determine which highways are Urban Federal-Aid Elligible. The [Highway Performance Monitoring System Field Manual](https://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/hpms_field_manual_dec2016.pdf) contains data item lookup coding requirements and guidance. 

***HPMS - California Shapefile Select Values***

|Field Name | Values                  |
|-----------|-------------------------|
|F_System   |1,2,3,4,5,6              |
|Urban_Code | != 99999                |
|County_Cod |75,81,41,55,95,1,85,13,97|

***F_System Value Description***

|Code |Description                                        |
|-----|---------------------------------------------------|
|1    |Interstate                                         |
|2    |Principal Arterial - Other Freeways and Expressways|      
|3    |Principal Arterial - Other                         |
|4    |Minor Arterial                                     |
|5    |Major Collector                                    |
|6    |Minor Collector                                    |
|7    |Local                                              |

***Urban_Code Value Description***

|Code     |Description         |
|---------|--------------------|
|99999    |Rural Area Sections |
|99998    |Small Urban Sections|
|All Other|Urban               | 


## Methodology applied to solve problem

1. Projects mapped using web-based project mapper tool. See - [Project Mapper](http://project-mapper.us-west-2.elasticbeanstalk.com/)
2. Three Views created from [Mapping tool project records](#mapping-tool-project-records) using [Create Point Line Poly Views](https://github.com/BayAreaMetro/Spatial-Analysis-Mapping-Projects/blob/master/OBAG-2-Project-Mapping/Scripts/Create_Point_Line_Poly_Views.sql) script
    - [Project views for export to fileGDB](#project-views-for-export-to-fileGDB)

## Expected Outcomes (if any)?

1. Tabloid map series illustrating projects for the nine-county bay area region.  Projects are symbolized by Mode...  
2. Project Database contains PNT, LN, and PY features for the Projects.  Projects can be viewed using the Project Mapper tool (link above)

## Potential Future Actions that may be Necessary to Take, but Unrelated to the Needs/ Requirements of this Project.

OBAG 2.0 Projects will eventually be assigned a TIP ID. We will need to coordinate with the TIP Team (Mallory/Adam C.) to confirm the project list.

## Results

[OBAG 2 Print Map Files](https://mtcdrive.box.com/s/pynzziqwe8b7ur74jdpdxzxc8vkdpa6w)
