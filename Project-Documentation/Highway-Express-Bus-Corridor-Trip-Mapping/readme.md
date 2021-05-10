# Bay Area Highway Express Bus Corridor Trip Mapping

Summarize express bus trip by highway and interstate corridors leveraging pre-pandemic transit schedules.

## Project Resources

- [Asana Task](https://app.asana.com/0/229355710745434/1199509677196413)
- [Project Box Directory](https://mtcdrive.box.com/s/yak7dsknysgwm4jnqtx4m0heu39xf4wy)

### Table of Contents

- [Data Sources](#data-sources)
- [Analysis Parameters](#analysis-parameters)
- [Methodology](#methodology)
- [Expected Outcomes](#expected-outcomes)
- [Results](#results)
- [Tags](#tags)

## Data Sources

- [SF Bay Area 511 GTFS Regional Feed- Downloaded January 2020](https://511.org/open-data/transit)
- TomTom Road Network Data (2019) - Dataset is not publicly available
- [CalTrans HOV Lanes](https://gisdata-caltrans.opendata.arcgis.com/datasets/aea15307150f4463909d5cc1b8da6232_0?geometry=-124.901%2C36.970%2C-119.627%2C37.735)
- [CalTrans Express Lanes](https://gisdata-caltrans.opendata.arcgis.com/datasets/f42004e4069744d5830e39424225ae59_0?geometry=-140.653%2C32.216%2C-98.466%2C38.482)

## Analysis Parameters

### Peak Period
For the purposes of this analysis, we define peak period as the morning peak period from 5:00 AM to 10:00 AM

### Pre-pandemic transit service
For the purposes of the analysis, we define pre-pandemic transit service as service available in January 2020

### Weekday service 
Weekday service is represented as a typical non-holiday weekday. The schedules analyzied for this analysis were the schedules for 01/06/2020. 

## Methodology

**[Better Bus Buffers - Count Trips on Lines Documentation](https://github.com/Esri/public-transit-tools/blob/master/better-bus-buffers/UsersGuide.md#CountTripsOnLines)**

[Preprocessing of GTFS](https://github.com/Esri/public-transit-tools/blob/master/better-bus-buffers/UsersGuide.md#running-preprocess-gtfs) and [blank stop times interpolation](https://github.com/Esri/public-transit-tools/blob/master/interpolate-blank-stop-times/UsersGuide.md) was run for a previous analysis. the SQLLite databases were coppied into this project's directory and re-used. 

The high-level methodology provided below is a summary of all processing steps executed in the [Count Trips on Lines January 2020 Python Jupyter Notebook](Count_Trips_on_Lines_January_2020.ipynb). To successfully run the notebook, download the [ArcGIS Pro Project](https://mtcdrive.box.com/s/yak7dsknysgwm4jnqtx4m0heu39xf4wy) and run the Jupyter Notebook within the ArcGIS Pro environment. The code will not work in a stand-alone environment as it relies on layer objects that are automatically added to the map when a geoprocessing function is run. 

1. Preprocess transit lines using January 2020 GTFS data
2. Count trips on lines without combining routes for am peak period and for all-day period
3. Summarize by route and number of trips to get max trips per route during am period and all-day period
4. Generate pretty transit routes from routes.txt data 
5. Delete identical routes by route_id and shape
6. For routes with duplicate route_id, keep longest route line
    - Project pretty route lines to WGS84 UTM Zone 10 North
    - Summarize routes by route_id and max length
    - Join summary table to routes table 
    - Select routes w/ count > 1 and length <> max length and delete
    - Unjoin summary table
7. Join pretty routes and average trips per route table 
8. Create highway and interstate corridors
    - Project highway and interstate data to WGS84 UTM Zone 10 North
    - Buffer highway and interstate data by 50 meters and dissolve
    - Select junctions from highway and interstate data and create new feature class
    - Buffer junctions by 100 meters
    - Using editing tools, select all buffered junctions as input and highway and interstate features as target. Split and save edits. (This is a manual process- no arcpy geoprocessing tools available). 
9. Summarize transit trips within each highway and interstate corridor (**See notes below**)
    - Spatially-join express route trips to corridors
    - Summarize am peak period and all day trip counts by corridor
    - Join route trip summary table to highway corridor buffers
10. Create centerline from polygon highway corridor summary areas  

## Expected Outcomes

- Regional Maps of Express Bus Trips Summarized by Corridor for AM Peak Period and All-Day Period
    - Transit line symbols should be thicker for corridors with higher trip counts and thinner for lower and grouped into 4 buckets.  
    - Transit line symbol colors should be different depending on trip counts. 
    - HOV and Express Lanes should be on the map. 

## Results

- [Express Bus Trips AM Peak](https://mtcdrive.box.com/s/d31tu2r2j65k5miyanhkhdz6kx2mnam9)
- [Express Bus Trips All Day Period](https://mtcdrive.box.com/s/sgyolg8s3vzwo17q189aj7iwdteis2gs)
