-- Draft --

# Plan Bay Area 2050 Transit Data Updates


Map new, planned and existing rail, ferry, and bus stops. Bus stops should contain a field flagging stops that qualify as a 'Major Transit Stops', as well as a field classifying stops served by routes meeting certain headway criteria.

The Existing Transit Stops dataset will replace the existing [Major Transit Stop](https://mtc.maps.arcgis.com/home/item.html?id=561dc5b42fa9451b95faf615a3054260) dataset, and will represent all transit stops in the Bay Area as of January 2020. 

### Project Resources

- [Asana Project - PBA 2050 Transit Data](https://app.asana.com/0/229355710745434/1177953172585985)
- [Box Directory](https://mtcdrive.box.com/s/ahdbq95qsuhpov42cmut147qp70sgj1g) 

### Table of Contents
-[Data Sources](#data-sources)
-[Analysis Parameters](#analysis-parameters)
	-[Existing Transit Stops](#existing-transit-stops)
		-[General Transit Feed Specification (GTFS)](#general-transit-feed-specification)
-[Methodology](#methodology)
	-[Planned or New Transit Stops Methodology](#planned-or-new-transit-stops-methodology)
	-[Existing Transit Stops Methodology](#existing-transit-stops-methodology)
-[Expected Outcomes](#expected-outcomes)
-[Results](#results)
-[Related Work](#related-work)

## Data Sources

- [511 Regional GTFS API January 2020](https://511.org/open-data/transit)
	- [Historic GTFS Data (MTC Access Only)](https://mtcdrive.box.com/s/704dfa2xadbcn91youc7pcaccnrlmvu1)
- [All Potential PBA 2050 Blueprint Stations (MTC Access Only)](https://mtcdrive.box.com/s/zn6geq8qtgh1gb88c28k1mdwbnlwfeg2)


## Analysis Parameters

### Existing Transit Stops

The existing transit stops dataset includes all transit stops for the Bay Area, including attributes that indicate level of service for routes served by them. The table below provides the columns that will contain level of service information as well as a description of the level of service criteria, such as headway threshold, time period, number of routes served, or route type. 

| Field Name Long    | Description                                                                                                                                                                                                                                                                                                                           | Domain                                                        |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| Headway 30 Minute  | Flag field for stops served by 1 or more transit routes with headways of 30 minutes or less during BOTH the AM (6:00 - 10:00 AM) and PM (3:00 - 7:00 PM) peak commute period                                                                                                                                                          | 0; 1                                                          |
| Headway 15 Minute  | Flag field for stops served by 1 or more transit routes with headways of 15 minutes or less during BOTH the AM (6:00 - 10:00 AM) and PM (3:00 - 7:00 PM) peak commute perio                                                                                                                                                           | 0; 1                                                          |
| Major Transit Stop | To qualify as a 'Major Transit Stop',as defined by As defined by [California Public Resource Code Section 21064.3](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=21064.3.&lawCode=PRC), a stop must be a rail or ferry stop, or the stop must be served by 2 or more transit routes with headways of 15 minutes or less during BOTH the AM (6:00 - 10:00 AM) and PM (3:00 - 7:00 PM) peak commute periods.  | 0; 1                                                          |
| Headway Class      | To fall into a given headway class, stops had to meet the headway threshold for both AM (6:00 - 10:00 AM) and PM (3:00 - 7:00 PM) Peak Periods. Not available is used for stops served by routes where headway information may be unavailable for am or pm commute periods.                                                           | 15 mins or less; 16 to 30 min; 31 mins or more; Not Available |

#### General Transit Feed Specification

General Transit Feed Specification (GTFS) static data was used to create the Existing Transit Stops dataset. The General Transit Feed Specification (GTFS), also known as GTFS static or static transit to differentiate it from the GTFS realtime extension, defines a common format for public transportation schedules and associated geographic information. GTFS "feeds" let public transit agencies publish their transit data and developers write applications that consume that data in an interoperable way.

The specification is made up of a number of text files. The data model below defines the relationships between those files. For more information, please review the [GTFS Static Reference Guide](https://developers.google.com/transit/gtfs)

![gtfs_diagram](img/Relations-among-different-text-files-of-a-GTFS-feed.png)

## Methodology

### Planned or New Transit Stops Methodology

Planned transit stops refer to fully funded projects that have been approved for construction or are currently under construction, while proposed transit stops refer to potential new transit stops that have not yet been fully funded or approved but are currently under study by MTC and ABAG for inclusion in Plan Bay Area 2050. Point features for planned or proposed stops were manually created based on qualitative descriptions of stop locations provided by project sponsors. Note that stop locations are approximate and subject to change as projects progress through environmental review and detailed planning work.

- The ppa_id and ppa_name field values are from the Horizon Project Performance Assessment: List of Transportation Projects (Feb 2020) located at https://mtc.ca.gov/sites/default/files/ProjectPerformance_List.pdf
- The transit type values in route_ty_t were changed from their original values to match the types used by GTFS
- County values were derived by selecting stops that intersected TomTom 2017 county features and assigning the value using the ArcGIS Pro calculator
- Jurisdiction values were derived through a spatial join with TomTom 2017 place features for incorporated jurisdictions in the San Francisco Bay Region using ArcGIS Pro. The unincorporated areas were added by selecting stops that intersected TomTom 2017 county features and using the ArcGIS Pro Calculator to assign a name

### Existing Transit Stops Methodology

To create the existing transit stops, ESRI Public Transit tools were leveraged as well as pandas/python tools. The tools and script rely on Regional General Transit Feed (GTFS) specification data provided by the [Bay Area 511 GTFS API](https://511.org/open-data/transit). 

The process was scripted in a jupyter notebook running in an ArcGIS Pro environment. You can review the processing script [here](gtfs_transit_stops_processing.ipynb). To run the script, you will need to download the ArcGIS Pro project which contains the ESRI toolboxes, jupyter nootebooks as well as the data you would need to repeat the process which can be accessed [here (MTC Acces Only)](https://mtcdrive.box.com/s/dr4bo6n1wois3dm4lutad8pivdj50uu3).   

**Resource Links**
- [ESRI Public Transit Tools](https://github.com/Esri/public-transit-tools)
- [General Transit Feed Specification (GTFS) Reference](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)

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
