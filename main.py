from OSMdata import OSMdata

'''Just run this file'''

osm_file_n = input('the name of your OSM file, e.g. sample_map.osm: ')
user_lon = input('Enter your desired longitude, e.g. 11.8764: ')
user_lon = float(user_lon)
user_lat = input('Enter your desired latitude, e.g. 49.6048488: ')
user_lat = float(user_lat)
user_radius = input('Enter your desired radius in meters: ')
user_radius = float(user_radius)

osm = OSMdata(user_lon, user_lat, user_radius, osm_file_n)
osm.node_extractor()
osm.way_extractor()
results = osm.rel_extractor()


# osm = OSMdata(11.0, 49.0, 500.0, 'sample_map.osm')
# osm.node_extractor()
# osm.way_extractor()
# results = osm.rel_extractor()

# for node in results:
#     print(node)
#     for key in node:
#         if not key == None:
#             print(key + ':', node[key])
#
#     # Separates tags of each node from the other nodes
#     print('---------------------------------------------------------------------------------\n')
#
