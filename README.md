## Extracting necessary information defined by the user from the OpenStreetMap

### By [Soroosh Tayebi Arasteh](https://github.com/starasteh) | سروش طیبی آراسته

[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)
[![](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/starasteh/osm-extractor/pulls)


[OpenStreetMap](https://www.openstreetmap.org/) (OSM) is a map of the world, created by people like you and free to use under an open license.

To download the OSM data for a specific region in the world, you can click [here](https://www.openstreetmap.org/export) and then click export. However, if you need to download a map of an area consisting more than 50000 nodes, you should visit their [planet](https://planet.openstreetmap.org/) website.

Conducted at the [Chair of Information Technology (Communication Electronics), Navigation and Localization group, Prof. Dr.-Ing. Jörn Thielecke](https://www.like.tf.fau.de/) of the [Electical Engineering Department](https://www.eei.tf.fau.de/) at [University of Erlangen-Nuremberg (FAU)](https://www.fau.eu/).


### Data structure
The downloaded files will be in the **XML** form and with `.osm` extension. You can refer to `sample_map.osm` as an example, which shows an area in Erlangen, Germany.

Also, the OpenStreetMap describes the world with 3 major elements,
1. **Node:** Every node indicates a point in the world.
2. **Way:** A combination of multiple nodes, which creates an open curve, e.g. a highway.
3. **Relation:** A combination of all the 3 elements, e.g. a building.

### Goal of this mini project 

Every single element with its information in a given area will be extracted. Then related elements will be grouped together to identify an object. Doing so, we can recognize every object (of course if it is mentioned in the OpenStreetMap), with its further information given by people, in any area of the world.

### Contributions needed!

As you can understand from the above explanation, the improvement potential of this project is non-ending, so feel free to fork it!
