import cartopy.crs as ccrs
import matplotlib
import matplotlib.pyplot as plt
import iris
import iris.plot as iplt
import iris.quickplot as qplt
from braceexpand import braceexpand
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

if nyears == 2:
    supermeanlabel = '2'

if nyears == 10:
    supermeanlabel = 'a'
    
if nyears == 20:
    supermeanlabel = 'k'

if nyears == 2:
    supermeanlabel = '2'

if nyears >= 30 and nyears <40:
    supermeanlabel = 't'

if nyears >= 50 and nyears <100:
    supermeanlabel = 'l'

fnames = list(braceexpand(in_dir+'*pm*{196[0-9],197[0-9]}*{mar,apr,may}*'))

period = 'mam'

print fnames

vars = iris.load(fnames)

#varsmean = vars.collapsed('time',iris.analysis.MEAN)

#iris.save(varsmean,out_dir+'/supermeans'+'/'+runid+'a.m'+supermeanlabel+str(year)+period+'.pp')
        # the m in the previous line is the 'mean' indicator, not to be
        # confused with the 'm for monthly' in the input files!
