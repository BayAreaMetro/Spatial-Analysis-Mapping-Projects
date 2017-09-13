## Define the Problem Statement

Map OBAG 2.0 projects and prepare maps for public dissemination.

## Data Sources

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
