import xml.etree.ElementTree as ET
from math import radians, cos, sin, asin, sqrt


class OSMdata:
    '''
    This class extracts all the information from a .osm file in a desired area.
    You can specify the area by giving the longitude and the latitude of a specific point on the earth
    and then specify a radius around that point.
    '''
    def __init__(self, lon, lat, radius):
        self.lat = lat
        self.lon = lon
        self.radius = radius


    def haversine(self, lon1, lat1, lon2, lat2):
        '''
        Calculates the great circle distance between two points
        on the earth (specified in decimal degrees).

        :param lon1: Longitude of the first point
        :param lat1: Latitude of the first point
        :param lon2: Longitude of the second point
        :param lat2: Longitude of the second point
        :return: Returns the distance between two points in meters
        '''
        # converts decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        r = 6371 #Radius of earth in kilometers. Use 3956 for miles.
        return c * r


    def checkfunction(self):
        """
        This function first of all checks which nodes are in our desired area.
        Then retrieves the tags of these nodes. And finally, retrieves the tags
        of ways created by these nodes and relations created by all the
        nodes, ways, and relations we have so far.
        """
        osm_file = 'the name of your OSM file, e.g. map.osm'
        with open(osm_file) as fhand:
            fhand = fhand.read()
            tree = ET.fromstring(fhand)

            # Tags related to nodes:
            print('''Nodes\nHere you will see the tags derived from the nodes. Ways and relations in the following.\n\n''')
            first = tree.findall('node')
            
            # A list to store all the id's of all desired OSM elements.
            id_s = list()
            for item in first:
                distance = self.haversine(self.lon, self.lat, float(item.get('lon')), float(item.get('lat')))
                if distance <= self.radius:
                    id_s.append(item.get('id'))
                    second = item.findall('tag')
                    for item2 in second:
                        print('KEY:', item2.get('k'), ' | VALUE:', item2.get('v'))

                    # Separates tags of each node from the other nodes
                    if len(second) > 0:
                        print('-----------------------------------------------------------------------------------------\n')

            # Tags related to ways:
            print('''Ways\n''')
            repeatid = list() # A list to find the repeated id's to avoid printing
            repeatid.append('a')
            first = tree.findall('way')
            for item in first: # Looping through ways
                wayid = item.get('id') # The way's id
                second = item.findall('nd')
                if all(t != wayid for t in repeatid):
                    for item2 in second: # Looping through nd's
                        third = item2.get('ref')
                        if any( i == third for i in id_s): # Looping through our id list from before
                            id_s.append(wayid) # Add the way id to our id list
                            repeatid.append(wayid) # So that we don't print it anymore
                            fourth = item.findall('tag')
                            for item3 in fourth:
                                print('KEY:', item3.get('k'), ' | VALUE:', item3.get('v'))

                            # Separates tags of each way from the other ways
                            if len(fourth) > 0:
                                print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
                            break

            # Tags related to relations:
            print('''Relations\n''')

            # A list to find the repeated id's to avoid printing
            repeatid = list()
            repeatid.append('a')
            first = tree.findall('relation')
            for item in first:
                relationid = item.get('id') #The relation's id
                second = item.findall('member')
                if all(t != relationid for t in repeatid):
                    for item2 in second: # Looping through member's
                        third = item2.get('ref')
                        for i in id_s: # Looping through our id list from before
                            if third == i:
                                id_s.append(relationid) # Add the relation id to our id list
                                repeatid.append(relationid)  # So that we don't print it anymore
                                fourth = item.findall('tag') # The problem is in here!!!
                                for item3 in fourth:
                                    print('KEY:', item3.get('k'), ' | VALUE:', item3.get('v'))

                                # Separates tags of each relation from the other relations
                                if len(fourth) > 0:
                                    print('------------------------------------------------------------------------------\n')
                                break



if __name__ == "__main__":
    user_lat = input('Enter your desired latitude, e.g. 49.6048488: ')
    user_lat = float(user_lat)
    user_lon = input('Enter your desired longitude: ')
    user_lon = float(user_lon)
    user_radius = input('Enter your desired radius in meters: ')
    user_radius = float(user_radius)

    osm = OSMdata(user_lon, user_lat, user_radius)
    osm.checkfunction()