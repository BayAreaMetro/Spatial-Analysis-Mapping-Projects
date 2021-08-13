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

## Analysis Parameters

### Regional Bikeway Network Schema

**Insert Table here**

The consolidated, regional bike facilities dataset should include a class column with facilities classified as follows: 

**[Highway Design Manual Bicycle Transportation Design](https://web.archive.org/web/20170501101515id_/http://www.dot.ca.gov/hq/oppd/hdm/pdf/english/chp1000.pdf)**

- Class I: Off-Street Shared-Use Path - A bikeway physically separated from motorized vehicular traffic by an open space or barrier. Pedestrians, skaters, wheelchair users, joggers, and other non-motorized users typically use shared-use paths.
- Class II: Bike Lane - Portion of the roadway that has been designated by striping, signing and pavement markings for the preferential or exclusive use of bicycles. Some cities and counties also define wide shoulders as bike lanes. Always ride about 4 feet from parked cars to avoid the door zone.
- Class III: On-Street Bike Route - Any road or street designated for bicycle travel. These routes are not for the exclusive use of cyclists. Often, routes include residential streets with low auto volumes and speeds.
- Class IV: Separated Bike Lanes - Separated bike lanes, also known as cycle tracks or protected bike lanes, are a dedicated bikeway that combines the user experience
 of a multi-use path but are located on a street. They are physically distinct from the sidewalk and separated from motor vehicle traffic by a physical object such as parking, a curb, or posts.

## Methodology

The consolidated, Regional Bike Facilities dataset was created through a mix of manual updates to the facility geometries using ArcGIS Pro desktop editing tools, as well as a scripted processes in python jupyter notebooks. 

Processing Steps:

1. Project each bike network dataset to NAD1983 UTM Z 10N, or EPSG 26910
2. Review facilities that cross jurisdictional boundaries, edit line ends to connect to facilities in adjacent jurisdictions
3. Map class attributes from jurisdiction class to a standardized classification using only numeric values. If class stored in a single column, separate class into existing or planned class columns based on a status column if present. Otherwise if an existing and planned / proposed class column already exists, add those values to the existing and planned class columns. ([See Regional Bikeway Network Schema](#regional-bikeway-network-schema))
	- [Bike Network Data Cleanup Notebook](Bike_Network_Data_Cleanup.ipynb )


## Results

## Related Work

[Regional Bike Network Summaries](../Regional%20Bike%20Network%20Summaries)