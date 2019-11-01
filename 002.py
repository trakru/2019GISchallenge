#loading ne_50m_populated places dataset

#importing modules, setting paths
import sys
from osgeo import ogr
fn = r'G:\gis\geoprocessing with python\data\osgeopy-data\osgeopy-data\global\ne_50m_populated_places.shp'
ds = ogr.Open(fn, 0)  # change to (fn, 1) to open in update mode

# opening the data source
if ds is None:
    sys.exit(f"could not open {fn}")
lyr = ds.GetLayer(0)

# opening file attributes
i = 0
for feat in lyr:
    pt = feat.geometry()
    x = pt.GetX()
    y = pt.GetY()
    name = feat.GetField('NAME')
    pop = feat.GetField('POP_MAX')
    print(name, pop, x, y)
    i += 1
    if i == 20:
        break

# Get Feature count
# num_features = lyr.GetFeatureCount()
# print(num_features)

del ds

