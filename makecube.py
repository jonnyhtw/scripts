import iris
import iris.quickplot as qplt
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-180,180)
y = np.arange(-90,90)

xx,yy=np.meshgrid(x,y)

arr = np.multiply(xx,yy)

latitude = iris.coords.DimCoord(y, standard_name='latitude', units='degrees')
longitude = iris.coords.DimCoord(x, standard_name='longitude', units='degrees')
cube = iris.cube.Cube(arr,
                    dim_coords_and_dims=[(latitude, 0), (longitude, 1)])

cube.coord('latitude').guess_bounds()

ax = plt.subplot(1,1,1,projection = ccrs.PlateCarree())
qplt.pcolormesh(cube)
qplt.contour(cube, colors = 'k')
plt.title('latitude * longitude')

ax.coastlines(color='w')

plt.show();

