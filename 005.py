# Edit existing data/create new data

import sys
import os
from osgeo import ogr
data_dir = 'G:\gis\geoprocessing with python\data\osgeopy-data\osgeopy-data'
fn = os.path.join(data_dir, 'global')

# open source folder for writing
ds = ogr.Open(fn, 1)  # opening in edit mode (kwarg = 1)
in_lyr = ds.GetLayer('ne_50m_populated_places')


if ds.GetLayer('capital_cities'):
    ds.DeleteLayer('capital_cities')  # delete layer if exists
out_lyr = ds.CreateLayer('capital_cities',
                         in_lyr.GetSpatialRef(),
                         ogr.wkbPoint)  # creating a point layer
out_lyr.CreateFields(in_lyr.schema)

# Creating a blank Feature

out_defn = out_lyr.GetLayerDefn()
out_feat = ogr.Feature(out_defn)

# Copy geometry based on if conditional

for in_feat in in_lyr:
    if in_feat.GetField('FEATURECLA') == 'Admin-0 capital':
        geom = in_feat.geometry()
        out_feat.SetGeometry(geom)
        for i in range(in_feat.GetFieldCount()):
            value = in_feat.GetField(i)
            out_feat.SetField(i, value)
        out_lyr.CreateFeature(out_feat)

del ds  # Close files