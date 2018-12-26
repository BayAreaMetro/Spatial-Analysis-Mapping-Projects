**Draft Status: Draft**

## CASA Equity Analysis

Identify the geographic impacts of the [CASA Compact](https://mtc.ca.gov/sites/default/files/CASA_Compact.pdf) as adopted by the CASA Technical Committee on December 3, modified before appproval by the CASA Steering Committee on December 12, and authorized for Commission Chair signiature by the MTC on December 19, 2018.

### Project Management

- [Asana Project](https://app.asana.com/0/356840529458476/913179078257017/f)
- [Box](https://mtcdrive.box.com/s/32q1ukuaifx0n7fowwowmsm97gohdtf7)
- [ArcGIS Online](https://mtc.maps.arcgis.com/home/group.html?id=5e22cf0f5f0b44a9ae622f60e52cde2f#overview)

### Contents 

- [Data Sources](#data-sources)
- [Analysis Parameters](#analysis-parameters)
- [Methodology](#methodology)
- [Expected Outcomes](#expected-outcomes)
- [Results](#results)

## Data Sources

- [MTC Communities of Concern]
- [BCDC Communities of Concern]  

Both sources are in turn derived from: 

- [U.S. Census - American Community Survey 2012-2016](https://www.census.gov/programs-surveys/acs/)
- [U.S. Census - TIGER/Line Shapefiles 2016](https://www.census.gov/geo/maps-data/data/tiger-line.html)

## Analysis Parameters

Analysis parameters are definable, measurable, and can contain a constant or variable characteristic, dimension, property, or value, that is selected from a set of data (or population) because it is considered essential to understanding how to solve a problem. List the parameters that you think are required to solve this problem. Leave this blank if you are unsure of how to determine the analysis parameters for your project. The analyst assigned to the project will document this information.

## Methodology

The analysis was performed in R and leverages the censusapi library which is documented here: [CensusAPI](https://hrecht.github.io/censusapi/index.html)

To explore the methodology, take a look at the [CASA Methodology](CASA_acs_vars_lowincomeTenure.Rmd)

## Expected Outcomes

Provide your expectations (if any) for the results of this work. Your expectations will form the basis for deciding if the work is complete, or if we need to revisit the problem statement and/or refine the methodology used to solve the problem.

## Results

Determine how close the solution is to the expected outcome. If the solution is acceptable, the work will be considered complete. If the solution is unacceptable, we will need to refine the problem statement or the methodology implemented to find the solution.
