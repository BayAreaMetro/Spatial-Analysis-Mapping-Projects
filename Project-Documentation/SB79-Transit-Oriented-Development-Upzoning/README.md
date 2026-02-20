# SB79 Transit Oriented Development Upzoning <!-- omit in toc -->

- [About the Dataset](#about-the-dataset)
- [Resources](#resources)
- [Expected Fields](#expected-fields)
  - [SB79 Transit-Oriented Development Zones](#sb79-transit-oriented-development-zones)
  - [Stations](#stations)
  - [Stops](#stops)
  - [Access Points](#access-points)
- [Process Overview](#process-overview)
  - [Load Data and Libraries](#load-data-and-libraries)
  - [Prepare Data for Analysis](#prepare-data-for-analysis)
  - [Flag Transit-Oriented Development (TOD) Stops](#flag-transit-oriented-development-tod-stops)
  - [Associate Parent Stations with TOD Stops \& Access Points](#associate-parent-stations-with-tod-stops--access-points)
  - [Create Transit-Oriented Development (TOD) Zones](#create-transit-oriented-development-tod-zones)
- [Development Notes](#development-notes)
  - [SB79 TOD Zones – Policy Applicability Matrix](#sb79-tod-zones--policy-applicability-matrix)
  - [Technical Considerations](#technical-considerations)

## About the Dataset

Senate Bill 79 (SB79) requires Metropolitan Planning Organizations (MPOs) to identify and map Transit-Oriented Development (TOD) Zones based on proximity to qualifying transit stops.

This project develops a reproducible geospatial methodology to:

- Identify SB79-eligible transit stops (Tier 1 and Tier 2)
- Define pedestrian access points and stations associated with those stops
- Generate distinct TOD zones based on Euclidean distance bands around access points
- Apply jurisdictional population rules
- Produce a policy-compliant TOD zone layer for the Bay Area

The resulting datasets will serve as the authoritative SB79 TOD geography for Alameda, San Francisco, San Mateo, and Santa Clara counties.

**Project Scope:**
- **Data Collection** -- Gather GTFS feeds, Caltrans HQTS data, jurisdiction boundaries, and transit station datasets.
- **Data Preparation / Modeling** -- Identify TOD-eligible stops, classify tiers, construct pedestrian access points, and generate TOD bands.
- **Data Ingestion** -- Prepare final geospatial layer for internal review and publication.
- **Data Catalog / Publishing / MDM** -- Document methodology, inventory dataset in MDM Catalog, add to Enterprise Database, and publish to DAAS platforms (e.g. ArcGIS Online, Open Data, Socrata.)

## Resources 

| Resource Type | Resource Name   | Description                                  | Source/Location      | Format       | Owner     | Version | Date Acquired/Created | Dependencies | Usage Notes                    |
|---------------|-----------------|----------------------------------------------|----------------------|--------------|-----------------|---------|-----------------------|--------------|--------------------------------|
| Dataset       | Pedestrian Access Points   | Pre-defined pedestrian access points for transit agencies | [Box Link](https://mtcdrive.box.com/s/q33u23k3amzgyidcf25cp1lzz6fn8br9)   | ZIP/Shapefile          | MTC       | Current     | 2026-02-18            | None         | Agency-specific access point locations    |
| Dataset        | Transit Stations   | Transit station location data    | [Box Link](https://mtcdrive.box.com/s/jafqtaxw419tmw0r0m5z7j6g53l9b1p1)    | ZIP/Shapefile| MTC        | Current     | 2026-02-18            | None       | Station geometries and attributes |
| API           | 511 GTFS Data     | Regional GTFS feeds for Bay Area transit agencies      | [Box Link](https://mtcdrive.box.com/s/qro5h0uvwwyovx1iuhvcjy55bjqbuana) | ZIP        | MTC  | Current      | 2026-02-18            | None         | Combined regional GTFS feed   |
| Dataset          | High Quality Transit Stops   | Caltrans-defined major BRT stops and high-frequency transit     | [ArcGIS Online](https://mtc.maps.arcgis.com/home/item.html?id=981ce33db7714f74b126489ef733437b)      | Feature Service  | MTC   | Current     | 2026-02-18            | None     | Used to identify Tier 2 BRT stops |
| Dataset          | Jurisdiction Boundaries   | Bay Area city and county boundaries with population data     | [ArcGIS Online](https://mtc.maps.arcgis.com/home/item.html?id=4b1242e5cb224a2c9043927d3344df5a)      | Feature Service  | MTC   | Current     | 2026-02-18            | None     | Population rules and geographic scope |

## Expected Fields

This process will generate four interrelated datasets:

### SB79 Transit-Oriented Development Zones
Final policy-compliant TOD zone polygons with tier classifications and distance bands.

*Field specifications to be documented during development.*

### Stations 
Parent transit station locations (location_type = 1 in GTFS hierarchy).

*Field specifications to be documented during development.*

### Stops
Individual transit stop/platform locations actively served by transit routes.

*Field specifications to be documented during development.*

### Access Points
Pedestrian access locations for each transit station used as the basis for TOD zone generation.

*Field specifications to be documented during development.*

## Process Overview

### Load Data and Libraries
1. Set up environment and load necessary libraries (e.g., pandas, geopandas, gtfs_kit)
2. Load GTFS data using gtfs_kit and convert to GeoDataFrame for spatial analysis
3. Load pedestrian access point data and transit station data as GeoDataFrames
4. Load Caltrans High Quality Transit Stops (HQTS) data as GeoDataFrame

### Prepare Data for Analysis
1. Enrich GTFS stops with route and agency information by merging with routes and agency tables; aggregate to get lists of routes and agencies serving each stop
2. Filter GTFS stops to include only those served by relevant transit agencies (e.g., BART, Caltrain, AC Transit, SFMTA, VTA)
3. Separate stations and stops based on GTFS hierarchy based on location_type and parent_station fields (see [GTFS documentation](https://gtfs.org/documentation/schedule/reference/#stopstxt) for details)
4. Filter Caltrans High Quality Station Stops to include only those with `HQTA Type == major_stop_brt`

### Flag Transit-Oriented Development (TOD) Stops
1. Flag GTFS stops as TOD applicable if they are either:
   1. A stop that meets the Caltrans definition of a major BRT stop (i.e., in the filtered Caltrans dataset) using a list of `stop_id`s from the filtered HQTS dataset, OR
   2. A stop with `route_type in [0 (Tram, Streetcar, Light rail), 1 (Subway, Metro)]` (see [GTFS documentation](https://gtfs.org/documentation/schedule/reference/#routestxt) for details) or `agency_id == 'CT' (Caltrain)`
      1. Exceptions: Exclude stops South of Tamien Station on the Caltrain System, and BART stops within Contra Costa County.
2. Create Transit Tier classification:
   1. Tier 1: `route_type == 1 (Subway, Metro)` or `agency_id == 'CT' (Caltrain)`
   2. Tier 2: `route_type == 0 (Tram, Streetcar, Light rail)` or a stop that meets the Caltrans definition of a major BRT stop (i.e., in the filtered Caltrans dataset) using a list of `stop_id`s from the filtered HQTS dataset.
3. Create a final filtered GeoDataFrame of TOD applicable stops, including relevant attributes such as stop_id, stop_name, parent_station, agency_name, route_short_name, and geometry.

### Associate Parent Stations with TOD Stops & Access Points
1. Manually create stations for stops that are flagged as TOD applicable, such as SFMTA light rail stops not co-located with a BART Station (e.g. Van Ness, Church, Forest Hill, Yerba Buena/Moscone, etc.), VTA light rail stops, and BRT stops.
2. Manually create pedestrian access points for stops that are flagged as TOD applicable following the same process as above (add guidance from HCD on what constitutes a pedestrian access point, e.g. crosswalks, sidewalks, etc.).
3. Associate stops and access points with parent stations. This may be performed by spatially joining stops and access points to stations using a near spatial join with a specified distance threshold (e.g. 200 feet) though manual review and adjustments will likely be necessary to ensure accurate associations, especially in dense urban areas where multiple stations and stops may be in close proximity.

### Create Transit-Oriented Development (TOD) Zones
1. Generate 200 ft, .25 mile, and .5 mile Euclidean (straight-line) buffers around all pedestrian access points by tier
2. Intersect buffers with jurisdiction boundaries with associated population data to determine applicable zones based on the policy matrix
3. Remove .5 mile buffers where jurisdiction population is ≤ 35,000 or in unincorporated areas
4. Erase Tier 2 areas where overlapping with Tier 1 buffers to ensure Tier 1 precedence
5. Dissolve by Tier and distance band to create final TOD Zone geometries
6. Validate and review final TOD Zone geometries for accuracy and consistency with the defined criteria

## Development Notes

### SB79 TOD Zones – Policy Applicability Matrix

This table summarizes where Transit-Oriented Development (TOD) Zones apply by Transit Tier and Jurisdiction Type. Distances are measured from pedestrian access points and represent distinct distance bands.

**Where TOD Zones Apply**

| Tier       | City with Population > 35,000       | City with Population ≤ 35,000 | Unincorporated Area |
| ---------- | ----------------------------------- | ----------------------------- | ------------------- |
| **Tier 1** | 0–200'<br>201'–1320'<br>1321'–2640' | 0–200'<br>201'–1320'          | Not Applicable      |
| **Tier 2** | 0–200'<br>201'–1320'<br>1321'–2640' | 0–200'<br>201'–1320'          | Not Applicable      |

**Policy Constraints**

1. **Tier Precedence Rule:**
   - Where Tier 1 and Tier 2 zones intersect, Tier 1 supersedes Tier 2. Tier 2 geometry must be erased in overlapping areas.
2. **Geographic Scope:**
   - Applies only to cities located within:
     - Alameda County
     - San Francisco County
     - San Mateo County
     - Santa Clara County
3. **Distance Bands:**
   - Bands are distinct (non-cumulative):
     - 0–200 feet
     - 201–1320 feet (¼ mile ring excluding first 200 feet)
     - 1321–2640 feet (½ mile ring excluding first ¼ mile)

### Technical Considerations

- GTFS data provides the authoritative source for transit stop locations and service patterns
- Agency filtering focuses on relevant Bay Area operators: BART (BA), Caltrain (CT), AC Transit (AC), VTA (SC), and SFMTA (SF)
- Parent-child relationships in GTFS hierarchy distinguish between stations (location_type=1) and individual stops/platforms (location_type=0)
- Manual review required for complex station areas with multiple access points


