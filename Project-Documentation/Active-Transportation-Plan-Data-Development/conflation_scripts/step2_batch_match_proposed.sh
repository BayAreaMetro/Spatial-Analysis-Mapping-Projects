#!/bin/bash

# This script should run in a shst docker
# If run immediately after running step1_batch_match_bike_rules.sh, skip the instructions before line 13
# 
# Run a command (/bin/bash) in a new container layer over the specified image:
# docker run -it --rm -v [path to this directory]:/usr/node/ shst:latest /bin/bash
# e.g. on a Mac machine:
#     docker run -it --rm -v /Users/yuqiwang/Documents/5_work/active_transportation:/usr/node/ shst:latest /bin/bash
# e.g. on a Windows machine:
#     docker run -it --rm -v /c/Users/ywang/Documents/GitHub/Spatial-Analysis-Mapping-Projects/Project-Documentation/Active-Transportation-Plan-Data-Development:/usr/node/ shst:latest /bin/bash
# 
# First, create a folder to store match results using car rules
# cd /usr/node/data
# mkdir -p shst_match/proposed/{car_rules_10m,ped_rules_10m}
# 
# cd /.
# 
# Then you can cd to this directory, make this script executable, and run this script:
# cd /usr/node/conflation_scripts
# chmod u+x step2_batch_match_proposed.sh (skip this line if running on a Windows machine)
# ./step2_batch_match_proposed.sh (if getting "/bin/bash^M: bad interpreter: No such file or directory" error, 
#   it means this file has Windows line endings, remove them by running "sed -i -e 's/\r$//' step2_batch_match_proposed.sh" before this step)

for filename in ../data/geojson/proposed/*.geojson
do
    name=$(basename "$filename" .geojson)
    echo ${name}

    echo "Matching ${name} to shst using car rules"
    shst match ../data/geojson/proposed/$name.geojson --out=../data/shst_match/proposed/car_rules_10m/$name.out.geojson --tile-hierarchy=8  --match-car
    echo "Matching ${name} to shst using pedestrian rules"
    shst match ../data/geojson/proposed/$name.geojson --out=../data/shst_match/proposed/ped_rules_10m/$name.out.geojson --tile-hierarchy=8  --match-pedestrian
done
