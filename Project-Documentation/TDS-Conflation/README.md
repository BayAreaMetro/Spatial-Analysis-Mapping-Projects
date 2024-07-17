-- Draft --
# Travel Diary Survey Conflation

### Table of Contents

- [Travel Diary Survey Conflation](#travel-diary-survey-conflation)
    - [Table of Contents](#table-of-contents)
  - [Define the Problem Statement](#define-the-problem-statement)
  - [Project Scope](#project-scope)
  - [Project Resources](#project-resources)
  - [Data Sources](#data-sources)
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

List the potential data sources that you think are required to solve the problem. If you are unsure, you can discuss these with the Unit Manager prior to submitting your request for support.

## Analysis Parameters

Analysis parameters are elements from the data as well as additional definitions or features that will be used in your analysis. For example, in a geospatial intersection area analysis, these would be the geometries of the base layer and overlay, and could optionally include a buffer distance or overlay category. Generally, think of analysis parameters as the most important aspects of the data that you are using to answer the questions driving your analysis. If your analysis parameters include definitions, be sure to describe these in your documentation or link to their documentation. For example, if Transit Priority Areas (TPAs) are one of your analysis parameters, give a short description of a TPA and link to the authoritative public resource on TPAs. These repositories have some example Analysis Parameters:

- [Communities of Concern](https://github.com/BayAreaMetro/Spatial-Analysis-Mapping-Projects/tree/master/Project-Documentation/Communities-of-Concern)
- [CASA](https://github.com/BayAreaMetro/Spatial-Analysis-Mapping-Projects/tree/master/Project-Documentation/CASA)

## Methodology

### How to run this code

1. Install the required package dependencies using the [requirements.txt](requirements/requirements.txt) file.
2. Clone the [mappymatch github repository](https://github.com/BayAreaMetro/mappymatch), which has been forked and modified from the original repository.
3. Update the MAPPYMATCH_PATH within [tds_conflation.py](tds_conflation.py#L13) to point to the location of the cloned repository.
4. Run the [tds_conflation.py](tds_conflation.py) script by executing `python tds_conflation.py` in the terminal.

The analyst assigned to the project will document this information. The analyst will review the methodology (if applicable) with the project team to ensure that it meets the requirements and expectations of the solution or problem.

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