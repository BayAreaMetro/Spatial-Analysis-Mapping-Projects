# Where Americans Talk About Climate Change

[Asana Project](https://app.asana.com/0/152661557501438/353985243507815/f)   

### Goal  

Reproduce this map featured in the New York Times using the original source data:  

![discuss_global_warming_occasionally](https://github.com/MetropolitanTransportationCommission/motm/blob/master/2017_07/images/discuss_global_warming_occasionally.PNG)

[New York Times Article - Last Map in Article](https://www.nytimes.com/interactive/2017/03/21/climate/how-americans-think-about-climate-change-in-six-maps.html?_r=0)

### Contents 

[Data Sources](#data-sources)  
[Methodology](#methodology)  
[Outcome & Products](#outcome--products)

### Data Sources 

Yale Climate Change Opinion Maps Data

- [excel spreadsheet--counties and states](https://mtcdrive.box.com/s/7odg20r86bndq5g05ha4fwj77cmuwwnb)   

- [metadata for spreadsheet](https://mtcdrive.box.com/s/u1lohwqelc7q0sg5pmv18k2m3dcloj1p)   

### Methodology  

see `R/join_yale_data_to_census_geometries.R` for string and integer processing to join the Yale survey spreadsheet to the census 2015 geometries.   

### Outcome & Products 

[File Geodatabase of Census County geometries joined to Yale survery data](https://mtcdrive.box.com/s/evpgx7v506p4p2xsnmbk0zdf6dr1mq8x)  

Tables included:  

- yale_climate_census_needed_columns - contains just the data needed for the map of the month   
- yale_climate_census_all_columns - contains all the columns in the source data from the yale survey. note that all of the vowels have been stripped from column names. please use the metadata link in the source above to look up these columns if needed.    

#### Maps, Charts, and Graphics 

- [Image Files](https://mtcdrive.box.com/s/m1mcx2nqb27t2z84u63p3uqb8v5ui7hg)
  - [US opinions on climate change.pdf (website)](https://mtcdrive.box.com/s/8xjwcaswzc7tf3xj12gi79e88tmx2r8f)
  - [US opinions on climate change.png (website)](https://mtcdrive.box.com/s/2c7b4ee2ycxly1mpuod5qppyyxk3dmbb)
  - [US opinions on climate change ED.pdf (Executive Director's Report)](https://mtcdrive.box.com/s/vc9q121rw5wwqi9d0d26thipjb5njfxt)
    - [US opinions on climate change ED.png (Executive Director's Report)](https://mtcdrive.box.com/s/l2sugy33a7fkcnxuv31kdqx8x5vcdmt2)
- [Illustrator Files](https://mtcdrive.box.com/s/8ikn0ileqtt26rboa7s75c6oe9gvikuf)
- [Commission Presentation Files](https://mtcdrive.box.com/s/wa7vfsithvfx3urou0hd45tx23hx14aj)

#### Written Material

[July 2017 Map of the Month Write - Up](https://mtcdrive.box.com/s/sppctakv4puwun43d0rp84e0ydnsokmo) 
