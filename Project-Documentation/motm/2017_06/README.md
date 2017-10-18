# Year Bay Area Cities will Reach 2040 Housing Targets

The June 2017 map of the month highlights how 2016 housing production compares to the annualized housing forecast from the Draft Plan Bay Area 2040 by identifying how many years it will take cities, at the current rate, to reach the year 2040 forecast. 

[Asana Project](https://app.asana.com/0/229355710745434/362649460499199) 

### Contents 

[Data Sources](#data-sources)  
[Methodology](#methodology)  
[Outcome & Products](#outcome--products)
  - [Maps, Charts, and Graphics](#maps-charts-and-graphics)
  - [Written Material](#written-material)
  - [Feature Classes & CSVs](#feature-classes--csvs)

### Data Sources 

- [California Department of Finance (DOF) E-5 Report - May 2017](http://www.dof.ca.gov/Forecasting/Demographics/Estimates/E-5/)
- [2017 Race to 2040](https://github.com/MetropolitanTransportationCommission/motm/blob/master/2017_06/data/2017%20Race%20to%202040.csv)
- [Bay Area Cities Centroid Shapefile](https://mtcdrive.box.com/s/z22ra13ziuh72soxw0kxzfyatu46oii1)

### Methodology

[2017 Race to 2040](https://github.com/MetropolitanTransportationCommission/motm/blob/master/2017_06/data/2017%20Race%20to%202040.csv) 

[2017 Race to 2040](https://github.com/MetropolitanTransportationCommission/motm/blob/master/2017_06/data/2017%20Race%20to%202040.csv) data was joined with [Bay Area Cities Centroid Shapefile](https://mtcdrive.box.com/s/z22ra13ziuh72soxw0kxzfyatu46oii1) based on jurisdiction name for visualization purposes. 

For each city in the Bay Area:
1. Using DOF data, calculate the number of housing units produced so far (between January 2010 and January 2017).
2. Subtract units produced so far from the 30-year household growth forecast by city from Plan Bay Area 2040. Note that, for simplicity, it is assumed that household growth is equivalent with housing unit growth (a housing unit growth forecast by city is not currently available for Plan Bay Area 2040).
3. Again using DOF data, calculate the housing production rate from 2016 (between January 2016 and January 2017).
4. Divide the numeric result from step 2 by the growth rate from 2016 to calculate the number of years it would take to build the remaining housing if housing production continues to occur at those levels consistently into the future.
5. Add the result from step 4 (the number of years required) to the current year (2017) to calculate the year which the Plan Bay Area 2040 housing goal would be achieved at the current rate of production.

City bubble size is based on the household growth forecast (30-year forecast) for Plan Bay Area 2040.


### Outcome & Products 

#### Maps, Charts, and Graphics 

- [Image Files](https://mtcdrive.box.com/s/hlnfwp1a0rmjxk7haz267it9wicid1aq)
  - [motm_6_23_17.pdf (website)](https://mtcdrive.box.com/s/uqfqn8lermqcxw3mx4zi0ewd6toagj75)
  - [motm_6_23_17.png (website)](https://mtcdrive.box.com/s/boupivq7ruc04pftds1r56i3fchvex3x)
  - [motm_5_20_17_ED.pdf (Executive Director's Report)](https://mtcdrive.box.com/s/cenv8abbuibjrzy1717c1e386p9rx5jk)
    - [motm_5_20_17_ED.png (Executive Director's Report)](https://mtcdrive.box.com/s/266l11vip8699jgysv84x9jp9wci29nl)
- [Illustrator Files](https://mtcdrive.box.com/s/u5kgyyfrxw5gf375ngd9aft4mi1il81o)
- [Commission Presentation Files](https://mtcdrive.box.com/s/pvdcrrhn6h2q2c8uuswl5d937oooeee0)

#### Written Material

[June 2017 Map of the Month Write - Up](https://mtcdrive.app.box.com/file/190357087290) 

#### Feature Classes & CSVs

- [Forcast Shapefiles](https://mtcdrive.box.com/s/z22ra13ziuh72soxw0kxzfyatu46oii1) 