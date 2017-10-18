# Northern California Employment Centers: Employment by Sector 

This month's map of the month highlights employment centers within the 21-county Northern California Mega Region. Employment Centers were defined within built-up areas where there was an employment density of over 5,000 jobs per square mile. Jobs within the Mega Region were broken down by North American Industry Classification System [NAICS economic sector](https://www.census.gov/eos/www/naics/faqs/faqs.html#q5), and were grouped into [7 related classifications](https://github.com/MetropolitanTransportationCommission/motm/blob/master/2017_05/data/MTC_2012_NAICS_Sector_Groups.csv).

[Asana Project](https://app.asana.com/0/152661557501438/350413001908217) 

### Contents 

[Data Sources](#data-sources)  
[Methodology](#methodology)  
[Outcome & Products](#outcome--products)  

### Data Sources 

- [Business Data: Esri;Infogroup 2016](https://mtcdrive.app.box.com/folder/11272654765)
  - *Datasets are licensed and therefor are not to be distributed publicly*
- [FMMP Urban 2014](http://www.conservation.ca.gov/dlrp/fmmp)

### Methodology

#### Northern California Mega Region Employment Density Feature Class 

Two custom tools were created using ArcGIS Pro Model Builder to generate the final output feature class, as well as intermediary feature classes &rasters. The feature class generated highlights employment density within [FMMP Urban and Built Up](http://www.conservation.ca.gov/dlrp/fmmp/mccu/Pages/map_categories.aspx) areas. The toolbox containing the tools is linked below. Input values are maintained as default within the tools.     

**[Select_By_Attr_Create_Point_Density_Raster](https://mtcdrive.box.com/s/ssp8bo255pci5dax5k8gxhs9k4krm04a)**

![Select by Attr Create Point Density Raster Model](https://github.com/MetropolitanTransportationCommission/motm/blob/master/2017_05/readme_images/Screen%20Shot%202017-05-25%20at%2010.54.57%20AM.png)

  **Input:**
  - [NC_Mega_Region_Businesses (Point)](#feature-classes--csvs)

  Environments:   
  - Mask: [NC_Mega_Region_FMMP_Urban_2014_SF (Polygon)](#feature-classes--csvs)
    - Built - up areas 

  **Output:**
  - [NC_Mega_Region_Emp_Density_Urban (Raster)](#feature-classes--csvs)

**[Reclassify_Convert_Raster_to_Polygon](https://mtcdrive.box.com/s/ssp8bo255pci5dax5k8gxhs9k4krm04a)**

![Reclassify Convert Raster to Polygon](https://github.com/MetropolitanTransportationCommission/motm/blob/master/2017_05/readme_images/Screen%20Shot%202017-05-25%20at%2010.57.25%20AM.png) 

  **Input:**
  - [NC_Mega_Region_Emp_Density_Urban (Raster)](#feature-classes--csvs)

  **Output:** 
  - [NC_Mega_Region_Emp_Density_FC (Polygon)](#feature-classes--csvs)

#### Northern California Mega Region Map Charts 

The [Employment_Breakdown_By_Sector.sql](https://github.com/MetropolitanTransportationCommission/motm/blob/master/2017_05/scripts/Employment_Breakdown_By_Sector.sql) script created employment summaries for the [7 related classifications](https://github.com/MetropolitanTransportationCommission/motm/blob/master/2017_05/data/MTC_2012_NAICS_Sector_Groups.csv). These classifications were devised by grouping related [NAICS economic sectors](https://www.census.gov/eos/www/naics/faqs/faqs.html#q5)    

  **Input:**

  - [NC_Mega_Region_Emp_Density_FC (Polygon)](#feature-classes--csvs)  
  - [NC_Mega_Region_Businesses (Point)](#feature-classes--csvs)  

  **Output:**
  
  - [Mega Region Employment Summaries by MTC Classifications](#feature-classes--csvs)  
  - [Mega Region Employment Center Summaries by MTC Classifications](#feature-classes--csvs)   
   
### Outcome & Products

#### Maps, Charts, and Graphics  

- [Image Files](https://mtcdrive.box.com/s/9icb7clcwjb71utccv52cxj78s6iz7aw)
    - [motm_5_20_17.pdf (Website)](https://mtcdrive.box.com/s/fl147feh0z1jh7izyqvrr36aah3t4arv)
    - [motm_5_20_17.png (Website)](https://mtcdrive.box.com/s/daxl8jzuo773ogwkk9bbso1e2xxbhvf3)
    - [motm_5_20_17_ED.pdf (Executive Director's Report)](https://mtcdrive.box.com/s/m3npoh7hmxuaq8wqbcxjq1om1e3gkllr)
    - [motm_5_20_17_ED.png (Executive Director's Report)](https://mtcdrive.box.com/s/dskntktinejb1d4jo6bjd6o512ibk3vd)
- [Illustrator Files](https://mtcdrive.box.com/s/09b22d2b44w3daehm8slg3fseo8023zj)
- [Commission Presentation Files](https://mtcdrive.box.com/s/bplrppfwwd4mbj4cia648xxvsogoxbgq)

#### Written Material 

[May 2017 Map of the Month Write-Up](https://mtcdrive.box.com/s/go4wg1ke7mzh8rjvf4kkf9xu0ie1p64h) 

#### Feature Classes & CSVs 

- [Mega Region Analysis FGDB](https://mtcdrive.box.com/s/3cdm9n0g6e1k5bsz7428zp52aqa2jc4x)

    Contents: 
    - NC_Mega_Region_Businesses (Point)
    - NC_Mega_Region (Polygon)
    - NC_Mega_Region_Emp_Density_FC (Polygon)
    - NC_Mega_Region_FMMP_Urban_2014_SF (Polygon)
    - NC_Mega_Region_Emp_Density_Urban (Raster)
    - NC_Mega_Region_Emp_Density_Urb_RC (Raster)

- [Mega Region Employment Summaries by MTC Classifications](https://github.com/MetropolitanTransportationCommission/motm/blob/master/2017_05/data/2016_NC_Mega_Region_Employment.csv)
- [Mega Region Employment Center Summaries by MTC Classifications](https://github.com/MetropolitanTransportationCommission/motm/blob/master/2017_05/data/2016_NC_Mega_Region_Emp_Center_Employment.csv)





