import iris
import iris.quickplot as qplt
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import os

os.chdir('/nesi/nobackup/niwa00013/williamsjh/nearline/niwa00013/'+
                 'williamsjh/cylc-run/u-bl658/share/data/History_Data')

constraint =    iris.AttributeConstraint(STASH="m01s30i461")

cube = iris.load_cube('bl658a.p620141111.pp', constraint)

ax = plt.subplot(1,1,1,projection = ccrs.PlateCarree(central_longitude=180))
qplt.pcolormesh(cube[0].intersection(longitude = (50,250), latitude = (-70,0) ))
ax.set_aspect('auto')
plt.title('Daily mean water vapour path')
ax.coastlines(color = 'w')
