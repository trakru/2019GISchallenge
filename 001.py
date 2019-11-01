#testing GDAL install

from osgeo import ogr
driver = ogr.GetDriverByName('GeoJSON')
print(driver)