import sys
import os
from osgeo import ogr
data_dir = 'G:\gis\geoprocessing with python\data\osgeopy-data\osgeopy-data'
fn = os.path.join(data_dir, 'Washington', 'large_cities.geojson')

ds = ogr.Open(fn, 0)
lyr = ds.GetLayer(0)

# find geometry attributes by boolean logic

print(lyr.GetGeomType() == ogr.wkbPoint)
print(lyr.GetGeomType() == ogr.wkbPolygon)

# Human readable string for geometry

feat = lyr.GetFeature(0)
print(feat.geometry().GetGeometryName())

# information about attribute fields attached to a layer
for field in lyr.schema:
    print(field.name, field.GetTypeName())