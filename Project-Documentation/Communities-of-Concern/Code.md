# Communities of Concern 2018

This script builds the 2016 Community of Concern Dataset using the presribed methodology located here:   [GitHub Documentation](https://github.com/BayAreaMetro/Spatial-Analysis-Mapping-Projects/tree/master/Project-Documentation/Communities-of-Concern). 

It uses the censusapi library which is documented here: [CensusAPI](https://hrecht.github.io/censusapi/index.html)

```{r message=FALSE, warning=FALSE}
library(censusapi)
library(readr)
library(dplyr)
#Community of Concern Spatial Processing
library(censusapi)
library(readr)
library(dplyr)
### Install Mapping Libraries
# install.packages("leaflet")
# install.packages("rgdal")
# install.packages("geojsonio")
# install.packages("spdplyr")
# install.packages("rmapshaper")
# install.packages("jsonlite")
library(leaflet)
library(jsonlite)
library(rgdal)
library(geojsonio)
library(spdplyr)
library(rmapshaper)

setwd("~/Documents/Github_Documentation/Spatial-Analysis-Mapping-Projects/Project-Documentation/Communities-of-Concern/Data")
#This key is private and should not be shared via GitHub.  This portion of the code should be removed when sharing to Github.
Sys.getenv("CENSUS_TOKEN")
# Add key to .Renviron
Sys.setenv(CENSUS_KEY='Your Key here')
# Reload .Renviron
readRenviron("~/.Renviron")
# Check to see that the expected key is output in your R console
Sys.getenv("CENSUS_KEY")
#Provides list of APIs 
apis <- listCensusApis()
```

```{r message=FALSE, warning=FALSE}
ACS_COC_SelectedVars <- read_csv("~/Documents/Github_Documentation/Spatial-Analysis-Mapping-Projects/Project-Documentation/Communities-of-Concern/Data/ACS_Table_Variables_COC_Factors.csv")
acs_vars <- ACS_COC_SelectedVars$ACS_Table_Variable
#rm(selectedData)
selectedData <- getCensus(name="acs5", vintage=2014,
                          vars=acs_vars, 
                          region="tract:*", 
                          regionin="state:06+county:001,013,041,055,075,081,085,095,097")
head(selectedData)
```

#### Calculate COC variables from selectedData

```{r message=FALSE, warning=FALSE}
selectedData$GEOID <- paste(selectedData$state,selectedData$county,selectedData$tract,sep="")
selectedData$STATE <- selectedData$state
selectedData$COUNTY_FIPS <- selectedData$county
selectedData$TRACT <- selectedData$tract
selectedData$TOT_POP_MIN <- selectedData$B03002_001E 
selectedData$TOT_POP_SEN <- selectedData$B01001_001E
selectedData$TOT_POP_POV <- selectedData$C17002_001E
selectedData$TOT_POP_CIV_NI <- selectedData$C18108_001E
selectedData$TOT_HH <- selectedData$B08201_001E
selectedData$TOT_FAM_CHILD <- selectedData$B11004_003E + selectedData$B11004_010E + selectedData$B11004_016E
selectedData$TOT_POP_OVER5 <- selectedData$B16005_001E
selectedData$TOT_RENT_OCC_HOUS <- selectedData$B25070_001E
selectedData$POP_MINORITY <- selectedData$B03002_001E - selectedData$B03002_003E
selectedData$POP_OVER75 <- selectedData$B01001_023E + selectedData$B01001_024E + selectedData$B01001_025E + selectedData$B01001_047E + selectedData$B01001_048E + selectedData$B01001_049E
selectedData$POP_SPFAM <- selectedData$B11004_010E + selectedData$B11004_016E
selectedData$POP_LEP<- selectedData$B16005_007E + selectedData$B16005_008E + selectedData$B16005_012E + selectedData$B16005_013E + selectedData$B16005_017E + selectedData$B16005_018E + selectedData$B16005_022E + selectedData$B16005_023E + selectedData$B16005_029E + selectedData$B16005_030E + selectedData$B16005_034E + selectedData$B16005_035E + selectedData$B16005_039E + selectedData$B16005_040E + selectedData$B16005_044E + selectedData$B16005_045E
selectedData$POP_BELOW200 <- selectedData$C17002_001E - selectedData$C17002_008E
selectedData$POP_DISABILITY <- selectedData$C18108_001E - (selectedData$C18108_005E + selectedData$C18108_009E + selectedData$C18108_013E)
selectedData$POP_HUS_RENT50 <- selectedData$B25070_010E
selectedData$POP_ZVHHS <- selectedData$B08201_002E
selectedData$PCT_OVER75 <- (selectedData$B01001_023E + selectedData$B01001_024E + selectedData$B01001_025E + selectedData$B01001_047E + selectedData$B01001_048E + selectedData$B01001_049E)/selectedData$B01001_001E
selectedData$PCT_MINORITY <- (selectedData$B03002_001E - selectedData$B03002_003E)/selectedData$B03002_001E
selectedData$PCT_SPFAM <- (selectedData$B11004_010E + selectedData$B11004_016E)/(selectedData$B11004_003E + selectedData$B11004_010E + selectedData$B11004_016E)
selectedData$PCT_LEP <- (selectedData$B16005_007E + selectedData$B16005_008E + selectedData$B16005_012E + selectedData$B16005_013E + selectedData$B16005_017E + selectedData$B16005_018E + selectedData$B16005_022E + selectedData$B16005_023E + selectedData$B16005_029E + selectedData$B16005_030E + selectedData$B16005_034E + selectedData$B16005_035E + selectedData$B16005_039E + selectedData$B16005_040E + selectedData$B16005_044E + selectedData$B16005_045E)/selectedData$B16005_001E
selectedData$PCT_BELOW200 <- (selectedData$C17002_001E - selectedData$C17002_008E)/selectedData$C17002_001E
selectedData$PCT_DISAB <- (selectedData$C18108_001E - (selectedData$C18108_005E + selectedData$C18108_009E + selectedData$C18108_013E))/selectedData$C18108_001E
selectedData$PCT_ZVHHS <- selectedData$B08201_002E/selectedData$B08201_001E
selectedData$PCT_HUS_RENT50 <- selectedData$B25070_010E/selectedData$B25070_001E
```

#### Logic flagging Disadvantage Factors
```{r}
selectedData$OVER75_10 <- ifelse(selectedData$PCT_OVER75 > .10,1,0)
selectedData$MINORITY_70 <- ifelse(selectedData$PCT_MINORITY > .70,1,0)
selectedData$SPFAM_20 <- ifelse(selectedData$PCT_SPFAM > .20,1,0)
selectedData$DISAB_25 <- ifelse(selectedData$PCT_DISAB > .25,1,0)
selectedData$LEP_20 <- ifelse(selectedData$PCT_LEP > .20,1,0)
selectedData$BELOW200_30 <- ifelse(selectedData$PCT_BELOW200 > .30,1,0)
selectedData$ZVHH_10 <- ifelse(selectedData$PCT_ZVHHS > .10,1,0)
selectedData$HUS_RENT50_15 <- ifelse(selectedData$PCT_HUS_RENT50 > .15,1,0)
```
#### Assignment Option using mutate
```{r}
#selectedData %>%
  #mutate(OVER75_10 = ifelse(PCT_OVER75 > .10,1,0)) %>%
  #mutate(MINORITY_70 = ifelse(PCT_MINORITY > .70,1,0)) %>%
  #mutate(SPFAM_20 = ifelse(PCT_SPFAM > .20,1,0)) %>%
  #mutate(DISAB_25 = ifelse(PCT_DISAB > .25,1,0)) %>%
  #mutate(LEP_20 = ifelse(PCT_LEP > .20,1,0)) %>%
  #mutate(BELOW200_30 = ifelse(PCT_BELOW200 > .30,1,0)) %>%
  #mutate(ZVHH_10 = ifelse(PCT_ZVHHS > .10,1,0)) %>%
  #mutate(HUS_RENT50_15 = ifelse(PCT_HUS_RENT50 > .15,1,0)) -> selectedData
```

#### Logic flagging Factors other than Minority or Low Income
```{r}
selectedData$Count_DisadFact <- selectedData$OVER75_10 + selectedData$SPFAM_20 + selectedData$DISAB_25 + selectedData$LEP_20 + selectedData$ZVHH_10 + selectedData$HUS_RENT50_15 
```
#### Logic flagging COCs
```{r}
selectedData$COC_FLAG_2014 <- ifelse((selectedData$MINORITY_70 == 1 & selectedData$BELOW200_30 == 1) | (selectedData$BELOW200_30 == 1 & selectedData$Count_DisadFact >= 3),1,0)
```

```{r}
 FinalTable <- selectedData[,43:80]
write.csv(FinalTable, "~/Documents/Github_Documentation/Spatial-Analysis-Mapping-Projects/Project-Documentation/Communities-of-Concern/Data/COCs_2014_tbl_ACS5.csv")
```

### Mapping Libraries
There are a few examples out there.  Here are a few that I think are useful when working with Census Data.  
    1. https://randomjohn.github.io/r-maps-with-census-data/  
    2. https://juliasilge.com/blog/using-tidycensus/
    3. https://walkerke.github.io/2017/06/comparing-metros/
    
```{r}
urban_tracts <- readOGR(dsn=path.expand("~/Documents/Data/COCs"), 
                  layer = "COCs_2016", verbose = FALSE)
ca_tracts <- readOGR(dsn=path.expand("~/Documents/Data/"), 
                     layer = "CA_Tracts", verbose = FALSE)
# Rename a column name GEOID to county_id.
ca_tracts <- ca_tracts %>% rename(GEOID = CODE)
ca_tracts %>%
  select(GEOID) -> ca_tracts
ca_tracts$GEOID <- sub('840','',ca_tracts$GEOID)
ca_tracts <- ca_tracts[,5]

#Add CountyFip using GEOID to ca_tracts
ca_tracts$COUNTYFIP <- as.numeric(substr(ca_tracts$GEOID, 2, 5))
ca_tracts$GEOID <- as.character(ca_tracts$GEOID)

#Fitler to Bay Area Tracts
ca_tracts %>%
  filter(COUNTYFIP %in% c(6001, 6013, 6041, 6055, 6075, 6081, 6085, 6095, 6097)) -> bay_tracts

#Add CountyFIp using GEOID
urban_tracts <- urban_tracts[,1:2]
urban_tracts$CountyFIP <- as.numeric(substr(urban_tracts$GEOID, 2, 5))
#Add Tracts using GEOID
urban_tracts$TRACT <- as.numeric(substr(urban_tracts$GEOID, 6, 11))
urban_tracts$TRACT <- as.character(urban_tracts$TRACT)
urban_tracts$GEOID <- as.character(urban_tracts$GEOID)

# Merge Final Table with Geography
urban_tracts@data <- right_join(urban_tracts@data,FinalTable, by="GEOID")
bay_tracts@data <- right_join(bay_tracts@data,FinalTable, by="GEOID")

#Fix NaN values.  For some reason these values show up in the tables from the merged FinalTable.
urban_tracts@data <- replace(urban_tracts@data, is.na(urban_tracts@data), 0)
bay_tracts@data <- replace(bay_tracts@data, is.na(bay_tracts@data), 0)

# Convert SP Data Frame to GeoJSON.
tracts_json <- geojson_json(urban_tracts)
bay_tracts_json <- geojson_json(bay_tracts)

# Save it to a local file system.
#geojson format
geojson_write(bay_tracts_json, file = "~/Documents/Data/Bay_Tracts.geojson")
geojson_write(tracts_json, file = "~/Documents/Data/COC_Urban_Tracts.geojson")
# Shapefile format.  Change the folder location on local system (if needed)
writeOGR(urban_tracts, "finaldata", "~/Documents/Data/Urban_Tracts", driver = "ESRI Shapefile")
writeOGR(bay_tracts, "finaldata", "~/Documents/Data/Bay_Tracts", driver = "ESRI Shapefile")
```
### Aggregate Summary Section

```{r}
#Example Calculations to summarize

FinalTable %>%
  filter(COC_FLAG_2014 == 1) -> cocs


COC_2014_DF_Summary_Region <-  setNames(aggregate( cocs$POP_MINORITY,
            cocs$POP_BELOW200, 
            cocs$POP_LEP, 
            cocs$POP_ZVHHS, 
            cocs$POP_OVER75, 
            cocs$POP_DISABILITY, 
            cocs$POP_SPFAM, 
            cocs$POP_HUS_RENT50,
            cocs$TOT_POP_MIN,
            by=list(
                    cocs$POP_MINORITY,
            cocs$POP_BELOW200, 
            cocs$POP_LEP, 
            cocs$POP_ZVHHS, 
            cocs$POP_OVER75, 
            cocs$POP_DISABILITY, 
            cocs$POP_SPFAM, 
            cocs$POP_HUS_RENT50,
            cocs$TOT_POP_MIN ), FUN=sum), c("Minority","Low Income","Limited English Proficiency","Zero Vehicle Households","Seniors","People with a Disability","Single Parent Family","Severely Rent Burdened Household","Total Population")) 
```
