#importing modules, setting paths
import sys
from osgeo import ogr
fn = r'G:\gis\geoprocessing with python\data\osgeopy-data\osgeopy-data\global\ne_50m_populated_places.shp'
ds = ogr.Open(fn, 0)  # change to (fn, 1) to open in update mode

# opening the data source
if ds is None:
    sys.exit(f"could not open {fn}")
lyr = ds.GetLayer(0)

# print the extent of the shapefile
extent = lyr.GetExtent()
print(extent)

# print all attribute fields
for field in lyr.schema:
    print(field.name, field.GetTypeName())