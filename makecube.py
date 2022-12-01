import iris
import iris.quickplot as qplt
import numpy as np

latitude = iris.coords.DimCoord(np.arange(-90,90), standard_name='latitude', units='degrees')
longitude = iris.coords.DimCoord(np.arange(0,360), standard_name='longitude', units='degrees')
cube = iris.cube.Cube(np.random.rand(180, 360),
                    dim_coords_and_dims=[(latitude, 0), (longitude, 1)])

cube.coord('latitude').guess_bounds()

ax = plt.subplot(1,1,1,projection = ccrs.PlateCarree())
qplt.pcolormesh(cube)

ax.coastlines(color='w')

plt.show();
