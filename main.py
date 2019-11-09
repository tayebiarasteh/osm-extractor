from OSMdata import OSMdata

'''Just run this file'''

osm_file_n = input('the name of your OSM file, e.g. map.osm: ')
user_lat = input('Enter your desired latitude, e.g. 49.6048488: ')
user_lat = float(user_lat)
user_lon = input('Enter your desired longitude, e.g. 11.8764: ')
user_lon = float(user_lon)
user_radius = input('Enter your desired radius in meters: ')
user_radius = float(user_radius)

osm = OSMdata(user_lon, user_lat, user_radius, osm_file_n)
osm.checkfunction()