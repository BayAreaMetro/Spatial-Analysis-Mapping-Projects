# Transit Analysis and Mapping Support for Blue Ribbon Task Force

## Analysis request:

(From [Box](https://mtcdrive.app.box.com/notes/684909665446))

- Generate a network stop and route map showing 10 min service_class for all operators
- Join headway data to route lines (JC)
- Filter out shuttle routes and other service types that we do not want to use (Cable Car, Shuttles)
- Automate the standard data deliverable for all Transit Service

**Final deliverable**: map of route service in January and June 2020 (route lines drawn by thickness of the headway metric)

**Eventually**: DV will generate a Transit and Roadway Dashboard (Long Term Support of Transit Service Analysis)

# Approach

This script returns (for the specified month and headway calculation time frame):

By route:
- number of trips
- number of stops
- headways: median, mean, and st.dev of route headways
- service_class: 10-min mean headway bracket for route

**Headway calculation months**:
- January 2020
- June 2020

**Headway calculation time periods**:
- AM peak = 6-10am
- Midday = 10am-3pm
- PM Peak = 3-7pm
- Late Night/Early Morning = 7pm-6am
- All day = 6am-6am


Output format is 5 time period files per month.
