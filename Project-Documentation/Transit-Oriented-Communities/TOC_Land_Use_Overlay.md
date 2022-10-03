### Transit Oriented Communities Parcel/Land Use Overlay
The work documented below was exploratory work that was carried out but ultimately was not used. This work may be picked back up at a later date and the documentation here will serve as a scaffolding to restart work at a future date.

Notebook: [Transit Oriented Communities Parcel Overlay](Transit_Oriented_Communities_Parcel_Overlay.ipynb)

Inputs:
- [Transit Oriented Communities Policy Area (MTC Access Only)](https://mtcdrive.box.com/s/0ngbewx00g9m4uhwrgbx1cyr6m14jsth)
- [Parcel Atlas Parcel Geo-Lookup v2 (MTC Access Only)](https://data.bayareametro.gov/resource/5y7p-4hs4)
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


1. Perform point in polygon overlay
    - Calculate parcel geometry centroids 'on the surface' of the parcel
    - Spatially join parcel centroids w/ PDAs and remainder TRAs
    - Flag PDA and remainder TRA areas
    - Create area name column that indicates PDA name and remainder TRA stop area names
2. Merge parcels w/ PDA TRA flags w/ plan land use attributes
3. ~~Calculate DUA and FAR density based on zoning or general plan designation~~
    - ~~Calculate parcel area (acres / square feet)~~
    - ~~Set source for residential and commercial capacities `('Zoning', 'General Plan', 'Missing Capacity')`~~
    - ~~Calculate residential capacity based on source (DUA * acres)~~
    - ~~Calculate commercial capacity based on source (FAR * sqft)~~
4. Determine where there is missing data
    - Determine where there is missing residential capacity. Regional zoning designations that allow **residential uses**: `('Specific or Special Plan Areas', 'Single Family Residential', 'Multi-Family Residential', 'Mixed Use Residential', 'Mixed Use Commercial')`
    - Determine where there is missing commercial capacity. Regional zoning designations that allow **commercial uses**: `('Specific or Special Plan Areas', 'Mixed Use Residential','Commercial', 'Mixed Use Commercial')` 
5. Export data for review
    - Export select columns as CSV and GeoJSON
6. Create TOC land use summaries Tableau workbook
    - [Tableau Workbook (MTC Access Only)](https://mtcdrive.box.com/s/pse3mlwq3y194vkjlspgep9gjkqcfisy)