**Draft Status: Draft**

# Transit Oriented Communities

The Transit Oriented Communities (TOC) policy aims to increase residential and commercial densities in transit-rich areas, prioritizing affordable housing and commercial development in areas near regional transit hubs served by multiple transit providers. The goal of this analysis is to assess the baseline zoning for residential and office/commercial within Priority Development Areas (PDAs) and Transit Rich Areas (TRAs) within 1/2 mile of existing or planned fixed-guideway transit facilities. 

## Project Management 

- [Asana Task (MTC Only)](https://app.asana.com/0/304776046055605/1202042875475784/f)
- [Box Link (MTC Only)](https://mtcdrive.box.com/s/z4gzf4maxwrl25a6pelu0bjzlb8mc5a4)

## Table of Contents

## Analysis Parameters

### Transit Oriented Communities Policy Area

The proposed TOC policy will apply in the follow areas:

- PDAs or TRAs within the half-mile station/stop/terminal area of existing or planned **fixed-guideway transit**. 
- Fixed-guideway transit:
    - Regional rail: BART, Caltrain
    - Light Rail Transit: Muni Metro, VTA
    - Bus Rapid Transit: AC Transit (1T) Tempo, Van Ness BRT
    - Commuter rail: Capitol Corridor, ACE, SMART
    - Ferry terminals (limited to certain requirements only)

#### Where will the TOC Policy Apply?
The entirety or portion of a designated PDA that is within the half-mile station, stop, or terminal area. The TRA if no PDA has been designated. 

**North Berkeley BART**

North Berkeley BART: Applies to the portion of PDA within ½ mile radius

![](images/north_berkeley_bart.png)

**VTA Reamwood**

VTA Reamwood: Applies to the entire TRA within ½ mile radius

![](images/vta_reamwood.png)

## Methodology

[Transit Oriented Communities Analysis Notebook](Transit_Oriented_Communities_Analysis.ipynb)

1. Pre-procesing
    - Pull all input datasets, convert to geodataframe, and project to EPSG:26910
2. Create TOC area
    - Filter existing and planned transit stops to only include fixed-guideway stations `('Rail', 'BRT', 'Tram, Streetcar, Light Rail', 'Cable Tram','Ferry')`
    - Create 1/2 buffer (804.672 meter) area around stops
    - Create unique stop identifier
    - Flag areas with PDAs 
    - Filter out TRAs that intersect with designated PDAs, creating remainder TRAs
3. Perform point in polygon overlay
    - Calculate parcel geometry centroids 'on the surface' of the parcel
    - Spatially join parcel centroids w/ PDAs and remainder TRAs
    - Flag PDA and remainder TRA areas
    - Create area name column that indicates PDA name and remainder TRA stop area names
4. Merge parcels w/ PDA TRA flags w/ plan land use attributes
5. Calculate DUA and FAR density based on zoning or general plan designation
    - Calculate parcel area (acres / square feet)
    - Set source for residential and commercial capacities `('Zoning', 'General Plan', 'Missing Capacity')`
    - Calculate residential capacity based on source (DUA * acres)
    - Calculate commercial capacity based on source (FAR * sqft)
6. Determine where there is missing data
'Specific or Special Plan Areas',
    'Single Family Residential',
    'Multi-Family Residential',
    'Mixed Use Residential',
    'Commercial',
    'Mixed Use Commercial'
    - Determine where there is missing residential capacity. Regional zoning designations that allow residential uses: `('Specific or Special Plan Areas', 'Single Family Residential', 'Multi-Family Residential', 'Mixed Use Residential', 'Mixed Use Commercial')`
    - Determine where there is missing commercial capacity. Regional zoning designations that allow commercial uses: `('Specific or Special Plan Areas', 'Mixed Use Residential','Commercial', 'Mixed Use Commercial')` 
7. Export data for review
    - Export select columns as CSV and GeoJSON
8. Create TOC land use summaries Tableau workbook
    - [Tableau Workbook (MTC Access Only)](https://mtcdrive.box.com/s/pse3mlwq3y194vkjlspgep9gjkqcfisy)

Inputs:
- [PBA2050 Priority Development Areas](https://arcgis.ad.mtc.ca.gov/portal/home/item.html?id=85043289ac774a928e4628aa904a317c#overview)
- [Transit Stops - Existing and Planned](https://arcgis.ad.mtc.ca.gov/portal/home/item.html?id=a4e761b25425464e978829db4c3563dc)
- **Redshift Tables via query**
    - basis_staging.parcel_base_tbl
    - basis_staging.zn_base_tbl
    - basis_staging.zn_base_lot_properties
    - basis_staging.gp_base_tbl
    - basis_staging.gp_base_density

Outputs:
- [TOC Land Use Summaries Tableau Dashboard (MTC Access Only)](https://10ay.online.tableau.com/t/metropolitantransportationcommission/views/TransitOrientedCommunitiesLandUseSummaries/ResidentialandCommercialCapacitybyJurisdiction?:showAppBanner=false&:origin=viz_share_link&:display_count=n&:showVizHome=n)
- [TOC Residential and Commercial Capacities CSV (MTC Access Only)](https://mtcdrive.box.com/s/6tv583axa8jmgrzcsiuyio7phs09zbi9)
- [TOC Residential and Commercial Capacities GeoJSON (MTC Access Only)](https://mtcdrive.box.com/s/htzptkiwws90qxnxjwyysgay4ap967wh)