**Draft Status: Draft**

# Transit Oriented Communities

The Transit Oriented Communities (TOC) policy aims to increase residential and commercial densities in eligible Transit-Rich Areas (TRAs), prioritizing affordable housing and commercial development in areas near regional transit hubs served by multiple transit providers. The primary goal of this project is identify areas where the TOC policy applies. The secondary goal is to assess the baseline zoning for residential and office/commercial within Priority Development Areas (PDAs) and Transit Rich Areas (TRAs) within 1/2 mile of existing or planned fixed-guideway transit facilities. 

## Project Management 

- [Asana Task (MTC Only)](https://app.asana.com/0/304776046055605/1202042875475784/f)
- [Box Link (MTC Only)](https://mtcdrive.box.com/s/z4gzf4maxwrl25a6pelu0bjzlb8mc5a4)

## Table of Contents

- [Analysis Parameters](#analysis-parameters)
    - [Transit Oriented Communities Policy Area](#transit-oriented-communities-policy-area)
        - [Where will the TOC policy apply?](#where-will-the-toc-policy-apply)
        - [Where will the TOC policy not apply?](#where-will-the-toc-policy-not-apply)
        - [How will densities for new residential and commercial development be determined?](#how-will-densities-for-new-residential-and-commercial-development-be-determined)
- [Methodology](#methodology)
    - [Create Transit Oriented Communities Policy Area](#create-transit-oriented-communities-policy-area)
    - [Transit Oriented Communities Parcel/Land Use Overlay (Not completed)](#transit-oriented-communities-parcelland-use-overlay)

## Analysis Parameters

### Transit Oriented Communities Policy Area

#### Where will the TOC policy apply?

The proposed TOC policy will apply in the follow areas:

- within the half-mile station/stop/terminal area of existing or planned **fixed-guideway transit**. 
- Fixed-guideway transit:
    - Regional rail: BART, Caltrain
    - Light Rail Transit: Muni Metro, VTA
    - Bus Rapid Transit: AC Transit (1T) Tempo, Van Ness BRT
    - Commuter rail: Capitol Corridor, ACE, SMART
    - Ferry terminals (limited to certain requirements only)

#### Where will the TOC policy not apply?

The TOC policy will not apply around airport air tram stations, including stations at San Francisco International Airport and at Oakland International Airport. Additionally, the policy **only** applies to areas within 1/2 mile of existing or planned fixed guideway transit service (regional rail, light rail, commuter rail, ferry, and bus rapid transit). In the case of planned service, only projects that are deemed likely to be delivered within the near-term (roughly 5 years) should be considered. As such, stops or stations associated with the following projects were excluded from analysis. Additionally, given its limited capacity, stations served only by Tideline Ferry service were also excluded from analysis.

| Project Name | Pba50_ID | agency_id | stop_id |
|---|---|---|---|
| Hovercraft pilot (not included in shapefile so OK) |  |   |
| Small-scale ferry | CC-021 |   |
| Tideline ferry |  | TD |
| SF historic streetcar extension | SF-024 |   |
| ReX blue | MU-060 |   |
| ReX green | MU-061 |   |
| ReX red | MU-062 |   |
| 23rd St BRT | CC-015 |   |
| Geneva-Harney BRT | SF-012 |   |
| Geary Phase 1 (not tagged in shapefile as BRT so OK) |   |   |
| Geary Phase 2 | SF-011 |   |
| El Camino San Mateo | SM-011 |   |
| El Camino Santa Clara (not tagged in shapefile as BRT so OK) |   |   |
| Telegraph | MU-033 |   |
| Appezzato Way | AL-016 |   |
| BRT to Brentwood | CC-018 |   |
| | |SI| SI:GA   |
| | |SI| SI:GG |
| | |SI| SI:HOT |
| | |SI| SI:ITA |
| | |SI| SI:ITG |
| | |SI| SI:RCC |
| | |SI| SI:T1 |
| | |SI| SI:T2 |
| | |SI| SI:T3 |
| | |SI| SI:WFR |
| | |BA| OAKL |

#### How will densities for new residential and commercial development be determined? 

Residential and commercial minimum and maximum densities will be determined by level of transit service. 

**Levels of Service & Residential Densities**
| Level of Transit Service | Required Min Density | Allowable Density |
|---|---|---|
| Tier 1: Rail stations serving regional centers\*  | 100 units/net acre | 150 units/net acre |
| Tier 2: Stop/station served by 2 or more BART lines or BART and Caltrain | 75 units/net acre | 100 units/net acre |
| Tier 3\*\*: Stop/station served by 1 BART line, Caltrain, light rail transit, or bus rapid transit | 50 units/net acre | 75 units/net acre |
| Tier 4: Commuter rail (SMART, ACE, Capitol Corridor) stations Caltrain Stations south of Tamien or ferry terminal | 25 units/net acre | 35 units/net acre |

- \* Applies to the following stations: Downtown San Francisco (Embarcadero, Montgomery, Powell, Civic Center); Oakland (19th, 12th, Lake Merritt); San Jose (Diridon)
- \*\* Tier 3 cities with a population of 30,000 or less my comply with Tier 4 density requirements. 

## Methodology

### Create Transit Oriented Communities Policy Area

Notebook: [Create Transit Oriented Communities Policy Area](Create_Transit_Oriented_Communities_Policy_Area.ipynb)

Inputs:
- [Transit Stops - Existing and Planned](https://opendata.mtc.ca.gov/datasets/transit-stops-existing-and-planned-2021/explore?location=37.890065%2C-122.301400%2C9.67)
- [San Francisco Bay Regional Water (Area)](https://opendata.mtc.ca.gov/datasets/san-francisco-bay-region-water-area/explore?location=37.833940%2C-122.344500%2C10.24)
- [San Francisco Bay Region Jurisdictions (Incorporated Places and Unincorporated Lands)](https://opendata.mtc.ca.gov/datasets/MTC::san-francisco-bay-region-jurisdictions-incorporated-places-and-unincorporated-county-lands/explore?location=37.833940%2C-122.344500%2C10.24)

Outputs:
- [Transit Oriented Communities Policy Area (MTC Access Only)](https://mtc.maps.arcgis.com/home/item.html?id=dd6f0b0a0d174cb2a4b61f0652e7ce31#overview)
- [Transit Oriented Communities Exploratory Map (TOC Team Access Only)](https://mtc.maps.arcgis.com/apps/mapviewer/index.html?webmap=e7e3e6df1d8c4b1da8341fa22b999047)

1. Preprocessing
    - Pull all input datasets and convert to geodataframe; project to `EPSG:26910`
2. Create dataframe of fixed-guideway stops
    - Fixed-guideway stops: `['Rail', 'BRT', 'Tram, Streetcar, Light Rail', 'Cable Tram','Ferry']`
    - Remove other stops where policy does not apply
    - Drop duplicate route/stop combinations
        - A number of stops are served by routes with the same route id for both directions. These need to be dropped to accurately count the number of unique routes that pass through any given station in later steps. 
3. Create station areas
    - Find stops that are nearby:
        - Cable Tram and BRT within 75 ft (22.86 meters) of other stops are considered same stop
        - Tram, Streetcar, Light Rail; Rail; Ferry within 300 ft (91.44 meters) of other stops are considered same stop
    - Dissolve stop areas to create station areas; this creates a multi-part geometry. 
    - Explode multi-part station areas to single-part station areas
    - Create station area id
    - Assign station id to stops
4. Drop duplicate routes from stations
    - After stations were identified in the previous step, some stations had duplicate route ids. These need to be dropped to accurately count the number of unique routes that pass through any given station in later steps. 
5. Count BART and Caltrain routes by station
    - Add BART and Caltrain route ids to planned routes
    - Group transit routes by station and agency
    - Add count columns to station geodataframe w/ point geometry
6. Flag levels of transit service and rank stations
    - **[Level of Transit Service](#how-will-densities-for-new-residential-and-commercial-development-be-determined)**
    - **Station rank:** Rank rail routes from 1-4 with 1 being the highest rank. This will be used along with tier to sort and drop duplicate routes, preserving stations with highest Level of Service and Route Rank. 
        - `Rail, Ferry`: 1
        - `Tram, Streetcar, Light Rail`: 2
        - `BRT`: 3
        - `Cable Tram`: 4
7. Create Transit Oriented Community Areas
    - Create 1/2 mile buffer (804.672 meter) around stops/stations (point geometry)
    - Erase [San Francisco Bay Regional Water (Area)](https://opendata.mtc.ca.gov/datasets/san-francisco-bay-region-water-area/explore?location=37.833940%2C-122.344500%2C10.24)
8. Add City and County to TOC Areas
    - Run identity overlay operation to assign county and jurisdiction to TOC from [San Francisco Bay Region Jurisdictions (Incorporated Places and Unincorporated Lands)](https://opendata.mtc.ca.gov/datasets/MTC::san-francisco-bay-region-jurisdictions-incorporated-places-and-unincorporated-county-lands/explore?location=37.833940%2C-122.344500%2C10.24)
9. Dissolve layers & remove overlaps
    - Dissolve or consolidate features by county, jurisdiction, service tier, and status
    - Remove overlaps between existing and planned areas. Existing TOC areas take priority over planned areas; where there are overlaps between the two keep existing areas and remove planned areas. 
    - Remove overlaps between service tier. Higher tiers take priority over lower tiers. Where there are overlaps, keep higher tier area and remove lower tier area. 
10. Publish Layers to ArcGIS Online