# US Population Growth Disparity - Net Population Change 2000 - 2016

[Asana Project](https://app.asana.com/0/229355710745434/387468480023035) 

### Goal 

Reproduce the map featured on this page of a report:
![Report_Map](https://github.com/BayAreaMetro/motm/blob/master/2017_09/readme_images/NetPopulationChange2000_2016.png)

### Contents 

[Data Sources](#data-sources)  
[Methodology](#methodology)  
[Outcome & Products](#outcome--products)
  - [Maps, Charts, and Graphics](#maps-charts-and-graphics)
  - [Written Material](#written-material)
  - [Feature Classes & CSVs](#feature-classes--csvs)

### Data Sources 

**2000 US County Census Estimates SF1** 
- [Decennial Census API](https://www.census.gov/data/developers/data-sets/decennial-census.html)

**2016 US County Census Population Estimates** 
- [Population Estimates and Projections API](https://www.census.gov/data/developers/data-sets/popest-popproj/popest.html)
- [2010 TIGER/Line County Shapefile](https://www.census.gov/geo/maps-data/data/tiger-line.html)

### Methodology

[US Population Growth Disparity Python Script](https://github.com/BayAreaMetro/motm/blob/master/2017_09/scripts/US_Population_Growth_Disparity.py)

   1. Pulled 2000 county population data from [Decennial Census API](#decennial-census-api) & 2016 population esimates from [PopulationEstimates and Projections API](#population-esimates-and-projections-api) 
   2. Convert to pandas dataframe (DF)
   3. Join 2000 Census Population DF with 2016 Census Population Estimate DF
   4. Calculate net different of population between 2016 and 2000
   5. Export to excel table 
   6. Join table to [2010 TIGER/Line County Shapefile](#data-sources)

### Outcome & Products 

#### Maps, Charts, and Graphics

- [Image Files](https://mtcdrive.box.com/s/3z6bgbt1xihziovv491jpg4xef2p3u6e)
  - [motm_9_19_17.pdf (Website Version)](https://mtcdrive.box.com/s/ej7rbba7uutjhyznpl1jrzopk2t2utgs)
  - [motm_9_19_17.png (Website Version)](https://mtcdrive.box.com/s/7ithhg89h40sq7x7hkhe6iz5bxz5vukf)
  - [motm_9_19_17_ED.pdf (Executive Director's Report Version)](https://mtcdrive.box.com/s/v1dpdep9olijdms5z8b7wi2rpv7rdww9)
    - [motm_9_19_17_ED.png (Executive Director's Report Version)](https://mtcdrive.box.com/s/n4pinmotfy38lmqxtm0oy70kexoppdqe)
- [Illustrator Files](https://mtcdrive.box.com/s/9lls3kca7dn4vp4hz119kkb68dmac7k9)
- [Commission Presentation Files](https://mtcdrive.box.com/s/s7lo1d2rmheijsedvzab3r29pybdvnq6) 

#### Written Material 

[September 2017 Map of the Month Write-Up](https://mtcdrive.box.com/s/asi7xfz06juw4h2zo9gsylss0piqqxfj)

#### Feature Classes & CSVs 

- [Population Change 2000 - 2016 Census](https://github.com/BayAreaMetro/motm/blob/master/2017_09/data/Population_Change_2000_2016_Census.csv) 