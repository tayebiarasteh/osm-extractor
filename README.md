## Extracting necessary information defined by the user from the OpenStreetMap


[OpenStreetMap](https://www.openstreetmap.org/) (OSM) is a map of the world, created by people like you and free to use under an open license.

To download the OSM data for a specific region in the world, you can click [here](https://www.openstreetmap.org/export) and then click export. However, if you need to download a map of an area consisting more than 50000 nodes, you should visit their [planet](https://planet.openstreetmap.org/) website.

### Data structure
The downloaded files will be in the **XML** form and with `.osm` extension. You can refer to `sample_map.osm` as an example, which shows an area in Erlangen, Germany.
Also, the OpenStreetMap describes the world with 3 major elements,
1. **Node:** Every node indicates a point in the world.
2. **Way:** A combination of multiple nodes, which create an open curve, e.g. a highway.
3. **Relation:** A combination of all the 3 elements, e.g. a building.

### Goal of this project 

Every single element with its information in a given area will be extracted. Then related elements will be grouped together to identify an object. Doing so, we can recognize every object (of course if it is mentioned in the OpenStreetMap), with its further information given by people, in any area of the world.
