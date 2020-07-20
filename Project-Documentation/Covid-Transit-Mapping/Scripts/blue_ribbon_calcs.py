"""
This tool calculates route stats


Returns (for the specified month and headway calculation time frame):

By route:
- number of trips
- number of stops
- headways: median, mean, and st.dev of route headways
- service_class: 10-min mean headway bracket for route

**Headway calculation months**:
- January 2020
- June 2020

For the **Headway calculation time periods** in config.py

Run with
    python blue_ribbon_calcs.py
"""


import sys
import getpass
user = getpass.getuser()
sys.path.insert(0, '/Users/{}/Box/DataViz Projects/Utility Code'.format(user))
from utils_io import *

from config import *
from pull_static_gtfs import *


def read_GTFS_feed(gtfs_dir):
    """
    Reads the necessary GTFS tables (trips, stop_times,
    routes) from output_dir and returns them as a dictionary of
    pandas DataFrames
    """
    gtfs_feed_dict = {}
    GTFS_tables = ['trips',
                   'stop_times',
                   'stops',
                   'routes']

    for tablename in GTFS_tables:
        fname = os.path.join(gtfs_dir,
                             '{}.csv'.format(tablename))
        gtfs_feed_dict[tablename] = pd.read_csv(fname)
    return gtfs_feed_dict


def drop_zombies(gtfs_feed_dict):
    """
    Drops "zombie" fields from the gtfs feed
    
    - Drop stop_ids and trip_ids with no stop times
    - Drop route_ids and service_ids with no trips
    
    Based on steps from 
    [GTFS Kit Drop Zombies](https://mrcagney.github.io/gtfs_kit_docs/index.html#gtfs_kit.cleaners.drop_zombies)  # noqa
    
    """
    # needs trips, stop_times, routes, stops
    try:
        trips = gtfs_feed_dict['trips']
        stop_times = gtfs_feed_dict['stop_times']
        routes = gtfs_feed_dict['routes']
        stops = gtfs_feed_dict['stops']
        
    except:
        error_msg = """gtfs_feed_dict needs trips, stop_times,
        routes, stops"""
        print(error_msg)
    
    print('Dropping zombies from feed...')

    # null_arrival_time = stop_times['arrival_time'].isnull()
    # null_departure_time = stop_times['departure_time'].isnull()

    # print('number of stop times with null arrival time: ',
    #       len(stop_times[null_arrival_time]))
    # print('number of stop times with null departure time: ',
    #       len(stop_times[null_departure_time]))

    # missing_stop_times = (stop_times[null_arrival_time
    #     | null_departure_time])
    # print('number of stop times with either null arrival or departure times: ',
    #       len(missing_stop_times))

    # stop_times_good = (stop_times
    #                    .drop(missing_stop_times.index,
    #                          axis=0)
    #                   )
    # print('number of stop times with both arrival and departure times: ',
    #       len(stop_times_good))

    # # Zombies 1: remove stop_ids with no stop times
    # print('Dropping Zombies 1: stop_ids with no stop times')
    # bad_stop_ids = (set(missing_stop_times['stop_id'].unique())
    #                 .difference(set(stop_times_good['stop_id'].unique()))
    #                )

    # print('number of stop_ids with no arrival/departure times: ',
    #       len(bad_stop_ids))
    # time_col_msg = 'number of stop_ids {} at least one arrival + departure times: '
    # print(time_col_msg.format('having'),
    #     len(stop_times_good['stop_id'].unique())
    #     )
    # print(time_col_msg.format('missing'),
    #       len(missing_stop_times['stop_id'].unique()))

    # missing_stop_times = missing_stop_times[~(missing_stop_times['stop_id']
    #   .isin(bad_stop_ids))]
    # print('''number of stop times after dropping Zombies 1
    #  (stop_ids with no stop times)''', len(missing_stop_times))
    
    # # Fix 1: Remove zombie stop_ids from stops
    # stops = stops[~stops['stop_id'].isin(bad_stop_ids)]

    # Zombies 2: remove trips with no stop times
    print('Dropping Zombies 2: trip_ids with no stop times')

    no_stop_times = (stop_times
                    .groupby('trip_id')
                    .agg({'arrival_time': check_null_group,
                          'departure_time': check_null_group})
                    .reset_index())

    no_arrival_times = no_stop_times['arrival_time'] == True
    no_departure_times = no_stop_times['departure_time'] == True

    bad_trip_ids = no_stop_times[no_arrival_times | no_departure_times]['trip_id'].unique()
    # Fix 2: Remove zombie trip_ids from trips
    trips = trips[~trips['trip_id'].isin(bad_trip_ids)]
    
    # # trip_ids with no stop times in stop_times
    # bad_trip_ids = (set(missing_stop_times['trip_id'].unique())
    #                 .difference(set(stop_times_good['trip_id'].unique()))
    #                )
    # # trip_ids with no stop times in trips
    # bad_trip_ids = (bad_trip_ids
    #   .union(set(trips['trip_id'].unique())
    #     .difference(set(stop_times_good['trip_id'].unique())))
    #   )
    # # Fix 2: Remove zombie trip_ids from trips
    # trips = trips[~trips['trip_id'].isin(bad_trip_ids)]
    
    # print('number of trip_ids with no arrival/departure times: ',
    #       len(bad_trip_ids))
    # print('number of trip_ids having at least one arrival + departure times: ',
    #       len(stop_times_good['trip_id'].unique()))
    # print('number of trip_ids missing at least one arrival + departure times: ',
    #       len(missing_stop_times['trip_id'].unique()))

    
    # missing_stop_times = missing_stop_times[~(missing_stop_times['trip_id']
    #   .isin(bad_trip_ids))]
    # print('''number of stop times after dropping Zombies 2
    #  (trip_ids with no stop times)''', len(missing_stop_times))

    
    # # Fix 3: Remove zombie trip_ids/stop_ids from stop_times
    # stop_times = pd.concat([stop_times_good, missing_stop_times],
    #                              ignore_index=True,
    #                              sort=False)
    
    # Zombies 3: remove routes with no trips
    print('Dropping Zombies 3: route_ids with no trips')
    routes_without_trips = (set(routes['route_id'].unique())
                            .difference(set(trips['route_id'].unique()))
                           )

    print('number of route_ids with no trips: ',
          len(routes_without_trips))

    # Fix 4: Remove zombie route_ids from routes
    routes = routes[~(routes['route_id']
      .isin(routes_without_trips))]
    
    
    # Replace dataframes in feed dict with cleaned versions
    gtfs_feed_dict['trips'] = trips
    gtfs_feed_dict['stop_times'] = stop_times
    gtfs_feed_dict['stops'] = stops
    gtfs_feed_dict['routes'] = routes
    
    # Print report
    gtfs_feed_dict_copy = get_dict_copy(gtfs_feed_dict)
    for k, v in gtfs_feed_dict.items():
        print('{}:  New length: {}, Old length: {}'.format(
          k,
          len(v),
          len(gtfs_feed_dict_copy[k]))
        )
    print('Zombies have been dropped from feed.')


