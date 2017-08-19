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
