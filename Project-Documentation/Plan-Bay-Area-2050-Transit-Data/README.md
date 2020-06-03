-- Draft --

# Plan Bay Area 2050 Transit Data Updates

### Define the Problem Statement

Map new and existing transit stops as well as rail, ferry, and bus stops served by routes meeting certain headway criteria for peak periods. 

### Project Resources

- [Asana Project - PBA 2050 Transit Data](https://app.asana.com/0/229355710745434/1177953172585985)
- [Box Directory](https://mtcdrive.box.com/s/ahdbq95qsuhpov42cmut147qp70sgj1g) 

## Data Sources

- [511 Regional GTFS API January 2020](https://511.org/open-data/transit)
	- [Historic GTFS Data (MTC Access Only)](https://mtcdrive.box.com/s/704dfa2xadbcn91youc7pcaccnrlmvu1)
- [All Potential PBA 2050 Blueprint Stations (MTC Access Only)](https://mtcdrive.box.com/s/zn6geq8qtgh1gb88c28k1mdwbnlwfeg2)


## Analysis Parameters

- [General Transit Feed Specification (GTFS) Reference](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#stopstxt)

**GTFS Relational Diagram**
- ![gtfs_diagram](img/Relations-among-different-text-files-of-a-GTFS-feed.png)

### Planned or New Transit Stops

### Existing Transit Stops (Define with a name that doesn't conflict with existing leg definitions or datasets)

Transit stops that are served by:
- Rail or Ferry
- Stop servied by bus routes with peak headways of 30 mins or less. 
	- AM Peak 6:00 A.M.–10:00 A.M.
	- PM Peak 3:00 P.M.–7:00 P.M. 


## Methodology applied to solve problem

- [ESRI Public Transit Tools](https://github.com/Esri/public-transit-tools)

## Expected Outcomes (if any)?

- New and Planned Transit Stops
- Existing Transit Stops with Routes Meeting AM/PM Peak Headways

## Results

## Related Work

- [Plan Bay Area 2050 Growth Framework](Plan-Bay-Area-2050-Growth-Framework)
- [Legislative Transit Data](https://github.com/BayAreaMetro/Data-Analysis-Projects/blob/master/legislative_transit_data.md)
- [Transportation MDM](https://github.com/BayAreaMetro/DataServices/tree/master/Project-Documentation/mdm/transportation-mdm)
- [511 GTFS Transportation Data](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/transportation-mdm/511_GTFS.md)

## Tags

Add tags to help others find your project, e.g. if you are documenting an analysis done to support Environmental Impact Reporting for Plan Bay Area 2050, add the tags **eir**, **plan bay area 2050**, **environment**.
