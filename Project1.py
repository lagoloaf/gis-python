#Creates contour feature for Fox Lake Quadrangle DEM and publishes on disk

import arcpy

#Define raster location (replace backslashes with forward slashes)
dem_raster = "C:/Users/space/OneDrive/Desktop/GEOG 485 PSU/Project 1 Content/Lesson1/foxlake"

#Run arcpy Contour function and save to disk
contour_result = arcpy.sa.Contour(dem_raster, 'dem_contours', 25, 0)
contour_result.save("C:/Users/space/OneDrive/Desktop/GEOG 485 PSU/Project 1 Content/Lesson1/dem_contours.shp")

### This code will not run in PyScripter without perms to use the sa package in arcpy. To get around this, an alternative for lines 9 and 10 would be:
### arcpy.Contour_3d(dem_raster, "C:/Users/space/OneDrive/Desktop/GEOG 485 PSU/Project 1 Content/Lesson1/dem_contours.shp", 25, 0)