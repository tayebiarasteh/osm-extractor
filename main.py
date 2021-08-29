'''
@author: Soroosh Tayebi Arasteh <soroosh.arasteh@fau.de>
https://github.com/tayebiarasteh/
'''
from OSMdata import OSMdata



def main(user_lon=11.8764, user_lat=49.6048488,
         user_radius=50, osm_file_n='sample_map.osm'):
    '''
    :param user_lon: your desired longitude, e.g. 11.8764.
    :param user_lat: your desired latitude, e.g. 49.6048488.
    :param user_radius: your desired radius in meters.
    :param osm_file_n: the name of your OSM file, e.g. "sample_map.osm".
    :return: A list of dictionaries of extracted information.
    '''
    osm = OSMdata(user_lon, user_lat, user_radius, osm_file_n)
    osm.node_extractor()
    osm.way_extractor()
    results = osm.rel_extractor()
    return results




if __name__ == '__main__':
    results = main(11.8764, 49.6048488, 500, 'sample_map.osm')

    # osm = OSMdata(11.0, 49.0, 500.0, 'sample_map.osm')
    # osm.node_extractor()
    # osm.way_extractor()
    # results = osm.rel_extractor()
    # for node in results:
    #     print(node)
    #     for key in node:
    #         if not key == None:
    #             print(key + ':', node[key])
    #     # Separates tags of each node from the other nodes
    #     print('--------------------------------------'
    #           '-------------------------------------------\n')
