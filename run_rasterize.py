gdal_rasterize -l "D:/Avi/New simulation/geo2 14a/Inundation Boundary (06MAY2014 00 00 00 Value_0)" -burn 1.0 -tr 5.0 5.0 -a_nodata 0.0 -te 388750.5094038011 7955412.783876576 442771.6455172393 8042954.577095281 -ot Float32 -of GTiff "D:/Avi/New simulation/geo2 14a/Inundation Boundary (06MAY2014 00 00 00 Value_0).shp" "D:/Avi/New simulation/result flood map/result_13c.tif"