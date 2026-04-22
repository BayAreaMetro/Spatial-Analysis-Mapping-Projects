# Running the Pipeline

The pipeline is implemented as a sequence of five Jupyter notebooks. Each notebook is self-contained and reads/writes to a shared GeoPackage (`tod_database.gpkg`) defined in `config.py`. There are **two mandatory manual GIS review gates** — one after Step 1 and one between Steps 2 and 3. Do not skip them.

## Prerequisites

- Python environment with `geopandas`, `pandas`, `gtfs_kit`, `shapely`, `uuid`, and `openpyxl` installed
- Access to the MTC Box folder containing source data (see [Source Data](README.md#source-data))
- Paths in `config.py` updated to match your local data directory
- QGIS (or equivalent) for the manual GIS review gate after Step 1
- Excel (or equivalent spreadsheet application) for the manual review gate between Steps 2 and 3

---

## Step 1 – GTFS TOD Stop Classification

**Notebook:** `1_gtfs_tod_stop_classification.ipynb`

Loads the regional GTFS feed and Caltrans High Quality Transit Stops (HQTS) data, classifies each stop as TOD-eligible (Tier 1 or Tier 2), and writes the results to the shared GeoPackage.

**Outputs written to GPKG:**
- `stops` — GTFS location_type=0 stop/platform records served by relevant routes, with `tod_stop` flag and `tod_tier` classification
- `stations` — GTFS location_type=1 parent station records
- `access_points` — GTFS location_type=2 (entrance/exit) and location_type=3 (generic node) records

> **Manual GIS review required before running Step 2.**
>
> The `stops` and `stations` layers from the GPKG serve as the starting point for manual curation. Curated output is saved to a File Geodatabase (`tod_database.gdb`, layers `stations` and `stops`), which Step 2 reads directly. Pedestrian access points are **not** carried through the FGDB — they are loaded directly from per-agency source files in Step 2.
>
> **Stations (`stations`):**
> 1. Load the `stations` layer from the GPKG into GIS.
> 2. Copy it into `tod_database.gdb` as `stations`.
> 3. Manually add station records for TOD-applicable stops that lack a parent station in GTFS — for example, SFMTA light rail stops not co-located with a BART station, VTA light rail stops, and BRT stops.
>
> **Stops (`stops`):**
> 1. Load the `stops` layer from the GPKG into GIS.
> 2. Copy it into `tod_database.gdb` as `stops`.
> 3. Review each stop flagged as `tod_stop = 1` by the automated process to confirm correctness.
> 4. For any stops that should be TOD-applicable but were not caught by the automated logic, manually set `tod_stop = 1` and populate the `action` column with the reason for inclusion (e.g. `"manual — VTA BRT stop"`, `"manual — SFMTA light rail"`).
> 5. Manually add stops that did not exist in the GTFS source data, such as planned stops identified in the Regional Transportation Improvement Plan (RTIP) and update required columns such as `tod_stop`, `stop_id`, `stop_name`, `agency_id`, `agency_name`, and `location_type`.
>
> Once both curated layers are saved to `tod_database.gdb`, proceed to Step 2.

---

## Step 2 – TOD Stop and Access Point Assignment

**Notebook:** `2_tod_stop_and_access_assignment.ipynb`

Loads per-agency pedestrian access point datasets, normalizes and merges them into a single GeoDataFrame, joins GTFS-authoritative `station_id` values, then spatially assigns each TOD stop and access point to a parent station by progressively expanding station buffers at **150 ft, 300 ft, 500 ft, and 1000 ft** (EPSG:26910). Points falling within exactly one station buffer are assigned; points intersecting multiple station buffers at the same distance are flagged as conflicts. Non-TOD stations are excluded before spatial assignment using the station overrides list (`YYYY_MM_DD_tod_stations_overrides.xlsx`). Outputs development layers to the shared GeoPackage and a review Excel workbook for manual resolution.

**Access point sources (loaded and normalized in order):**
Defined in `ACCESS_PTS_SOURCES` in [`config.py`](config.py). Update file paths there when new agency source files are available.

**Outputs written to GPKG** *(development layers):*
- `tod_stations_dev` — station layer used for spatial assignment (filtered to TOD stations)
- `tod_stops_dev` — TOD stops with spatially assigned `station_id` and `assignment_status`
- `tod_access_points_dev` — merged access points with spatially assigned `station_id` and `assignment_status`

**Review workbook written to Box data folder:**
- `SB79_tod_review.xlsx` — contains all stops and access points with `assignment_status` and `station_id`; reviewers use this file to resolve conflicts and no-match records before running Step 3

> **Manual Excel review required before running Step 3.**
>
> 1. **Before editing — rename the file.** Rename `SB79_tod_review.xlsx` to `SB79_tod_review_reviewed_YYYY_MM_DD.xlsx` (replacing `YYYY_MM_DD` with today's date). This prevents a future re-run of Step 2 from overwriting your work. Then update `REVIEW_XLSX` in `config.py` to point to the renamed file path.
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

## Step 2b – Review Reconciliation

**Notebook:** `2b_tod_review_reconciliation.ipynb`

Run **only** when Step 2 has been re-run after new stops or access points were added, making the existing reviewed workbook stale. Reconciles the fresh `SB79_tod_review.xlsx` with the previously-reviewed workbook (`REVIEW_XLSX` in `config.py`) to carry forward valid `manual_station_assignment` decisions, then writes a new dated workbook as the starting point for the next manual review cycle.

**Carry-over rules:**
- Only rows with `assignment_status = manual_station_assignment` are carried from the stale workbook — `conflict` and `no_match` rows are discarded in favour of the fresh spatial assignment.
- Carried-over `station_id` values that no longer exist in the current TOD station universe are downgraded to `conflict` and flagged for re-review.
- Records dropped from the new ID universe (present in the stale workbook but absent from the fresh Step 2 output) are reported in the notebook output but not written to the reconciled workbook.

**Inputs (set in `config.py`):**
- `REVIEW_XLSX_OUTPUT` (`SB79_tod_review.xlsx`) — fresh Step 2 output; authoritative ID universe
- `REVIEW_XLSX` (`SB79_tod_review_reviewed_YYYY_MM_DD.xlsx`) — stale reviewed workbook with prior manual overrides
- `GPKG_TOD_STATIONS_DEV_LAYER` — used to validate carried-over `station_id` values

**Output written to Box data folder:**
- `SB79_tod_review_YYYY_MM_DD.xlsx` — reconciled workbook with today's date; ready for manual review

> **After running this notebook:**
>
> 1. Update `REVIEW_XLSX` in `config.py` to point to the new dated output file.
> 2. Open the file and resolve any remaining `conflict` or `no_match` rows (same process as after Step 2).
> 3. Save the workbook, then run Step 3.

---

## Step 3 – Station Assignment Reintegration

**Notebook:** `3_tod_station_assignment_reintegration.ipynb`

Reads the manually-reviewed Excel workbook (path set via `REVIEW_XLSX` in `config.py`), validates any manually-assigned `station_id` values against the TOD station universe, applies corrections to the development datasets, and exports the final authoritative layers to the shared GeoPackage.

**Inputs:**
- Reviewed workbook (path set via `REVIEW_XLSX` in `config.py`) — the renamed `SB79_tod_review_reviewed_YYYY_MM_DD.xlsx` file with `manual_station_assignment` rows filled in
- `tod_stations_dev`, `tod_stops_dev`, `tod_access_points_dev` — development layers from Step 2 (read from GPKG)

**Outputs written to GPKG** *(final authoritative layers):*
- `tod_stations` — final station layer (see [Pipeline Outputs](README.md#pipeline-outputs))
- `tod_stops` — final stops with all manual corrections applied (see [Pipeline Outputs](README.md#pipeline-outputs))
- `tod_access_points` — final access points with all manual corrections applied (see [Pipeline Outputs](README.md#pipeline-outputs))

> No manual review required between Steps 3 and 4.

---

## Step 4 – TOD Zone Buffer Generation

**Notebook:** `4_tod_zone_buffer_generation.ipynb`

Loads the finalized `tod_access_points` layer from the shared GeoPackage and generates the SB79 TOD zone geography through four main stages:

1. **Buffer generation** — creates full-circle Euclidean buffers at 200 ft, ¼ mile, and ½ mile around each access point, tagged with `tod_tier` and `buffer_band`.
2. **Jurisdictional population rule** — erases all buffers (200 ft, ¼ mile, ½ mile) within unincorporated county lands; additionally erases half-mile buffers within incorporated cities with total population < 35,000.
3. **Geographic priority resolution** — applies a sequential erase to produce six non-overlapping zone layers labeled by `zone_label`. See [Geographic Prioritization Approach](README.md#geographic-prioritization-approach) in Development Notes.
4. **Finalization** — dissolves by `zone_label` and explodes to single-part polygons, producing a dataset with uniform geometry types throughout.

**Inputs:**
- `tod_access_points` — finalized pedestrian access points (from Step 3)
- `tod_stations` — finalized TOD stations (from Step 3)
- `tod_stops` — finalized TOD stops (from Step 3)
- Bay Area jurisdiction boundaries with ACS 2019–2023 5-year population estimates (loaded from ArcGIS REST service)

**Outputs written to GPKG:**
- `tod_zone_buffers` — full-circle per-access-point buffers at all three distance bands; diagnostic/QA layer (see [Pipeline Outputs](README.md#pipeline-outputs))
- `jurisdictions_with_pop_acs2019_2023` — jurisdiction boundaries with ACS 2019–2023 population attributes
- `tod_zones` — authoritative SB79 TOD zone polygons, post-priority resolution (see [Pipeline Outputs](README.md#pipeline-outputs))
