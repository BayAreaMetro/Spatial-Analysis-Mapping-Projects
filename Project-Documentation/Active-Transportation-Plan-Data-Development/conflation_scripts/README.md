Bikeway network conflation aims to match bikeway network data from various sources to the [sharedstreets network](https://github.com/sharedstreets/sharedstreets-js), based on which the Travel Model Two network was developed. Network matching requires running the shst "match" command in a Docker environment. Instructions on installing Docker can be found [here](https://www.docker.com/get-started). Instructions on creating a shs image in the Docker environment is included in step1 and step2 batch_match scripts, to be explained later.


* [step0_prepare_data_for_shst_match.ipynb](step0_prepare_data_for_shst_match.ipynb)
Does two things: 1) splits each source dataset (.geojson) into two, 'existing' facilities and 'proposed' facilities. Existing links with proposed changes are considered 'existing'. This is because different match rules will be used to match 'existing' and 'proposed' links. 2) partitions regional datasets (bact, caltrans, vta) spatially using the 14-area system (named "boundary_1" to "boundary_14") created during the TM2 networks creation process. This is because shst needs to load its base network for the area covered by the bikenetwork before running matching, and trying to load a regional network may cause docker to run out of memory.

Inputs:
	* `[source]_bike_network_epsg4326.geojson`
	* `boundary_[1-14].geojson`

Outputs:
	* `[source]_bike_network_epsg4326_exst.geojson` or `[source]_bike_network_epsg4326_exst_[1-14].geojson`: existing facilities
	* `[source]_bike_network_epsg4326_ppsd.geojson` or `[source]_bike_network_epsg4326_ppsd_[1-14].geojson`: proposed facilities


* [step1_batch_match_existing.sh](step1_batch_match_existing.sh)
Matches existing bikeway network links to shst network links using bike rules.
Run this bash script in the shst Docker container. The in-line comment explains how to build a shst image using the [Dockerfile](Dockerfile) is this folder, active the container, and run this script.
Matching methodology: first, try matching using bike rules iteratively with increased search distance: 10-meter, 20-meter, 30-meter, 40-meter, 50-meter (see this [README](https://github.com/sharedstreets/sharedstreets-js) for details on --match_bike and --search-radius=NUM); only bikeway links that failed to match with a smaller search distance enter the next round of matching with a greater distance. This ensures that a bikeway link, if there are matching shst links within 50 meters, alway gets matched to the closet shst link. Second, for the links that failed to find a matching shst link within 50 meters, try matching using car rules. 

Inputs:
   	* `[source]_bike_network_epsg4326_exst.geojson` or `[source]_bike_network_epsg4326_exst_[1-14].geojson`

Outputs (only those going into the final output are included):
	* `\existing\bike_rules_10m\[source]_bike_network_epsg4326_exst_[1-14].out.matched.geojson`
	* `\existing\bike_rules_20m\[source]_bike_network_epsg4326_exst_[1-14].out.matched.geojson`
	* `\existing\bike_rules_30m\[source]_bike_network_epsg4326_exst_[1-14].out.matched.geojson`
	* `\existing\bike_rules_40m\[source]_bike_network_epsg4326_exst_[1-14].out.matched.geojson`
	* `\existing\bike_rules_50m\[source]_bike_network_epsg4326_exst_[1-14].out.matched.geojson`
	* `\existing\car_rules_10m\[source]_bike_network_epsg4326_exst_[1-14].out.matched.geojson`
	* `\existing\car_rules_10m\[source]_bike_network_epsg4326_exst_[1-14].out.unmatched.geojson`


* [step2_batch_match_proposed.sh](step2_batch_match_proposed.sh)
Matches proposed bikeway network links to shst network links using car rules and pedestrian rules.
Matching methodology: try matching all the proposed bikeway links to shst network using car rules and pedestrian rules independently (see this [README](https://github.com/sharedstreets/sharedstreets-js) for details on --match_car and --match-pedestrian). 

Inputs:
	* `[source]_bike_network_epsg4326_ppsd.geojson` or `[source]_bike_network_epsg4326_ppsd_[1-14].geojson`

Outputs (only those going into the final output are included):
	* `\proposed\car_rules_10m\[source]_bike_network_epsg4326_exst_[1-14].out.matched.geojson`
	* `\proposed\car_rules_10m\[source]_bike_network_epsg4326_exst_[1-14].out.unmatched.geojson`
	* `\proposed\ped_rules_10m\[source]_bike_network_epsg4326_exst_[1-14].out.matched.geojson`
	* `\proposed\ped_rules_10m\[source]_bike_network_epsg4326_exst_[1-14].out.unmatched.geojson`

* [step3_aggr_match_results.ipynb](step3_aggr_match_results.ipynb)
Aggregates the matching results by data source. Each data source ends up with 4 files: existing_matched, existing_unmatched, proposed_matched, proposed_unmatched.

Inputs:
	* outputs of `step1_batch_match_existing.sh` and `step2_batch_match_proposed.sh`
Outputs:
	* `\matched\[source]_bike_network_epsg4326_exst_[1-14].out.matched.geojson`
	* `\matched\[source]_bike_network_epsg4326_ppsd_[1-14].out.matched.geojson`
	* `\unmatched\[source]_bike_network_epsg4326_exst_[1-14].out.unmatched.geojson`
	* `\unmatched\[source]_bike_network_epsg4326_ppsd_[1-14].out.unmatched.geojson`
