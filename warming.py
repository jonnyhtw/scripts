import matplotlib
import cf_units as unit
import numpy as np
from tqdm import tqdm
from tqdm import tqdm_gui
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import iris
import iris.analysis.cartography
import iris.quickplot as qplt
import glob
import iris

plt.ion()

#from behrens et al. (2020)...
#In the case of the NZESM the nested high‐resolution ocean model domain spans from 132.7°E to 143.7°W and 60.17°S to 10.75°S...

latmin = -60.17
latmax = -10.75
lonmin = 132.7
lonmax = 180 -143.7

start = 0
step = 5
num=int(65*360/5)
result=np.arange(0,num)*step+start

date = np.array('1950-01-01', dtype=np.datetime64, )

dates = date +result.astype(int)

files = sorted(glob.glob('/scale_wlg_persistent/filesets/project/niwa00013/williamsjh/NZESM/warming/sellevidx*bl658*.nc'))

read_data = True
#read_data = False

if read_data:

    mean = []
    
    for file in tqdm_gui(files):
        print(file)
        cube = iris.load_cube(file)
        mean.append(cube.collapsed(['latitude','longitude'],iris.analysis.MEAN).data)

flat = np.ndarray.flatten(np.array(mean))

meaning_period_in_days = 5
nyears = 65

monthly = int(30/meaning_period_in_days)
annually = int(360/meaning_period_in_days)

flatmonthly = np.convolve(flat, np.ones((monthly,))/monthly, mode='valid')
flatannually = np.convolve(flat, np.ones((annually,))/annually, mode='valid')

plt.figure()

plt.plot(np.linspace(1950,2015, flatannually.size), flatannually, 'o', alpha = 0.1)



