# SB79 Transit Oriented Development Upzoning <!-- omit in toc -->

- [About the Dataset](#about-the-dataset)
- [Background and Policy Context](#background-and-policy-context)
  - [TOD stop tiers](#tod-stop-tiers)
  - [Pedestrian access points](#pedestrian-access-points)
  - [Development standards](#development-standards)
- [Resources](#resources)
  - [Source Data](#source-data)
  - [Pipeline Outputs](#pipeline-outputs)
- [Expected Fields](#expected-fields)
  - [SB79 Transit-Oriented Development Zones](#sb79-transit-oriented-development-zones)
  - [Stations](#stations)
  - [Stops](#stops)
  - [Access Points](#access-points)
- [Running the Pipeline](#running-the-pipeline)
- [Process Overview](#process-overview)
  - [Manual Data Preparation](#manual-data-preparation)
  - [Load Data and Libraries](#load-data-and-libraries)
  - [Prepare Data for Analysis](#prepare-data-for-analysis)
  - [Flag Transit-Oriented Development (TOD) Stops](#flag-transit-oriented-development-tod-stops)
  - [Associate Parent Stations with TOD Stops \& Access Points](#associate-parent-stations-with-tod-stops--access-points)
  - [Create Transit-Oriented Development (TOD) Zones](#create-transit-oriented-development-tod-zones)
- [Development Notes](#development-notes)
  - [SB79 TOD Zones – Policy Applicability Matrix](#sb79-tod-zones--policy-applicability-matrix)
  - [TOD Zone Geographic Prioritization](#tod-zone-geographic-prioritization)
  - [Geographic Prioritization Approach](#geographic-prioritization-approach)
  - [Technical Considerations](#technical-considerations)

## About the Dataset

Senate Bill 79 (SB79) requires Metropolitan Planning Organizations (MPOs) to identify and map Transit-Oriented Development (TOD) Zones based on proximity to qualifying transit stops.

This project develops a reproducible geospatial methodology to:

- Identify SB79-eligible transit stops (Tier 1 and Tier 2)
- Define pedestrian access points and stations associated with those stops
- Generate distinct TOD zones based on Euclidean distance bands around access points
- Apply jurisdictional population rules
- Produce a TOD zone layer for the Bay Area that complies with SB 79.

The resulting datasets will serve as the authoritative SB79 TOD geography for the nine-county San Francisco Bay Area. In the Bay Area, the law applies to Alameda, San Francisco, San Mateo, and Santa Clara counties.

**Project Scope:**
- **Data Collection** -- Gather General Transit Feed Specification (GTFS) feeds, Caltrans High-Quality Transit Stops (HQTS) data, jurisdiction boundaries, and transit station datasets.
- **Data Preparation / Modeling** -- Identify TOD-eligible stops, classify tiers, construct pedestrian access points, and generate TOD bands.
- **Data Ingestion** -- Prepare final geospatial layer for internal review and publication.
- **Data Catalog / Publishing / MDM** -- Document methodology, inventory dataset in MDM Catalog, add to Enterprise Database, and publish to DAAS platforms (e.g. ArcGIS Online, Open Data, Socrata.)

## Background and Policy Context

SB 79, the *Abundant and Affordable Homes Near Transit Act*, was signed into law on October 10, 2025 and is codified in Government Code §§ 65912.155–65912.162. The law makes qualified housing development an allowed use on residential, mixed-use, and commercial sites near high-quality transit stops in counties with more than 15 passenger rail stations. In the Bay Area, eligible counties are Alameda, San Francisco, San Mateo, and Santa Clara.

SB 79 establishes minimum standards for building height, density, and residential floor area ratio (FAR) that vary by distance from a transit stop and the classification of that stop. It also requires each metropolitan planning organization (MPO) to produce a tiered map of TOD stops and zones. That map carries a rebuttable presumption of validity for use by project applicants and local governments.

### TOD stop tiers

Each qualifying transit stop is assigned one of two tiers based on service type:

- **Tier 1** — served by heavy rail transit or very high-frequency commuter rail (at least 72 trains/day across both directions, or the sum of total commuter rail stops regardless of direction). In the Bay Area: BART stations in Alameda, San Francisco, San Mateo, and Santa Clara Counties, and qualifying Caltrain stations (Tamien Station through the future Salesforce Transit Center, excluding stations with no daily service).
- **Tier 2** — served by light rail transit, high-frequency commuter rail (at least 48 trains/day across both directions, or the sum of total commuter rail stops regardless of direction), or bus rapid transit. In the Bay Area: VTA light rail, SF Muni Metro and Streetcar, AC Transit Tempo, and select additional bus stops that are adjacent to dedicated lanes and have AM and PM peak headways of 15 minutes or less.

### Pedestrian access points

Buffer distances under SB 79 are measured as a straight line from the nearest edge of a parcel to a pedestrian access point for the TOD stop — not from a single station centroid. While "pedestrian access point" is not defined in the statute, staff relied upon guidance in the HCD *SB 79 Advisory Clarifications on Definitions for Metropolitan Planning Organizations*, published March 23, 2026, and on previous communication from the bill author's office in response to a request or clarification by MPOs.

Guidance from the HCD Advisory: "Any applicable station entrance, boarding platform access point, or location of a Transit-Oriented Development stop as defined and depicted on the applicable Metropolitan Planning Organization Senate Bill 79 map."

(Source: SB 79 [Advisory Clarifications on Definitions for Metropolitan Planning Organizations](https://www.hcd.ca.gov/sites/default/files/docs/planning-and-community/sb-79-mpo-advisory.pdf), published March 23, 2025)

Guidance communicated by the bill author's office:

- Where an entrance exists: the station entrance
- Where no entrance exists: the platform edges
- Where neither exists: a single point

(Source: letter transmitted electronically from Senator Scott Wiener's office to Southern California Association of Governments staff in response to MPO questions, December 23, 2025)

### Development standards

SB 79 sets the following minimum development standards by tier and distance from a TOD stop. With the exception of TOD Alternative Plans approved by HCD prior to July 1, 2026 and eligible exemptions, local agencies may not apply lower height, density, or residential FAR limits to qualifying residential development projects than those listed below on parcels zoned for commercial, mixed use, or residential development.

| Distance from TOD stop | Tier 1 height | Tier 1 density | Tier 1 FAR | Tier 2 height | Tier 2 density | Tier 2 FAR |
|---|---|---|---|---|---|---|
| Adjacent (≤ 200 ft) | 95 ft | 160 du/ac | 4.5 | 85 ft | 140 du/ac | 4.0 |
| ≤ ¼ mile | 75 ft | 120 du/ac | 3.5 | 65 ft | 100 du/ac | 3.0 |
| ¼–½ mile (cities ≥ 35,000 residents) | 65 ft | 100 du/ac | 3.0 | 55 ft | 80 du/ac | 2.5 |

*Source: ABAG SB 79 Summary*

## Resources

The sources below were used to generate SB 79 stations, stops, and access points and were augmented with data as part of manual review steps outlined in subsequent sections. While scripts produced intermediate scratch data, only the final authoritative layers are documented in the pipeline outputs section below.

### Source Data

| Resource Type | Resource Name   | Description                                  | Source/Location      | Format       | Owner     | Version | Date Acquired/Created | Dependencies | Usage Notes                    |
|---------------|-----------------|----------------------------------------------|----------------------|--------------|-----------------|---------|-----------------------|--------------|--------------------------------|
| Dataset       | Pedestrian Access Points   | Pre-defined pedestrian access points for transit agencies | [Box Link](https://mtcdrive.box.com/s/q33u23k3amzgyidcf25cp1lzz6fn8br9)   | ZIP/Shapefile          | MTC       | Current     | 2026-02-18            | None         | Upstream source for access points curated into `tod_database.gdb`; individual shapefiles are not a direct pipeline input    |
| Dataset        | Transit Stations   | Transit station location data    | [Box Link](https://mtcdrive.box.com/s/jafqtaxw419tmw0r0m5z7j6g53l9b1p1)    | ZIP/Shapefile| MTC        | Current     | 2026-02-18            | None       | Station geometries and attributes |
| Dataset        | TOD Database (GDB)   | Curated stations, stops, and pedestrian access points for the SB79 TOD pipeline    | [Box Link](https://mtcdrive.box.com/s/vb000w0mrdgvgvxpon15ygvx4o3c5d00)    | File Geodatabase | MTC        | Current     | Ongoing            | Pedestrian Access Points, Transit Stations, 511 GTFS Data       | Direct input to Steps 2 and 3; contains curated stations, stops, and access points layers read via `GDB_STATIONS_LAYER`, `GDB_STOPS_LAYER`, and `GDB_ACCESS_PTS_LAYER` in `config.py` |
| API           | 511 GTFS Data     | Regional GTFS feeds for Bay Area transit agencies      | [Box Link](https://mtcdrive.box.com/s/qro5h0uvwwyovx1iuhvcjy55bjqbuana) | ZIP        | MTC  | Current      | 2026-02-18            | None         | Combined regional GTFS feed   |
| Dataset          | High Quality Transit Stops   | Caltrans-defined major BRT stops and high-frequency transit     | [ArcGIS Online](https://mtc.maps.arcgis.com/home/item.html?id=981ce33db7714f74b126489ef733437b)      | Feature Service  | MTC   | Current     | 2026-02-18            | None     | Used to identify Tier 2 BRT stops |
| Dataset          | Jurisdiction Boundaries   | Bay Area city and county boundaries with population data     | [ArcGIS Online](https://mtc.maps.arcgis.com/home/item.html?id=4b1242e5cb224a2c9043927d3344df5a)      | Feature Service  | MTC   | Current     | 2026-02-18            | None     | Population rules and geographic scope |

### Pipeline Outputs

The following authoritative layers are written to the centralized database ([`tod_database.gpkg`](https://mtcdrive.box.com/s/dc42a1ofq2mslwmkztdxk6pyvofoppee)). Intermediate development layers (`tod_stations_dev`, `tod_stops_dev`, `tod_access_points_dev`) are omitted.

| Layer | Description | Produced By |
|---|---|---|
| `tod_stations` | Finalized TOD parent station locations. | Step 3 |
| `tod_stops` | Finalized TOD stops with tier classification and station assignment. | Step 3 |
| `tod_access_points` | Finalized pedestrian access points used as the origin for TOD zone buffer generation. | Step 3 |
| `tod_zone_buffers` | Full-circle per-access-point buffers at all three distance bands (200 ft, ¼ mile, ½ mile), tagged with `tod_tier` and `buffer_band`. Retained as a diagnostic/QA layer and will be used in a public-facing web map to support transparency about how `tod_zones` were derived. | Step 4 |
| `jurisdictions_with_pop_acs2019_2023` | Bay Area jurisdiction boundaries joined to ACS 2019–2023 5-year total population estimates. Used to apply the jurisdictional population threshold rule. | Step 4 |
| `tod_zones` | **Authoritative** SB79 TOD zone polygons. Each polygon is assigned to exactly one of six non-overlapping `zone_label` classifications, representing the highest-priority applicable development standard under SB 79. | Step 4 |

## Expected Fields

This process will generate four interrelated datasets. Field types are logical/platform-agnostic; platform-specific type mappings (GeoPackage, ArcGIS, PostgreSQL) are documented separately at publication time.

**Data Model**

![image](img/SB79%20Data%20Model.png)

### SB79 Transit-Oriented Development Zones
Final SB 79-consistent TOD zone polygons. One polygon per non-overlapping zone; each polygon is assigned the highest-priority applicable development standard under SB 79. See [Geographic Prioritization Approach](#geographic-prioritization-approach) for how zones are derived.

| Field | Data Type | Allow NULL | Domain | Description |
|---|---|---|---|---|
| `zone_id` | UUID | No | — | Unique zone identifier; UUID4 assigned after priority resolution |
| `zone_label` | Text | No | `Tier 1 - 200ft`, `Tier 2 - 200ft`, `Tier 1 - Quarter Mile`, `Tier 2 - Quarter Mile`, `Tier 1 - Half Mile`, `Tier 2 - Half Mile` | Priority tier and distance band classification |
| `geometry` | Geometry (Polygon) | No | — | Non-overlapping TOD zone polygon. All zones have unincorporated county lands erased. Half-mile zones additionally have sub-35,000 population incorporated city jurisdictions erased. Slivers < 100 m² are removed |

### Stations
Parent transit station locations (GTFS `location_type = 1`).

| Field | Data Type | Allow NULL | Domain | Description |
|---|---|---|---|---|
| `station_id` | Text | No | — | Unique station identifier sourced from the curated GDB layer (`GDB_STATIONS_LAYER` in `config.py`) |
| `station_name` | Text | No | — | Human-readable station name |
| `location_type` | Integer | No | GTFS: `1` = Station | GTFS location type |
| `manually_added` | Integer | No | `0` = sourced from GTFS; `1` = manually added | Indicates whether the station was manually added during the Step 1 GIS review rather than sourced natively from GTFS |
| `geometry` | Geometry (Point) | No | — | Station location |

### Stops
Individual transit stop/platform locations actively served by transit routes and classified as TOD-eligible under SB 79.

| Field | Data Type | Allow NULL | Domain | Description |
|---|---|---|---|---|
| `stop_id` | Text | No | — | Unique GTFS stop identifier |
| `station_id` | Text | No | — | Parent station ID — assigned by spatial buffer analysis in Step 2, with manual corrections applied in Step 3 |
| `location_type` | Integer | No | GTFS: `0` = Stop/Platform | GTFS location type |
| `stop_name` | Text | Yes | — | Stop name from GTFS or curated GDB |
| `agency_id` | Text | No | `BA`, `CT`, `AC`, `SC`, `SF` | Transit agency short code |
| `agency_name` | Text | No | — | Full transit agency name |
| `route_short_name` | Text | Yes | — | GTFS route short name or number |
| `route_type` | Integer | No | See [GTFS routes.txt reference](https://gtfs.org/documentation/schedule/reference/#routestxt) | GTFS route type (e.g. `0` = tram/streetcar/light rail, `1` = subway/metro, `2` = rail) |
| `tod_tier` | Text | No | `Tier 1`, `Tier 2` | SB79 tier designation |
| `geometry` | Geometry (Point) | No | — | Stop location |

### Access Points
Pedestrian access locations for each transit station used as the origin for TOD zone buffer generation.

| Field | Data Type | Allow NULL | Domain | Description |
|---|---|---|---|---|
| `access_id` | Text | No | — | Unique access point identifier. Sourced from each agency's stop ID field; falls back to a stable coordinate-based ID (`geom:<lat>,<lon>`) for records with missing or colliding IDs. Assigned during GDB curation and read as-is by Step 2 |
| `station_id` | Text | No | — | Parent station ID — joined from GTFS, then resolved spatially or manually via the Step 2–3 review workflow |
| `access_point_name` | Text | Yes | — | Descriptive name of the pedestrian access point, sourced from each agency's stop name field |
| `location_type` | Integer | No | GTFS: `2` = Entrance/Exit, `3` = Generic Node | GTFS location type; defaults to `2` if absent in the curated GDB layer |
| `geometry` | Geometry (Point) | No | — | Access point location used as the origin for TOD zone buffer generation |

## Running the Pipeline

Step-by-step execution instructions for the five-notebook pipeline are maintained in a separate document intended for internal technical use. This includes notebook descriptions, prerequisite setup, mandatory manual GIS review gates, and output specifications for each step.

See [RUNNING_THE_PIPELINE.md](RUNNING_THE_PIPELINE.md) for full instructions.

---

## Process Overview

> This section describes the conceptual methodology behind the pipeline. For step-by-step execution instructions, see [RUNNING_THE_PIPELINE.md](RUNNING_THE_PIPELINE.md).

### Manual Data Preparation
1. Manually create stations for stops that will be flagged as TOD applicable, such as SFMTA light rail stops not co-located with a BART Station (e.g. Van Ness, Church, Forest Hill, Yerba Buena/Moscone, etc.), VTA light rail stops, and BRT stops.
2. Manually create pedestrian access points for stops that will be flagged as TOD applicable following the same process as above (add guidance from HCD on what constitutes a pedestrian access point, e.g. crosswalks, sidewalks, etc.).

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
1. Associate stops and access points with parent stations. This may be performed by spatially joining stops and access points to stations using a near spatial join with a specified distance threshold (e.g. 200 feet) though manual review and adjustments will likely be necessary to ensure accurate associations, especially in dense urban areas where multiple stations and stops may be in close proximity.

### Create Transit-Oriented Development (TOD) Zones
1. Generate full-circle Euclidean buffers at 200 ft, ¼ mile, and ½ mile around each finalized pedestrian access point; tag each buffer with `tod_tier` and `buffer_band`.
2. Apply the jurisdictional population rule: erase all buffers (200 ft, ¼ mile, ½ mile) within unincorporated county lands; additionally erase half-mile buffers within incorporated cities with total population < 35,000.
3. Resolve geographic priority via sequential erase: split buffers into six groups by `(tod_tier, buffer_band)`, then for each group in priority order, erase the accumulated geometry of all higher-priority zones before assigning a `zone_label`. This produces six clean, non-overlapping zone layers. See [Geographic Prioritization Approach](#geographic-prioritization-approach) for implementation details.
4. Finalize: dissolve by `zone_label` 
5. Export the buffer layer, jurisdiction boundaries with population, and resolved TOD zones to the shared GeoPackage.

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
   - Where Tier 1 and Tier 2 zones intersect, Tier 1 generally supersedes Tier 2. Tier 2 geometry must be erased in overlapping areas. The one exception is where a Tier 2 200 ft zone overlaps with a Tier 1 quarter-mile or half-mile zone — in that case Tier 2 200 ft prevails, as it carries higher development standards than either Tier 1 distance band.
2. **Geographic Scope:**
   - Applies only to incorporated cities and towns located within:
     - Alameda County
     - San Francisco County
     - San Mateo County
     - Santa Clara County
3. **Distance Bands:**
   - Bands are distinct (non-cumulative):
     - 0–200 feet
     - 201–1320 feet (¼ mile ring excluding first 200 feet)
     - 1321–2640 feet (½ mile ring excluding first ¼ mile)

### TOD Zone Geographic Prioritization

Where buffers from different tiers and distance bands overlap after union, each geometry is assigned a single TOD zone classification representing the most permissive applicable development standard for qualified residential development projects under SB 79. The prioritization cascades as follows:

| Priority | Zone | Height limit | Density (du/ac) | Residential FAR |
|---|---|---|---|---|
| 1 | Tier 1 — 200 ft | 95 ft | 160 | 4.5 |
| 2 | Tier 2 — 200 ft | 85 ft | 140 | 4.0 |
| 3 | Tier 1 — Quarter mile | 75 ft | 120 | 3.5 |
| 4 | Tier 1 — Half mile* | 65 ft | 100 | 3.0 |
| 5 | Tier 2 — Quarter mile | 65 ft | 100 | 3.0 |
| 6 | Tier 2 — Half mile* | 55 ft | 80 | 2.5 |

*Half-mile band only applies within incorporated cities with population ≥ 35,000. All bands (200 ft, quarter-mile, and half-mile) are erased from unincorporated county lands.

This ordering reflects two rules. First, Tier 1 takes full precedence over Tier 2 at all distance bands — all Tier 1 zones are resolved before any Tier 2 zone beyond 200 ft. Second, both 200 ft zones are resolved first as a pair because Tier 2 200 ft development standards (85 ft, 140 du/ac) are more permissive than either Tier 1 quarter-mile (75 ft, 120 du/ac) or Tier 1 half-mile (65 ft, 100 du/ac), so Tier 2 200 ft takes priority 2 ahead of those bands. The result is that Priority 1 always yields the highest entitlements and Priority 6 the lowest — a geometry retains the classification of the highest-priority zone it falls within.

See [Geographic Prioritization Approach](#geographic-prioritization-approach) for implementation details.

### Geographic Prioritization Approach

The priority order above is implemented via a **sequential erase** rather than a union-then-classify approach. A union-based approach would fragment geometry at every intersection boundary — producing thousands of small polygons across the entire study area, each requiring individual classification. The sequential erase avoids this entirely and produces clean, non-overlapping polygons directly.

The approach works as follows: the six `(tod_tier, buffer_band)` groups are processed in priority order. The highest-priority group (Tier 1 – 200 ft) is kept unchanged and becomes the initial accumulated mask. For each subsequent group, a dissolved union of all previously processed groups is erased from the current group's geometry before it is assigned its `zone_label`. The accumulated mask grows with each iteration, so by the time the lowest-priority group (Tier 2 – Half Mile) is processed, the geometry of all five higher-priority zones has already been removed from it.

After each erase step, zero-area floating-point artifacts are dropped and geometry validity is repaired before the result is appended to the accumulated mask. The six resulting layers are concatenated to form `tod_zones`.

### Technical Considerations

- GTFS data provides the authoritative source for transit stop locations and service patterns. Agency filtering focuses on relevant Bay Area operators: BART (BA), Caltrain (CT), AC Transit (AC), VTA (SC), and SFMTA (SF). Parent-child relationships in the GTFS hierarchy distinguish between stations (`location_type=1`) and individual stops/platforms (`location_type=0`).
- Some stops and access points are not fully represented in GTFS and require manual mapping. This includes SFMTA light rail stops not co-located with a BART station, VTA light rail stops, and BRT stops. In addition, many BART and Caltrain stops do not have comprehensively mapped pedestrian access points. Manually mapped features are tracked via the `action` column in the curated stop and station layers.
- Caltrans [High Quality Transit Areas (HQTA) Stops](https://gis.data.ca.gov/datasets/f6c30480f0e84be699383192c099a6a4_0) data is used to identify TOD-eligible bus stops. Specifically, stops with `hqta_type = major_stop_brt` are used to flag Tier 2 BRT stops based on frequency standards derived from GTFS schedule data. The HQTA dataset is updated monthly by Caltrans — the version acquired for this analysis is recorded in the [Source Data](#source-data) table. For methodology details see the [Caltrans HQTA documentation](https://docs.calitp.org/data-analyses/high_quality_transit_areas/).
- All spatial operations in Step 4 use EPSG:26910 (UTM Zone 10N) as the analysis CRS for accurate planar distance and area measurements. Reprojection to EPSG:4326 occurs only at final GeoPackage export.
- After each erase operation in Step 4, polygon fragments smaller than 100 m² are discarded as floating-point artifacts. This threshold was validated against the actual area distribution of post-overlay fragments, which showed a hard gap between near-zero artifacts (all < 1 m²) and the smallest legitimate fragment (> 1,279,000 m²).
- `tod_zone_buffers` is a diagnostic layer retained for QA and public transparency. The authoritative output for policy and regulatory use is `tod_zones`.