def interpolate_stop_times(gtfs_feed_dict):
    print('Interpolating stop times...')
    stop_times = gtfs_feed_dict['stop_times']

    sort_cols = ['trip_id', 'stop_sequence']
    time_cols = ['arrival_time', 'departure_time']

    for col in time_cols:
        stop_times[col] = pd.to_timedelta(stop_times[col])

    null_arrival_time = stop_times['arrival_time'].isnull()
    null_departure_time = stop_times['departure_time'].isnull()

    print('number of stop times with null arrival time: ',
          len(stop_times[null_arrival_time]))
    print('number of stop times with null departure time: ',
          len(stop_times[null_departure_time]))

    bad_trip_ids = (stop_times[null_arrival_time | null_departure_time]
      ['trip_id'].unique()
      )

    bad_trips = (stop_times[stop_times['trip_id'].isin(bad_trip_ids)]
                                  .sort_values(by=sort_cols)
                                 .drop_duplicates()
                                 )
    # interpolate stop times for bad trips
    for col in time_cols:
        bad_trips[col] = (bad_trips
                              .groupby('trip_id')
                              .apply(lambda x:
                                interpolate_timedelta_col(x[col]))
                             ).values

    # Combined fixed (time interpolated) trips and fully non-null trips
    # to re-form stop_times
    fully_non_null_trips = stop_times[~stop_times['trip_id']
                                           .isin(bad_trips['trip_id'].unique())]
    stop_times = pd.concat([bad_trips, fully_non_null_trips],
                            ignore_index=True,
                            sort=False
                            )

    gtfs_feed_dict['stop_times'] = stop_times
    print('Stop times have been interpolated.')


def parse_time_from_time_list(time_window):
    """
    Given time_window, a list of start_time and 
    end_time strings of format HH:MM
    
    e.g. 
    
    time_window = ['06:00', '20:00']
    start_time, end_time = parse_time_from_time_list(time_window)
    
    NOTE: start_time must always be earlier than end_time.
    
    If you want to do late night to early morning service,
    specify end_time as 24H+, e.g. 3am would be '27:00'
    """
    error_msg = """Error, invalid time_window format.
                time_window must be a list containing
                start and end times of format 'HH:MM'.

                e.g. ['06:00', '20:00']
                """

    time_order_msg = """Error, invalid times.
    Start time must be less than end time."""

    try:
        start_time, end_time = [pd.Timedelta(t + ':00') for t in time_window]
        if start_time >= end_time:
            print(time_order_msg)
            return
        return start_time, end_time
    except:
        print(error_msg)
        return


