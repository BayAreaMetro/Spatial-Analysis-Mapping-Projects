-- Draft --
# Travel Diary Survey Conflation <!-- omit in toc -->

### Table of Contents

- [Define the Problem Statement](#define-the-problem-statement)
- [Project Scope](#project-scope)
- [Project Resources](#project-resources)
- [Data Sources](#data-sources)
  - [trips schema](#trips-schema)
  - [locations schema](#locations-schema)
- [Analysis Parameters](#analysis-parameters)
- [Methodology](#methodology)
  - [How to run this code](#how-to-run-this-code)
- [Expected Outcomes](#expected-outcomes)
- [Results](#results)
- [Tags](#tags)

## Define the Problem Statement

Associate travel diary survey smartphone trip traces with Bay Area roadway facilities to enable matching of survey demographics/trip characteristics of users with bridges, express lanes, etc. The script should work with hundreds of thousands, possibly millions of x,y smartphone pings:

    1. Starts with a network, possibly OpenStreetMap, but ideally it could be flexible and accommodate a modeling network (and maybe other networks too)
    2. It also starts with a set of points with x,y values associated with numbered trips (each trip has multiple points associated with it, and has a unique household, person, and trip ID)
    3. The script should match the points to network facility links
    4. Smartphone pings aren't constant, so some facility segments are skipped. The script should fill in interstitial links that were skipped by the list of trip points
    5. The script would probably be in Python, though I personally would love something in R. I don't know if it would use PostGIS/Redshift, or something else to manage the large data files. We're probably open about this.
    6. The script should filter out non-auto modes (otherwise it will include BART trips on routes within freeway medians)
    7. The data include PII

## Project Scope

- **Data Collection** Shimon Israel
- **Data Preparation/ Modeling**  Joshua Croff
- **Data Development**  Joshua Croff
- **Data Analysis / Summary**  Shimon Isreal 

## Project Resources

- [Asana Task](https://app.asana.com/0/304776046055605/1206835675432259/f)
- [Input File Directory on Box](https://mtcdrive.box.com/s/igest7sgigyt24rexyobsbdgr7vrl5ei)
- [Output File Directory on Box](https://mtcdrive.box.com/s/5zo8d8ytesqaqya23os543wkdf29ksfr)

## Data Sources

- [trips.csv (internal access only)](https://mtcdrive.box.com/s/5zo8d8ytesqaqya23os543wkdf29ksfr)
- [locations.csv (internal access only)](https://mtcdrive.box.com/s/j7wrtou0mrlvfio5owj4iia7hfye524c)


### trips schema

| Field Name   | Description                                           | Domain                                                                                   |
|--------------|-------------------------------------------------------|------------------------------------------------------------------------------------------|
| trip_id      | Unique identifier for the trip                        |                                                                                          |
| o_in_region  | Trip originates in region                             | 0: No<br>1: Yes                                                                          |
| d_in_region  | Trip destination in region                            | 0: No<br>1: Yes                                                                          |
| mode_type    | Primary mode used to complete trip                    | 1: Walk<br>2: Bike<br>3: Bikeshare<br>4: Scootershare<br>5: Taxi<br>6: TNC<br>7: Other<br>8: Car<br>9: Careshare<br>10: School bus<br>11: Shuttle/Vanpool<br>12: Ferry<br>13: Transit<br>14: Long Distance Passenger<br>995: Missing Response |
| mode_1       | First mode of travel used to complete trip if multiple modes used | Too many to list                                                                         |
| mode_2       | Second mode of travel used to complete trip if multiple modes used | Too many to list                                                                         |
| mode_3       | Third mode of travel used to complete trip if multiple modes used  | Too many to list                                                                         |
| mode_4       | Fourth mode of travel used to complete trip if multiple modes used | Too many to list                                                                         |

### locations schema
| Field Name   | Description                                           | Domain                                                                                   |
|--------------|-------------------------------------------------------|------------------------------------------------------------------------------------------|
| trip_id      | Unique identifier for the trip                        |                                                                                          |
| collect_time | | |
| accuracy | | |
| bearing | | |
| speed | | |
| lat | Latitude | |
| lon | Longitude | |

## Analysis Parameters

For this project, the following parameters will be used:

- **Network**: OpenStreetMap
- **Network type**: Drive
- **Trips**: Mode Type = Taxi, TNC, Car, Careshare, Shuttle/Vanpool & Origin/Destination in Region

## Methodology

### How to run this code

1. Install the required package dependencies using the [requirements.txt](requirements/requirements.txt) file.
2. Clone the [mappymatch github repository](https://github.com/BayAreaMetro/mappymatch), which has been forked and modified from the original repository.
3. Update the MAPPYMATCH_PATH within [tds_conflation.py](scripts/tds_conflation.py#L13) to point to the location of the cloned repository.
4. Run the [tds_conflation.py](scripts/tds_conflation.py) script by executing `python tds_conflation.py` in the terminal.
   1. If file paths change or need to be updated, update in [config.py](scripts/config.py).

## Expected Outcomes

Provide your expectations (if any) for the results of this work. Your expectations will form the basis for deciding if the work is complete, or if we need to revisit the problem statement and/or refine the methodology used to solve the problem.

## Results

TDS Conflation test results: 
- [Box Link](https://mtcdrive.box.com/s/9vbcd3l6w2kcwo20b1t15j8qic668jkj)
- File path: `/Users/{user}/Library/CloudStorage/Box-Box/DataViz Projects/Spatial Analysis and Mapping/TDS Conflation/Data/tds_conflation_results.gpkg`

Geopackage layers:
- trace_gdf: raw original traces
- trace_line_gdf: line created from gps traces
- matched_gdf: matched links in the network
- matched_path_gdf: full matched path through the network

## Tags

**travel diary survey**, **transportation network**, **conflation**