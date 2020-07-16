# specify desired files from each agency's GTFS feed
GTFS_FILES = ['agency',
              'calendar_dates',
              'directions',
              'feed_info',
              'routes',
              'shapes',
              'stops',
              'stop_times',
              'trips']

routes_cols = ['agency_id',
               'route_id',
               'route_short_name',
               'route_long_name',
               'route_type',
               'route_url']

trips_cols = ['route_id',
              'trip_id',
              'direction_id',
              'shape_id']

stop_times_cols = ['stop_id',
                   'trip_id',
                   'arrival_time',
                   'departure_time',
                   'stop_sequence']

# headway calculation periods
time_windows = {'am': ['06:00', '09:59'],
                'mid': ['10:00', '14:59'],
                'pm': ['15:00', '18:59'],
                'late': ['19:00', '29:59'],
                'all_6am_6am': ['06:00', '29:59'],
                'all_5am_8pm': ['05:00', '19:59']}