def filter_location_types(gtfs_feed_dict):
    """
    SKIP
    ----
    
    Skip for now-- this removes 29165 stop_times which results in
    the exclusion of 12 routes in the final headways table
    """
    # # remove stops with location_type == 1
    # stops = gtfs_feed_dict['stops']
    # gtfs_stop_ids = stops[stops['location_type'] != 1][['stop_id']].drop_duplicates()

    # stop_times = gtfs_feed_dict['stop_times']
    # stop_times = stop_times.merge(gtfs_stop_ids)

    # gtfs_feed_dict['stops'] = stops
    # gtfs_feed_dict['stop_times'] = stop_times
    
    
def filter_stop_times_to_window(time_window, gtfs_feed_dict):
    start_time, end_time = parse_time_from_time_list(time_window)
    stop_times = gtfs_feed_dict['stop_times']
    # filter stop_times to time_window
    for t in ['arrival_time', 'departure_time']:
        stop_times[t] = pd.to_timedelta(stop_times[t])

    is_after_start_time = stop_times['arrival_time'] >= start_time
    is_before_end_time = stop_times['departure_time'] <= end_time

    stop_times = stop_times[is_after_start_time & is_before_end_time]
    
    gtfs_feed_dict['stop_times'] = stop_times


def add_route_pattern_id(gtfs_feed_dict):
    """
    Given the trips dataframe, returns a modified table with renamed
    direction_id column values and a unique route_pattern_id of format
    '{route_id}-{direction_id}' for each agency route direction (for
    headway calculations)
    """
    trips = gtfs_feed_dict['trips']

    route_pattern_src_cols = ['route_id',
                              'direction_id']

    trips[route_pattern_src_cols] = (trips[route_pattern_src_cols]
                                             .astype(str)
                                            )
    # add ids to trips
    direction_id_map = {'0': 'Outbound',
                        '1': 'Inbound'}
    trips['direction_id'] = (trips['direction_id']
        .map(direction_id_map)
        )

    # create route pattern id
    trips['route_pattern_id'] = (trips['route_id']
        + '-'
        + trips['direction_id']
        )

    # replace in gtfs_feed_dict
    gtfs_feed_dict['trips'] = trips


def filter_route_type(gtfs_feed_dict, route_types='All'):
    """
    If route_type is not 'All', filters to the given list of route_types

    Route type must a list containing one or more of these keys:

    route_type_dict = {0:'Tram, Streetcar, Light Rail',
                       1: 'Subway, Metro',
                       2: 'Rail',
                       3: 'Bus',
                       4: 'Ferry',
                       5: 'Cable Tram',
                       6: 'Aerial Lift',
                       7: 'Funicular',
                       11: 'Trollybus',
                       12: 'Monorail'
                       }
    """
    if route_types != 'All':
        print('removing all route types except {}'.format(route_types))
        gtfs_feed_dict['routes'] = (gtfs_feed_dict['routes']
          [gtfs_feed_dict['routes']['route_type']
          .isin(route_types)]
          )


def clean_GTFS_feed(gtfs_feed_dict, time_window):
    # drop zombies
    drop_zombies(gtfs_feed_dict)

    # interpolate stop times
    interpolate_stop_times(gtfs_feed_dict)

    # # remove location type 1
    # filter_location_types(gtfs_feed_dict)

    # filter stop_times to time_window
    filter_stop_times_to_window(time_window, gtfs_feed_dict)

    # add Route Pattern Id fields to trips
    add_route_pattern_id(gtfs_feed_dict)

    # filter routes to desired route type
    filter_route_type(gtfs_feed_dict, route_types='All')


