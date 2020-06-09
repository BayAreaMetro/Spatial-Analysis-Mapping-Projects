-- Draft --

# Plan Bay Area 2050 Transit Data Updates


Map new, planned and existing rail, ferry, and bus stops. Bus stops should contain a field flagging stops that qualify as a 'Major Transit Stops', as well as a field classifying stops served by routes meeting certain headway criteria.

The Existing Transit Stops dataset will replace the existing [Major Transit Stop](https://mtc.maps.arcgis.com/home/item.html?id=561dc5b42fa9451b95faf615a3054260) dataset, and will represent all transit stops in the Bay Area as of January 2020. 

### Project Resources

- [Asana Project - PBA 2050 Transit Data](https://app.asana.com/0/229355710745434/1177953172585985)
- [Box Directory](https://mtcdrive.box.com/s/ahdbq95qsuhpov42cmut147qp70sgj1g) 

## Data Sources

- [511 Regional GTFS API January 2020](https://511.org/open-data/transit)
	- [Historic GTFS Data (MTC Access Only)](https://mtcdrive.box.com/s/704dfa2xadbcn91youc7pcaccnrlmvu1)
- [All Potential PBA 2050 Blueprint Stations (MTC Access Only)](https://mtcdrive.box.com/s/zn6geq8qtgh1gb88c28k1mdwbnlwfeg2)


## Analysis Parameters


### GTFS Relational Diagram

![gtfs_diagram](img/Relations-among-different-text-files-of-a-GTFS-feed.png)

### Planned or New Transit Stops

### Existing Transit Stops

The existing transit stops dataset includes all transit stops for the Bay Area, including attributes that indicate level of service for routes served by them. The table below provides the columns that will contain level of service information as well as a description of the level of service criteria, such as headway threshold, time period, number of routes served, or route type. 


| Field Name Long    | Description                                                                                                                                                                                                                                                                                                                           | Domain                                                        |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| Headway 30 Minute  | Flag field for stops served by 1 or more transit routes with headways of 30 minutes or less during BOTH the AM (6:00 - 10:00 AM) and PM (3:00 - 7:00 PM) peak commute period                                                                                                                                                          | 0; 1                                                          |
| Headway 15 Minute  | Flag field for stops served by 1 or more transit routes with headways of 15 minutes or less during BOTH the AM (6:00 - 10:00 AM) and PM (3:00 - 7:00 PM) peak commute perio                                                                                                                                                           | 0; 1                                                          |
| Major Transit Stop | To qualify as a 'Major Transit Stop',as defined by As defined by [California Public Resource Code Section 21064.3](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=21064.3.&lawCode=PRC), a stop must be a rail or ferry stop, or the stop must be served by 2 or more transit routes with headways of 15 minutes or less during BOTH the AM (6:00 - 10:00 AM) and PM (3:00 - 7:00 PM) peak commute periods.  | 0; 1                                                          |
| Headway Class      | To fall into a given headway class, stops had to meet the headway threshold for both AM (6:00 - 10:00 AM) and PM (3:00 - 7:00 PM) Peak Periods. Not available is used for stops served by routes where headway information may be unavailable for am or pm commute periods.                                                           | 15 mins or less; 16 to 30 min; 31 mins or more; Not Available |

## Methodology

### Planned or New Transit Stops Methodology

### Existing Transit Stops Methodology

To create the existing transit stops, ESRI Public Transit tools were leveraged as well as pandas/python tools. The tools and script rely on Regional General Transit Feed (GTFS) specification data provided by the [Bay Area 511 GTFS API](https://511.org/open-data/transit). 

The process was scripted in a jupyter notebook running in an ArcGIS Pro environment. You can review the processing script [here](gtfs_transit_stop_processing.ipynb). To run the script, you will need to download the ArcGIS Pro project which contains the ESRI toolboxes, jupyter nootebooks as well as the data you would need to repeat the process which can be accessed [here (MTC Acces Only)](https://mtcdrive.box.com/s/dr4bo6n1wois3dm4lutad8pivdj50uu3).   

**Resource Links**
- [ESRI Public Transit Tools](https://github.com/Esri/public-transit-tools)
- [General Transit Feed Specification (GTFS) Reference](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#stopstxt)

## Expected Outcomes

- New and Planned Transit Stops
	- New and Planned Stops Metadata
- Existing Transit Stops with Routes Meeting AM/PM Peak Headways
	- Existing Transit Stops Metadata

## Results

- New and Planned Transit Stops Web Layer
	- [New and Planned Stops Metadata](transit_stops_potential_schema.csv)
- Existing Transit Stops Web Layer
	- [Existing Transit Stops Metadata](transit_stops_existing_schema.csv)

## Related Work

- [Plan Bay Area 2050 Growth Framework](Plan-Bay-Area-2050-Growth-Framework)
- [Legislative Transit Data](https://github.com/BayAreaMetro/Data-Analysis-Projects/blob/master/legislative_transit_data.md)
- [Transportation MDM](https://github.com/BayAreaMetro/DataServices/tree/master/Project-Documentation/mdm/transportation-mdm)
- [511 GTFS Transportation Data](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/transportation-mdm/511_GTFS.md)
