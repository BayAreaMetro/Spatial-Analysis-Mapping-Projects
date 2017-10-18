library(sf)
library(dplyr)
library(tidyr)

motm_path <- "C:/projects/motm/2017_07"

setwd(motm_path)

# sf_obj_small <- st_read("cb_2016_us_county_20m/cb_2016_us_county_20m.shp",
#                   agr=c(GEOID="identity",ALAND="aggregate"))
sf_obj_medium <- st_read("cb_2016_us_county_5m/cb_2016_us_county_5m.shp",
                  agr=c(GEOID="identity",ALAND="aggregate"))


df_obj <- read.csv("YCOM_2016_Data.01.csv")

#calculate deviation from discussion mean (as in nytimes final map)
national_discuss <- df_obj[df_obj$GeoType=="National",c("discuss")]
df_obj$dscs_dev <- df_obj$discuss - national_discuss

df_obj <- df_obj[df_obj$GeoType=="County",]

#need to reconstruct the yale geoid from scratch
#they used a concatenation of state fips and then county (as strings) 
#and then set the type to integer, dropping a leading 0

library(tidyr)
sf_obj_medium <- tidyr::unite_(as.data.frame(sf_obj_medium), 
                               "y_geoid", 
                               c("STATEFP","COUNTYFP"),
                               sep="")
sf_obj_medium$GEOID <- as.integer(sf_obj_medium$y_geoid)
sf_obj_medium <- st_sf(sf_obj_medium)

no_census_geoid_for_yale_geoid <- sf_obj_medium[!sf_obj_medium$GEOID %in% df_obj$GEOID,]$NAME
no_yale_geoid_for_census_geoid <- df_obj[!df_obj$GEOID %in% sf_obj_medium$GEOID,]$GeoName

lj <- left_join(sf_obj_medium,df_obj, by="GEOID")

lj <- lj[!(st_geometry_type(lj$geometry)=="GEOMETRYCOLLECTION"),]

lj_s <- select(lj,GeoType,GEOID,GeoName,discuss,dscs_dev)

st_write(lj_s,"yale_climate_census_subset_columns.shp",driver="ESRI Shapefile")

strip_vowels <- function(y) {
  if(!y=="geometry"){
    y<-gsub("[aeiouAEIOU]","",y)
  }
  return(y)
}

names(lj) <- sapply(names(lj), FUN=strip_vowels)

st_write(lj,"yale_climate_census_all_columns.shp",driver="ESRI Shapefile")