def get_route_stop_agg(gtfs_feed_dict, use_arrivals, time_frame):
    """
    By route + stop:

    - number of trips
    - start times of the earliest and latest trips on the route
    - headways: maximum, minimum, and mean of the durations (in minutes) between trip starts on the route
    """
    if use_arrivals:
        sort_time_col = 'arrival_time'
    else:
        sort_time_col = 'departure_time'

    sort_cols = ['route_pattern_id',
                 'stop_id',
                 sort_time_col]

    # create headways table
    headways_table = (gtfs_feed_dict['routes'][routes_cols]
                      .merge(gtfs_feed_dict['trips'][trips_cols + ['route_pattern_id']])
                      .merge(gtfs_feed_dict['stop_times'][stop_times_cols])
                      .drop_duplicates()
                      .sort_values(by=sort_cols)
                     )

    # Aggregate route-stop stats

    # set groupby columns: route info + stop info
    gb_cols = ['route_id'] + sort_cols[:-1]

    # define aggregations
    agg_d = {sort_time_col: ['min', 'max'],
             'trip_id': 'nunique',
             'headway': ['mean', 'median', 'std',
                         'max', 'min']
            }

    # add headway as difference in time between route stops
    headways_table['headway'] = (headways_table
                     .groupby(gb_cols)[sort_time_col]
                     .diff()
                     .dt.total_seconds() / 60.0
                    )

    # # Question: is this useful to include,
    # #     or are we interested in routes that serve a stop more than once?

    # # Null headway implies the route only serves the stop once during the time window
    # # Solution: set the headway to the duration of the time window
    time_window = time_windows[time_frame]
    start_time, end_time = parse_time_from_time_list(time_window)
    time_frame_duration_mins = round((end_time - start_time).total_seconds()/60.0)
    headways_table['headway'] = (headways_table['headway']
                                 .fillna(time_frame_duration_mins)
                                 )

    # generate route stop aggregation table
    route_stop_agg = (headways_table
          .groupby(gb_cols)
          .agg(agg_d)
          .reset_index()
        )

    # Rename columns for readability

    # flatten index generated by lists of aggs in agg_d
    flatten_hierarchical_index(route_stop_agg)

    sort_time_base = sort_time_col.split('_time')[0]
    sort_time_rename_d = {'{}_min'.format(sort_time_col): 'earliest_{}'.format(sort_time_base),
                          '{}_max'.format(sort_time_col): 'latest_{}'.format(sort_time_base)}

    rename_d = {**sort_time_rename_d,
                **{'trip_id_nunique': 'num_trips'}
               }
    route_stop_agg = route_stop_agg.rename(columns=rename_d)

    # recast time cols to str
    for col in sort_time_rename_d.values():
        route_stop_agg[col] = route_stop_agg[col].map(timedelta_to_hour_str)

    return route_stop_agg


def service_class(x):
    """
    Returns the 10 minute service class a route headway falls into:
    
    10 mins or less
    11-20 mins
    21-30 mins
    31 mins or more

    e.g. service_class(129) -> 31 mins or more
    """
    if x <= 10:
        service_class = '10 mins or less'
    elif x > 10 and x <= 20:
        service_class = '11-20 mins'
    elif x > 20 and x <= 30:
        service_class = '21-30 mins'
    else:
        service_class = '31 mins or more'
    return service_class


def blue_ribbon_tp_calcs(month, time_frame):
    """
    Given a month and a time frame,
    computes the route headway stats
    """
    gtfs_dir = '511_gtfs_pull_historic_{}'.format(month)
    use_arrivals = True  # Boolean

    time_window = time_windows[time_frame]
    
    # read historic GTFS feed
    gtfs_feed_dict = read_GTFS_feed(gtfs_dir)

    # clean feed
    clean_feed_args = {'gtfs_feed_dict': gtfs_feed_dict,
                       'time_window': time_window}
    clean_GTFS_feed(**clean_feed_args)

    # create output dir
    output_dir = os.path.join('blue_ribbon_calcs', month)

    # create route stop aggregation (i.e. calculate headway stats)
    route_stop_agg = get_route_stop_agg(gtfs_feed_dict, use_arrivals, time_frame)

    route_stop_dir = os.path.join(output_dir, 'route_stop_aggs')
    makedirs_if_not_exists(route_stop_dir)
    output_fname = os.path.join(route_stop_dir, '{}_route_stop_agg.csv'.format(time_frame))
    route_stop_agg.to_csv(output_fname, index=False)

    routes_gb_cols = ['route_id']

    # create final blue ribbon agg
    blue_ribbon_agg_d = {'num_trips': 'sum',
                         'headway_median': 'mean',
                         'headway_mean': 'mean',
                         'headway_std': 'mean',
                         'stop_id': 'nunique'}

    rename_d = {'num_trips': 'total_departures',
                'headway_median': 'median_headways',
                'headway_mean': 'mean_headways',
                'headway_std': 'st_dev_headways',
                'stop_id': 'stop_count'}

    route_agg = (route_stop_agg
                 .groupby(routes_gb_cols, as_index=False)
                 .agg(blue_ribbon_agg_d)
                 .rename(columns=rename_d)
                 .round()
                )

    route_agg = route_agg[~route_agg['mean_headways'].isnull()]
    route_agg['service_class'] = route_agg['mean_headways'].map(service_class)

    output_fname = os.path.join(output_dir, '{}_blue_ribbon_calcs.csv'.format(time_frame))
    route_agg.to_csv(output_fname, index=False)


def blue_ribbon_calcs():    
    months = ['2020-01',
              '2020-06']
    for month in months:
        pull_gtfs_feed(historic=month)
        for time_frame in time_windows:
            blue_ribbon_tp_calcs(month, time_frame)


if __name__ == '__main__':
    blue_ribbon_calcs()
    
