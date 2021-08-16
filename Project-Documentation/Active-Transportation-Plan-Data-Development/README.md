-- Draft --

# Active Transportation Plan Data Development

Create a consolidated, Regional Bike Network dataset conflated to the Travel Model II network, which include all bike facilities collected from the 9-Bay Area Congestion Management Agencies (CMAs) and the 3 largest Bay Area Cities - San Jose, San Francisco, and Oakland. 

## Project Resources

Add links to:
- [Asana Task](https://app.asana.com/0/229355710745434/1199875072414782)
- [Box Data Development & Outputs Directory](https://mtcdrive.box.com/s/gy0u7jg4i1mwad9vqarzlkigg6qxbcvv)
- [Box Data Collection Directory](https://mtcdrive.app.box.com/folder/140341300081?s=tnttek9iqztxw1ibaj7ltyot2e66yikd)
- [Bike Ped Network Data Collection Inventory](https://mtcdrive.box.com/s/tfuj96k1tqqirg42c8qtlzty7gd8pi2u)


### Table of Contents

- [Data Sources](#data-sources)
- [Analysis Parameters](#analysis-parameters)
	- [Regional Bikeway Network Classes](#regional-bikeway-network-classes)
- [Methodology](#methodology)
- [Results](#results)
- [Related Work](#related-work)

## Data Sources

- [Regional Bikeway Network (MTC Access Only)](https://arcgis.ad.mtc.ca.gov/portal/home/item.html?id=3a58a12a474444e3ab60b5551fba1a9a)
- [Regional Bikeway Network (Public)](https://opendata.mtc.ca.gov/datasets/regional-bikeway-network-2019/explore)
- [State, County, City Bike and Pedestrian Networks](https://mtcdrive.app.box.com/folder/140341300081?s=tnttek9iqztxw1ibaj7ltyot2e66yikd)

### Source Organizations
| Source                                               | Type                  | Website                                                                           |
|------------------------------------------------------|-----------------------|-----------------------------------------------------------------------------------|
| City of Oakland Department of   Transportation       | City                  | https://www.oaklandca.gov/departments/transportation                              |
| Alameda County Transportation Authority              | CMA                   | https://www.alamedactc.org/                                                       |
| City/County Association of Governments   San Mateo   | CMA                   | https://ccag.ca.gov/                                                              |
| Contra Costa Transportation Authority                | CMA                   | https://ccta.net/                                                                 |
| Napa Valley Transportation Authority                 | CMA                   | https://www.nvta.ca.gov/                                                          |
| San Francisco County Transportation   Authority      | CMA                   | https://www.sfcta.org/                                                            |
| Solano Transportation Authority                      | CMA                   | https://sta.ca.gov/                                                               |
| Sonoma County Transportation Authority               | CMA                   | https://scta.ca.gov/                                                              |
| Transportation Authority of Marin                    | CMA                   | https://www.tam.ca.gov/                                                           |
| Valley Transportation Authority                      | CMA                   | https://www.vta.org/                                                              |
| Bay Area Trails Collaborative                        | Non-Profit / Advocacy | https://www.railstotrails.org/our-work/trailnation/bay-area-trails-collaborative/ |
| California Department of Transportation   District 4 | State                 | https://dot.ca.gov/caltrans-near-me/district-4                                    |

## Analysis Parameters

### Regional Bikeway Network Schema

| Column     | Column Alias            | Type    | Description                                                                   | Domain                                          |
|------------|-------------------------|---------|-------------------------------------------------------------------------------|-------------------------------------------------|
| shape_id   | TM2 Shape ID            | text    | Travel Model II Shape Join ID                                                 |                                                 |
| cma_ex_cl  | CMA Existing Class      | numeric | CMA Existing Bicycle Facility Class Value                                     | 0;1;2;3;4;999                                   |
| cma_pl_cl  | CMA Planned Class       | numeric | CMA Planned/Proposed Bicycle Facility Class Value                             | 0;1;2;3;4;999                                   |
| oak_ex_cl  | Oakland Existing Class  | numeric | City of Oakland Existing Bicycle Facility Class Value                         | 0;1;2;3;4;999                                   |
| oak_pn_cl  | Oakland Planned Class   | numeric | City of Oakland Planned/Proposed Bicycle Facility Class Value                 | 0;1;2;3;4;999                                   |
| sj_ex_cl   | San Jose Existing Class | numeric | City of San Jose Existing Bicyle Facility Class Value                         | 0;1;2;3;4;999                                   |
| sj_pl_cl   | San Jose Planned Class  | numeric | City of San Jose Planned/Proposed Bicycle Facility Class Value                | 0;1;2;3;4;999                                   |
| batc_ex_cl | BATC Existing Class     | numeric | Bay Area Trails Collaborative Existing Bicycle Facility Class Value           | 0;1;2;3;4;999                                   |
| batc_pl_cl | BATC Planned Class      | numeric | Bay Area Trails Collaborative Planned/Proposed Bicycle Facility Class Value   | 0;1;2;3;4;999                                   |
| calt_ex_cl | CalTrans Existing Class | numeric | California Department of Transportation D4 Existing Bicycle Facility Class Value           | 0;1;2;3;4;999                                   |
| calt_pl_cl | CalTrans Planned Class  | numeric | California Department of Transportation D4 Planned/Proposed Bicycle Facility Class Value   | 0;1;2;3;4;999                                   |

The consolidated, regional bike facilities dataset should include a class column with facilities classified as follows: 

**[Highway Design Manual Bicycle Transportation Design](https://web.archive.org/web/20170501101515id_/http://www.dot.ca.gov/hq/oppd/hdm/pdf/english/chp1000.pdf)**

- Class 0: Unpaved, or dirt bike facility. This classification only used for Contra Costa County.
- Class 1: Off-Street Shared-Use Path - A bikeway physically separated from motorized vehicular traffic by an open space or barrier. Pedestrians, skaters, wheelchair users, joggers, and other non-motorized users typically use shared-use paths.
- Class 2: Bike Lane - Portion of the roadway that has been designated by striping, signing and pavement markings for the preferential or exclusive use of bicycles. Some cities and counties also define wide shoulders as bike lanes. Always ride about 4 feet from parked cars to avoid the door zone.
- Class 3: On-Street Bike Route - Any road or street designated for bicycle travel. These routes are not for the exclusive use of cyclists. Often, routes include residential streets with low auto volumes and speeds.
- Class 4: Separated Bike Lanes - Separated bike lanes, also known as cycle tracks or protected bike lanes, are a dedicated bikeway that combines the user experience
 of a multi-use path but are located on a street. They are physically distinct from the sidewalk and separated from motor vehicle traffic by a physical object such as parking, a curb, or posts.
- Class 999: The classification was unknown or not yet determined.

## Methodology

The consolidated, Regional Bike Facilities dataset was created through a mix of manual updates to the facility geometries using ArcGIS Pro desktop editing tools, as well as a scripted processes in python jupyter notebooks. State, City, and Non-Profit Advocacy Bike Facility datasets also underwent processing to standardize the schema and values to match the expected columns and attribute values as indicated in the [Regional Bikeway Network Schema](#regional-bikeway-network-schema). Each of these datasets were then conflated with the Travel Model II Network, leveraging the [Shared Streets Python Library](https://github.com/sharedstreets/sharedstreets-python). The resulting dataset is an attribute join table modeled after the [Regional Bikeway Network Schema](#regional-bikeway-network-schema) above.

Processing Steps:

1. Project each bike network dataset to NAD1983 UTM Z 10N, or EPSG 26910
2. Review facilities that cross jurisdictional boundaries, edit line ends to connect to facilities in adjacent jurisdictions
3. Map class attributes from jurisdiction class to a standardized classification using only numeric values. If class stored in a single column, separate class into existing or planned class columns based on a status column if present. Otherwise if an existing and planned / proposed class column already exists, add those values to the existing and planned class columns. ([See Regional Bikeway Network Schema](#regional-bikeway-network-schema))
	- [Bike Network Data Cleanup Notebook](Bike_Network_Data_Cleanup.ipynb )
4. Conflate each bike facility dataset with Travel Model II Network
	- [Bike Network Conflation Notebook (not yet added)]()


## Results

## Related Work

[Regional Bike Network Summaries](../Regional%20Bike%20Network%20Summaries)