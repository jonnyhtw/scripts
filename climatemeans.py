


import cartopy.crs as ccrs
import matplotlib
import matplotlib.pyplot as plt
import iris
import iris.plot as iplt
import iris.quickplot as qplt
from braceexpand import braceexpand
import numpy as np
import datetime
from iris.time import PartialDateTime
import iris.analysis
import netCDF4
from netCDF4 import Dataset
import os
from pylab import *
import cartopy.crs as ccrs
import iris.analysis.cartography
import re
from os import listdir





in_dir_base='/home/williamsjh/cylc-run/'
runid='bc048'

whoami='williamsjh'

project='niwa00013'

out_dir='/nesi/nobackup/'+project+'/'+whoami+'/esmeval/user_data/'+whoami+'/model_data/u-'+runid

print 'out_dir = '
print out_dir

in_dir=in_dir_base+'u-'+runid+'/share/data/History_Data/'

firstyear=1960

nyears=20

if not os.path.exists(out_dir+'/supermeans'):
    os.makedirs(out_dir+'/supermeans')

if len(years) == 2:
    supermeanlabel = '2'

if len(years) == 10:
    supermeanlabel = 'a'
    
if len(years) == 20:
    supermeanlabel = 'k'

if len(years) == 2:
    supermeanlabel = '2'

if len(years) >= 30 and len(years) <40:
    supermeanlabel = 't'

if len(years) >= 50 and len(years) <100:
    supermeanlabel = 'l'

fnames = list(braceexpand(in_dir+'*pm*196[1-2]*{mar,apr,may}*'))

months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

for year in range(firstyear,firstyear+nyears):

    for month in months:
        
        print str(year)+':'+str(month)

        file =  'bc048a.pm'+str(year)+str(month)+'.pp'
         
        print file

        vars = iris.load(in_dir+'/'+file)

        iris.save(vars,out_dir+'/supermeans'+'/'+runid+'a.m'+supermeanlabel+str(years[-1])+month+'.nc')
        # the m in the previous line is the 'mean' indicator, not to be
        # confused with the 'm for monthly' in the input files!
