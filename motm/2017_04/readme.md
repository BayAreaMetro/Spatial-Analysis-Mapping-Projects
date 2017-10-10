*April, 2017*

# Good Schools and Affordable Homes

This month's map of the month was inspired by a recent article published by in the New York Times. The original article is linked below. Additionally, a link to Asana is provided to track the project's status.   

[NYT Original Article](https://www.nytimes.com/interactive/2017/03/30/upshot/good-schools-affordable-homes-suburban-sweet-spots.html)  

[Asana Project](https://app.asana.com/0/152661557501438/319130360517993)

## Map of the Month Collateral 

All Map of the Month products, including illustrator, image, presentation, and write up files can be found in the [MOTM_Uploads - 2017_04](https://mtcdrive.box.com/s/dqgewnk6t2boon0hq0h8hjke7y7z63p1) directory on Box. 


## Data Sources  

### San Francisco Metro Area chart (NYT)     

##### Input

- [Grade, Commute, Home Price Data](https://mtcdrive.box.com/s/plb0jfn0vnshdpub1vpuxsh7k6vwajb7) - from the HTML source of the NYT article above.  

- [Stanford School District Data](http://mtc.maps.arcgis.com/home/item.html?id=53f98257229b49c1a0f53447bff434c8). The same data also in [this FileGDB](https://mtcdrive.box.com/s/kfkna9wcmkhgmtbocu0l3tobks6gb32r) as `stanford_schools_data`.   

Note that we used the Stanford School geometries rather than ESRI geometries because there were at least 2x more matches with the data. Apparently the Stanford School data district_nces code as used in NYT does not link automagically with the ESRI geometries. Stanford seems to have processed the geometries into more detailed subsets. 

##### Output 

- Above inputs are joined together and named `nyt_join_2013_unified` in the FileGDB [here]( https://mtcdrive.box.com/s/kfkna9wcmkhgmtbocu0l3tobks6gb32r)  NOTE-THE EPSG of that data is 3857. 

headers:   

- `gsmean_poo` = e.g. 1 grade ahead    
- `district_n` = school district  
- `mean_commu` = mean commute time  

These are basically all the variables of interest.  

### NYT Primary Data Sources

#### Stanford Schools Project

##### Input  

- [Stanford School District Data](http://mtc.maps.arcgis.com/home/item.html?id=53f98257229b49c1a0f53447bff434c8). The same data also in [this FileGDB](https://mtcdrive.box.com/s/kfkna9wcmkhgmtbocu0l3tobks6gb32r) as `stanford_schools_data`.   

- [schools_ca.csv](https://mtcdrive.box.com/s/2n4jzdo300bw18vqs54091f11jwn9f00) From [this csv](https://stacks.stanford.edu/file/druid:db586ns4974/district%20means%20grade%20equivalent%20std%20(gs)%20(pooled%20year,%20grade%20and%20sub)_v1_1.csv) from the [Stanford Schools Data Archive](https://cepa.stanford.edu/seda/data-archive).  See this link for the [metadata](https://stacks.stanford.edu/file/druid:db586ns4974/codebook_achievement_v1point1.xlsx).   

##### Output  

- [AGOL Feature Class](http://mtc.maps.arcgis.com/home/item.html?id=793ddad43053421a9a620fa45a1279e7)  

Also copied in [this GDB](https://mtcdrive.box.com/s/wvoye1h9e1o6mhcrfxh3lccqrxp9euch) as `stanford_schools_data`  

[Processing Script](https://github.com/MetropolitanTransportationCommission/motm/blob/master/2017_04/scripts/join_agol_schools_to_stanford.py)   

#### Redfin/Places  

##### Input   

- `Census Places geometries` (ESRI) on AGOL [here](http://mtc.maps.arcgis.com/home/item.html?id=fa734bd049604d50a62dd204389d2c31) The same data are also subset in [this FileGDB](https://mtcdrive.box.com/s/wvoye1h9e1o6mhcrfxh3lccqrxp9euch) as `esri_places_geometries_bay_area`]    

- `Redfin Data Export` as subset in [this](https://github.com/MetropolitanTransportationCommission/motm/blob/master/2017_04/data/places_redfin_ca_feb_2017_all_property_types.csv) CSV to Places in california in February, 2017. The source for this subset is this full CSV [here](https://mtcdrive.box.com/s/dt1uinv3lc12phtpp0be3k4udsenixx8) as exported from the Redfin Data Center TDE File.  

##### Output  

- [AGOL Feature Class](http://mtc.maps.arcgis.com/home/item.html?id=7e844734bea04efebe38420746cbae6a)   

[Processing Script](https://github.com/MetropolitanTransportationCommission/motm/blob/master/2017_04/scripts/join_places_to_redfin.py)    

#### Commute Data

##### Input  

- [Vital Signs API](http://data.vitalsigns.mtc.ca.gov/api/t3/city)   

Should be joined to:  

- `Census Places geometries` (ESRI) on AGOL [here](http://mtc.maps.arcgis.com/home/item.html?id=fa734bd049604d50a62dd204389d2c31).  The same data are also subset in [this FileGDB](https://mtcdrive.box.com/s/wvoye1h9e1o6mhcrfxh3lccqrxp9euch) as `esri_places_geometries_bay_area`]   

##### Output  

## Analysis 

The output table `nyt_join_2013_unified` referenced above in the data sources section was analyzed using tsql. 

School districts with the following characteristics were selected: 
- Median per sf home price below Bay Area Average 
- School district performance above Bay Area Average
- Mean commute less than 30 minutes

Script:

[2017_04_motm_analysis.sql](https://github.com/MetropolitanTransportationCommission/motm/tree/master/2017_04/scripts/2017_04_motm_analysis.sql) 




