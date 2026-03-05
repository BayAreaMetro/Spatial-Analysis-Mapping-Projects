# SB79 Transit Oriented Development Upzoning <!-- omit in toc -->

- [About the Dataset](#about-the-dataset)
- [Resources](#resources)
- [Expected Fields](#expected-fields)
  - [SB79 Transit-Oriented Development Zones](#sb79-transit-oriented-development-zones)
  - [Stations](#stations)
  - [Stops](#stops)
  - [Access Points](#access-points)
- [Running the Pipeline](#running-the-pipeline)
  - [Prerequisites](#prerequisites)
  - [Step 1 – GTFS TOD Stop Classification](#step-1--gtfs-tod-stop-classification)
  - [Step 2 – TOD Stop and Access Point Assignment](#step-2--tod-stop-and-access-point-assignment)
  - [Step 3 – Station Assignment Reintegration](#step-3--station-assignment-reintegration)
  - [Step 4 – TOD Zone Buffer Generation](#step-4--tod-zone-buffer-generation)
- [Process Overview](#process-overview)
  - [Manual Data Preparation](#manual-data-preparation)
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

## Running the Pipeline

The pipeline is implemented as a sequence of four Jupyter notebooks. Each notebook is self-contained and reads/writes to a shared GeoPackage (`tod_database.gpkg`) defined in `config.py`. There are **two mandatory manual GIS review gates** — one after Step 1 and one between Steps 2 and 3. Do not skip them.

### Prerequisites

- Python environment with `geopandas`, `pandas`, `gtfs_kit`, `shapely`, `uuid`, and `openpyxl` installed
- Access to the MTC Box folder containing source data (see [Resources](#resources))
- Paths in `config.py` updated to match your local data directory
- QGIS (or equivalent) for the manual GIS review gate after Step 1
- Excel (or equivalent spreadsheet application) for the manual review gate between Steps 2 and 3

---

### Step 1 – GTFS TOD Stop Classification

**Notebook:** `1_gtfs_tod_stop_classification.ipynb`

Loads the regional GTFS feed and Caltrans High Quality Transit Stops (HQTS) data, classifies each stop as TOD-eligible (Tier 1 or Tier 2), and writes the results to the shared GeoPackage.

**Outputs written to GPKG:**
- `stops` — GTFS location_type=0 stop/platform records served by relevant routes, with `tod_stop` flag and `tod_tier` classification
- `stations` — GTFS location_type=1 parent station records
- `access_points` — GTFS location_type=2 (entrance/exit) and location_type=3 (generic node) records

> **Manual GIS review required before running Step 2.**
>
> The `stops` and `stations` layers from the GPKG serve as the starting point for manual curation. Curated output is saved to a File Geodatabase (`tod_database.gdb`, layers `stations_v1` and `stops_v1`), which Step 2 reads directly. Pedestrian access points are **not** carried through the FGDB — they are loaded directly from per-agency source files in Step 2.
>
> **Stations (`stations_v1`):**
> 1. Load the `stations` layer from the GPKG into GIS.
> 2. Copy it into `tod_database.gdb` as `stations_v1`.
> 3. Manually add station records for TOD-applicable stops that lack a parent station in GTFS — for example, SFMTA light rail stops not co-located with a BART station, VTA light rail stops, and BRT stops.
>
> **Stops (`stops_v1`):**
> 1. Load the `stops` layer from the GPKG into GIS.
> 2. Copy it into `tod_database.gdb` as `stops_v1`.
> 3. Review each stop flagged as `tod_stop = 1` by the automated process to confirm correctness.
> 4. For any stops that should be TOD-applicable but were not caught by the automated logic, manually set `tod_stop = 1` and populate the `action` column with the reason for inclusion (e.g. `"manual — VTA BRT stop"`, `"manual — SFMTA light rail"`).
>
> Once both curated layers are saved to `tod_database.gdb`, proceed to Step 2.

---

### Step 2 – TOD Stop and Access Point Assignment

**Notebook:** `2_tod_stop_and_access_assignment.ipynb`

Loads per-agency pedestrian access point datasets, normalizes and merges them into a single GeoDataFrame, joins GTFS-authoritative `station_id` values, then spatially assigns each TOD stop and access point to a parent station by progressively expanding station buffers at **150 ft, 300 ft, 500 ft, and 1000 ft** (EPSG:26910). Points falling within exactly one station buffer are assigned; points intersecting multiple station buffers at the same distance are flagged as conflicts. Non-TOD stations are excluded before spatial assignment using the station overrides list (`2026_03_04_tod_stations_overrides.xlsx`). Outputs development layers to the shared GeoPackage and a review Excel workbook for manual resolution.

**Access point sources (loaded and normalized in order):**
- `BA` — BART (`BART_PedAccessPoints_GTFS_v1.zip`)
- `CT` — Caltrain (`Caltrain_PedAccessPoints_GTFS_v3.zip`)
- `AC` — AC Transit (`AC_Transit_PedAcessPoints_v3.gdb`)
- `SC` — VTA (`VTA_PedAccessPoints_GTFS_v2.zip`)
- `SF` — SFMTA (`SFMuni_PedAccessPoints_GTFS_v1.zip`)

**Outputs written to GPKG** *(development layers — not yet authoritative):*
- `tod_stations_dev` — station layer used for spatial assignment (filtered to TOD stations)
- `tod_stops_dev` — TOD stops with spatially assigned `station_id` and `assignment_status`
- `tod_access_points_dev` — merged access points with spatially assigned `station_id` and `assignment_status`

**Review workbook written to Box data folder:**
- `SB79_tod_review.xlsx` — contains all stops and access points with `assignment_status` and `station_id`; reviewers use this file to resolve conflicts and no-match records before running Step 3

> **Manual Excel review required before running Step 3.**
>
> 1. Open `SB79_tod_review.xlsx`.
> 2. **Priority — resolve `conflict` and `no_match` records first.**
>    - Filter each sheet to rows where `assignment_status` is `conflict` or `no_match`.
>    - Open the corresponding `_dev` layer (`tod_stops_dev` or `tod_access_points_dev`) in QGIS/ArcGIS Pro alongside `tod_stations_dev` to visually identify the correct parent station.
>    - Copy the correct `station_id` from `tod_stations_dev` into the `station_id` cell for that row.
>    - Set `assignment_status` = `manual_station_assignment` using the dropdown.
> 3. **Secondary — correct any mis-assigned records.**
>    - If a row has `assignment_status = assigned` but the spatial assignment produced the wrong station (e.g., a stop was snapped to the nearest station rather than its true parent), update `station_id` to the correct value and set `assignment_status` = `manual_station_assignment`.
>    - Leave correctly-assigned rows untouched — only rows with `assignment_status = manual_station_assignment` are applied as updates in Step 3.
> 4. Save the workbook, then run Step 3.

---

### Step 3 – Station Assignment Reintegration

**Notebook:** `3_tod_station_assignment_reintegration.ipynb`

Reads the manually-reviewed Excel workbook (`SB79_tod_review.xlsx`), validates any manually-assigned `station_id` values against the TOD station universe, applies corrections to the development datasets, and exports the final authoritative layers to the shared GeoPackage.

**Inputs:**
- `SB79_tod_review.xlsx` — reviewed workbook with `manual_station_assignment` rows filled in
- `tod_stations_dev`, `tod_stops_dev`, `tod_access_points_dev` — development layers from Step 2 (read from GPKG)

**Outputs written to GPKG** *(final authoritative layers):*
- `tod_stations` — final station layer
- `tod_stops` — final stops with all manual corrections applied
- `tod_access_points` — final access points with all manual corrections applied

> No manual review required between Steps 3 and 4.

---

### Step 4 – TOD Zone Buffer Generation

**Notebook:** `4_tod_zone_buffers.ipynb` *(planned)*

Generates 200 ft, ¼ mile, and ½ mile Euclidean buffer zones around finalized access points, applies the policy matrix (tier precedence, jurisdictional population rules, geographic scope), and produces the final SB79 TOD Zone polygons.

**Outputs written to GPKG:**
- `tod_zones` — final SB79 TOD Zone polygons with tier and distance-band attributes

---

## Process Overview

> This section describes the conceptual methodology behind the pipeline. For step-by-step execution instructions, see [Running the Pipeline](#running-the-pipeline).

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


