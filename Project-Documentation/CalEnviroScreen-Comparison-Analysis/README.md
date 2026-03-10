# CalEnviroScreen Comparison Analysis <!-- omit in toc -->

This analysis compares Disadvantaged Community (DAC) designations between CalEnviroScreen 4.0 and Draft CalEnviroScreen 5.0, with a focus on how those designations have changed in the Bay Area — and how they align with MTC/ABAG Equity Priority Communities (EPCs).

### Table of Contents

- [Problem Statement](#problem-statement)
- [Project Resources](#project-resources)
- [Data Sources](#data-sources)
- [Analysis Parameters](#analysis-parameters)
- [Methodology](#methodology)
- [Results](#results)
- [Tags](#tags)

## Problem Statement

California's Office of Environmental Health Hazard Assessment (OEHHA) develops CalEnviroScreen (CES), a tool that ranks census tracts across the state based on cumulative environmental and health burdens. Tracts scoring in the top quartile statewide are designated as Disadvantaged Communities (DACs), which carry significant implications for funding eligibility and policy prioritization.

OEHHA's Draft CalEnviroScreen 5.0 (CES 5.0) represents a significant change in the number and distribution of DACs in the Bay Area relative to CES 4.0. Bay Area commissioners and advocates have raised concerns that the draft methodology under-represents Bay Area tracts as DACs compared to prior versions and relative to the state as a whole. To support advocacy and public comment, MTC/ABAG staff have been asked to quantify and communicate these changes clearly.

Specifically, the analysis must answer three questions:

1. **Bay Area tract comparison — CES 4.0 vs. CES 5.0:** How does the number of DAC-designated census tracts in the Bay Area change between CES 4.0 and Draft CES 5.0? What share of Bay Area tracts qualify under each version?
2. **Bay Area share of statewide DACs — CES 4.0 vs. CES 5.0:** What percentage of all statewide DAC tracts are located in the Bay Area under each version? How does this compare to the historic precedent (e.g., CES 3.0 draft: 2.8% / 56 tracts; CES 3.0 final: 105 tracts)?
3. **EPC to DAC comparison within the Bay Area:** How do MTC/ABAG Equity Priority Communities (EPCs) align with DAC-designated tracts under CES 4.0 and CES 5.0? How many EPC tracts are or are not captured by each version?

## Project Resources

- [Box — Working Files](https://mtcdrive.box.com/s/mrgek94t7vskw6cqkws980w9vrot6arl) *(internal only)*

## Data Sources

| Dataset | Source | Description |
|---|---|---|
| CalEnviroScreen 4.0 Results | [CalEnviroScreen 4.0 Results](https://data.ca.gov/dataset/calenviroscreen-4-0-results1) | Excel file with cumulative impact scores and percentile rankings for all California census tracts, based on 2010 tract boundaries |
| Draft CalEnviroScreen 5.0 Results | [Draft CalEnviroScreen 5.0 Results](https://data.ca.gov/dataset/draft-calenviroscreen-5-0) | Excel file with updated scores and rankings based on 2020 tract boundaries |
| California Census Tract Boundaries — 2010 | [U.S. Census TIGER](https://www2.census.gov/geo/tiger/TIGER2010/TRACT/2010/tl_2010_06_tract10.zip) | Official 2010 census tract geometries for California (8,057 tracts), used as the geographic denominator for CES 4.0 analysis |
| California Census Tract Boundaries — 2020 | [U.S. Census TIGER](https://www2.census.gov/geo/tiger/TIGER2020/TRACT/tl_2020_06_tract.zip) | Official 2020 census tract geometries for California (9,129 tracts), used as the geographic denominator for CES 5.0 analysis |
| 2010–2020 Census Tract Crosswalk | [NHGIS (IPUMS)](https://www.nhgis.org/geographic-crosswalks#to-census-tracts) | Population-weighted crosswalk that maps every 2010 census tract to its corresponding 2020 tract(s), accounting for boundary changes over the decade |
| Equity Priority Communities — 2018 ACS | [MTC/ABAG ArcGIS Online](https://services3.arcgis.com/i2dkYWmb4wHvYPda/arcgis/rest/services/equity_priority_communities_2025_acs2018/FeatureServer/0) | EPC designations used in Plan Bay Area 2050, based on 2010 tract boundaries |
| Equity Priority Communities — 2022 ACS | [MTC/ABAG ArcGIS Online](https://services3.arcgis.com/i2dkYWmb4wHvYPda/arcgis/rest/services/draft_equity_priority_communities_pba2050plus_acs2022a/FeatureServer/0) | Draft EPC designations for Plan Bay Area 2050+, based on 2020 tract boundaries |

## Analysis Parameters

**Disadvantaged Community (DAC)**
A census tract designated by OEHHA as a DAC if its cumulative CalEnviroScreen score falls at or above the 75th percentile statewide — meaning it ranks among the top 25% most environmentally and health-burdened communities in California. This threshold is applied separately within each CES version.

**Equity Priority Community (EPC)**
A geographic designation used by MTC/ABAG to identify census tracts with a significant concentration of underserved populations. Formerly called "Communities of Concern," EPCs are defined using eight demographic variables — including people of color, low-income households, limited English proficiency, seniors 75+, zero-vehicle households, single-parent families, people with a disability, and rent-burdened households — each with specific threshold values. A tract qualifies as an EPC if it exceeds both the low-income and people of color thresholds, or if it exceeds the low-income threshold and three or more of the remaining six variables. MTC uses the EPC framework to direct funding and prioritize investments in transportation, housing, and community services. For more information, see the [MTC Equity Priority Communities page](https://mtc.ca.gov/planning/transportation/access-equity-mobility/equity-priority-communities) and the [EPC GitHub repository](https://github.com/BayAreaMetro/Spatial-Analysis-Mapping-Projects/tree/master/Project-Documentation/Equity-Priority-Communities). Two vintages are used in this analysis: the 2018-based EPCs from Plan Bay Area 2050, and the 2022-based draft EPCs for Plan Bay Area 2050+.

**Bay Area Counties**
The nine-county San Francisco Bay Area: Alameda, Contra Costa, Marin, Napa, San Francisco, San Mateo, Santa Clara, Solano, and Sonoma.

## Methodology

The analysis is implemented in the Python notebook [ces_4_and_5_change_analysis.ipynb](ces_4_and_5_change_analysis.ipynb). The sections below describe the key steps in plain language.

### Defining DAC Status

For both CES 4.0 and CES 5.0, a tract is flagged as a DAC if its cumulative impact score percentile is **75 or above**. This is applied to the percentile columns provided in each OEHHA Excel file. The result is a simple yes/no flag for every census tract in the state.

### Geographic Harmonization

CES 4.0 is based on **2010 census tract boundaries**, while CES 5.0 uses **2020 boundaries**. Between the two decennial censuses, the Census Bureau redrew many tract boundaries — some tracts were split into multiple smaller tracts, others were merged, and most stayed the same. This means we can't directly compare CES 4.0 and CES 5.0 tract-by-tract without first bridging the two geographies.

To make a like-for-like comparison, we use a **population-weighted crosswalk** published by NHGIS. This crosswalk provides modeled interpolation weights derived from 2020 Census block-level population counts. For each pair of overlapping 2010 and 2020 tracts, the weight represents the expected proportion of the 2010 tract's population attributable to each 2020 tract. We use these population weights — rather than simpler area-based weights — to carry the CES 4.0 DAC flag forward into 2020 geography, ensuring the methodology reflects where people actually live rather than how land area is distributed.

There are four types of tract relationships in the crosswalk, classified based on how many 2020 tracts each 2010 tract maps to, and how many 2010 tracts contribute to each 2020 tract.

| Relationship | When it occurs | 2010 side | 2020 side | How DAC status is carried forward |
|---|---|---|---|---|
| **1-to-1** | Boundary unchanged — the most common case | 1 tract | 1 tract | Flag carries forward directly |
| **Split** | One tract was subdivided — common in fast-growing areas where population growth warranted finer boundaries | 1 tract (DAC or not) | 2+ tracts | Each resulting 2020 tract inherits the DAC flag if ≥50% of its population came from the source tract |
| **Merge** | Multiple tracts were consolidated — common where population is sparse or declining | 2+ tracts | 1 tract | The 2020 tract becomes a DAC if the combined population-weighted DAC share across all source tracts is ≥50% |
| **Complex** | Simultaneous splits and merges — the least common case | 2+ tracts | 2+ tracts | Same population-weighting logic as merge; each 2020 tract receives a weighted share of DAC status from all contributing 2010 tracts |


### Summary Statistics

Three sets of summary tables are produced, corresponding to the two tabs in the summary spreadsheet:

- **CES 4.0 native geography** *(Native Tract Geographies tab)* — DAC and non-DAC counts across all 8,057 California 2010 census tracts, broken down by Bay Area county and statewide totals.
- **CES 5.0 native geography** *(Native Tract Geographies tab)* — Same structure across all 9,129 California 2020 census tracts.
- **Cross-version comparison on 2020 tracts** *(Harmonized Geographies tab)* — Both the carried-forward CES 4.0 DAC flag and the CES 5.0 DAC flag are summarized on the same 2020 tract denominator (9,129 tracts), enabling a direct apples-to-apples comparison of how DAC designations changed. This is the methodologically correct comparison, as it holds geography constant across both versions.

## Results

Analysis outputs are available in the project Box folder *(internal only)*:

- [Box — Working Files](https://mtcdrive.box.com/s/mrgek94t7vskw6cqkws980w9vrot6arl)
- [Analysis Notebook](ces_4_and_5_change_analysis.ipynb)

| File | Description |
|---|---|
| [ces_comparison_database.gpkg](https://mtcdrive.box.com/s/z9eor1u66hk9mfcxulqnj4z4dmjb0xnl) | GeoPackage with one record per 2020 California census tract. Includes CES 5.0 DAC flag, CES 4.0 DAC flag carried forward to 2020 geography via population-weighted crosswalk, EPC 2050 (ACS 2018) flag carried forward, EPC 2050+ (ACS 2022) flag, county name, Bay Area classification, and four mutually-exclusive EPC/DAC overlap categories for each CES version. |
| [comparison_summary_harmonized_2020.xlsx](https://mtcdrive.box.com/s/dg4nxnijet8pjpuknypj2w2wpg8itve0) | Excel workbook with four tabs, all on the harmonized 2020 tract denominator (9,129 tracts). **CES4** — CES 4.0 DAC counts carried forward to 2020 tracts. **CES5** — CES 5.0 DAC counts on native 2020 tracts. **EPC vs CES4** — Bay Area breakdown of EPC/DAC overlap for CES 4.0 (epc_and_ces4, epc_only, ces4_only, neither). **EPC vs CES5** — Same breakdown for CES 5.0. |
| [ces_summary.xlsx](https://mtcdrive.box.com/s/8nz0zedgyo3972mz4mbqsr5a7vxtpbvd) | Excel workbook with simple DAC counts in each version's native tract geography. **CES4 (2010 tracts)** — DAC and non-DAC counts across all 8,057 California 2010 tracts. **CES5 (2020 tracts)** — DAC and non-DAC counts across all 9,129 California 2020 tracts. Both tabs are broken down by Bay Area county with Bay Area and statewide subtotals. |

## Tags

**calenviroscreen**, **disadvantaged communities**, **equity**, **bay area**, **census tracts**, **plan bay area 2050+**, **oehha**, **environmental justice**