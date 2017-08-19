# ETL Data Processing for InfoGroup Business Datasets 

### Problem Statement

Build scripts for processing InfoGroup Business datasets. 

### Data Sources
These datasets are private and only accessible by MTC staff.

- [Business Analyst Business Data](https://mtcdrive.box.com/s/oyj6twno0gjtp3y6w2nswq5xak4qltju)
- [TomTom County Boundaries](https://mtcdrive.box.com/s/5k8kbwbdpz7kt2udsfh357nkvcp3stw1) | Password Protected dataset.  See a member of the Data and Visualization team to gain access to this dataset.



### Methodology

Prepare R Script to select and extract the datasets by county.

- [etl.R](#etl.R)  

```
# Documents and Help: http://rhodyrstats.org/geospatial_with_sf/geospatial_with_sf.html

library(sf)
library(dplyr)
library(rgeos)
library(rgdal)
library(sp)

#Set working Directory
setwd("~/Documents/GIS Data/")
#Read Business into DF
CA_Businesses <- st_read("BA_2016/BA_CA_2016.gdb")

#Read Counties into DF
Ca <- st_read("TomTom/2015_12/mn_a8.shp")

# Select a single county
Alameda_Co <- subset(Ca, Ca$CountyFIP == 1)

# Match geom proj(crs) of features
Alameda_Co <-st_transform(Alameda_Co,st_crs(CA_Businesses))

# create overlay index using point in poly or intersection of features
search_index <- st_intersects(Alameda_Co, CA_Businesses, sparse = FALSE)

# apply index of features to subset the
Ala_Bus <- CA_Businesses[search_index,]

#plot(Ala_Bus$Shape, col = Ala_Bus$CITY)

write.csv(Ala_Bus, file = "Ala_Bus.csv")  

```

Example ArcGIS Pro python script that accomplishes the same task as above.

```
arcpy.management.MakeFeatureLayer(r"\\Mac\Home\Documents\GIS Data\TomTom\2015_12\TomTom_CA.gdb\mn_a8", "input_county", "CountyFIP = 1", None)
arcpy.analysis.Intersect(r"input_county #;'\\Mac\Home\Documents\GIS Data\BA_2016\BA_CA_2016.gdb\ca_businesses' #", r"\\Mac\Home\Documents\GIS Data\Data Processing\Ala_Bus.shp", "ALL", None, "POINT")
arcpy.management.CopyRows(r"\\Mac\Home\Documents\GIS Data\Data Processing\Ala_Bus.shp", r"\\Mac\Home\Documents\GIS Data\TomTom\2015_12\Alameda_Bus.csv", None)  

```

### Outcome 
Generate csv output that contains the business within Alameda County.

- [Ala_Bus.csv](https://mtcdrive.app.box.com/folder/11272654765) | Accessible by MTC Staff Only.
