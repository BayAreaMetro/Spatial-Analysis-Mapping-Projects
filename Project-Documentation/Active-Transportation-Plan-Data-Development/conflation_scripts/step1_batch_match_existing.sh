#!/bin/bash

# This script should run in a shst docker
# To build the docker image using the Dockerfile in this directory use:
# docker build -t shst .
#
# see it:
# docker image list
#
# Run a command (/bin/bash) in a new container layer over the specified image:
# docker run -it --rm -v [path to this directory]:/usr/node/ shst:latest /bin/bash
# e.g. on a Mac machine:
#     docker run -it --rm -v /Users/yuqiwang/Documents/5_work/active_transportation:/usr/node/ shst:latest /bin/bash
# e.g. on a Windows machine:
#     docker run -it --rm -v /c/Users/ywang/Documents/GitHub/Spatial-Analysis-Mapping-Projects/Project-Documentation/Active-Transportation-Plan-Data-Development:/usr/node/ shst:latest /bin/bash
# 
# First, create a folder to store match results using bike rules
# cd /usr/node/data
# mkdir -p shst_match/existing/{bike_rules_10m,bike_rules_20m,bike_rules_30m,bike_rules_40m,bike_rules_50m}
# 
# cd /.
# 
# Then you can cd to this directory, make this script executable, and run this script:
# cd /usr/node/conflation_scripts
# chmod u+x step1_batch_match_bike_rule.sh (skip this line if running on a Windows machine)
# ./step1_batch_match_existing.sh (if getting "/bin/bash^M: bad interpreter: No such file or directory" error, 
#   it means this file has Windows line endings, remove them by running "sed -i -e 's/\r$//' step1_batch_match_existing.sh" before this step)

for filename in ../data/geojson/existing/*.geojson
do
    name=$(basename "$filename" .geojson)
    echo ${name}

    echo "Matching ${name} to shst using bike routing rules 10-meter search"
    shst match ../data/geojson/existing/$name.geojson --out=../data/shst_match/existing/bike_rules_10m/$name.out.geojson --tile-hierarchy=8 --match-bike
done

for filename in ../data/shst_match/existing/bike_rules_10m/*out.unmatched.geojson
do
    name=$(basename "$filename" .geojson)
    echo ${name}

    name_split=(${name//./ })
    namebase=${name_split[0]}

    echo "Matching ${name} to shst using bike routing rules 20-meter search"
    shst match ../data/shst_match/existing/bike_rules_10m/$name.geojson --out=../data/shst_match/existing/bike_rules_20m/$namebase.out.geojson --tile-hierarchy=8 --match-bike --search-radius=20
done

for filename in ../data/shst_match/existing/bike_rules_20m/*out.unmatched.geojson
do
    name=$(basename "$filename" .geojson)
    echo ${name}

    name_split=(${name//./ })
    namebase=${name_split[0]}

    echo "Matching ${name} to shst using bike routing rules 30-meter search"
    shst match ../data/shst_match/existing/bike_rules_20m/$name.geojson --out=../data/shst_match/existing/bike_rules_30m/$namebase.out.geojson --tile-hierarchy=8 --match-bike --search-radius=30
done

for filename in ../data/shst_match/existing/bike_rules_30m/*out.unmatched.geojson
do
    name=$(basename "$filename" .geojson)
    echo ${name}

    name_split=(${name//./ })
    namebase=${name_split[0]}

    echo "Matching ${name} to shst using bike routing rules 40-meter search"
    shst match ../data/shst_match/existing/bike_rules_30m/$name.geojson --out=../data/shst_match/existing/bike_rules_40m/$namebase.out.geojson --tile-hierarchy=8 --match-bike --search-radius=40
done

for filename in ../data/shst_match/existing/bike_rules_40m/*out.unmatched.geojson
do
    name=$(basename "$filename" .geojson)
    echo ${name}

    name_split=(${name//./ })
    namebase=${name_split[0]}

    echo "Matching ${name} to shst using bike routing rules 50-meter search"
    shst match ../data/shst_match/existing/bike_rules_40m/$name.geojson --out=../data/shst_match/existing/bike_rules_50m/$namebase.out.geojson --tile-hierarchy=8 --match-bike --search-radius=50
done

for filename in ../data/shst_match/existing/bike_rules_50m/*out.unmatched.geojson
do
    name=$(basename "$filename" .geojson)
    echo ${name}

    name_split=(${name//./ })
    namebase=${name_split[0]}

    echo "Matching ${name} to shst using car routing rules"
    shst match ../data/shst_match/existing/bike_rules_50m/$name.geojson --out=../data/shst_match/existing/car_rules_10m/$namebase.out.geojson --tile-hierarchy=8 --match-car
done
