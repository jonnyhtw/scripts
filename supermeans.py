
# coding: utf-8

# # generate 'supermeans' for validation notes

# Firstly, clear all variables in the local memory.

# In[1]:


for name in dir():
    if not name.startswith('_'):
        del globals()[name]


# Now import modules etc.

# In[1]:


import cartopy.crs as ccrs
import matplotlib
import matplotlib.pyplot as plt
import iris
import iris.plot as iplt
import iris.quickplot as qplt
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


base_dir='/home/williamsjh/cylc-run/'
runid='ai955'

full_dir=base_dir+'u-'+runid+'/share/data/History_Data/'
#full_dir='/nesi/nobackup/williamsjh/esmeval/user_data/williamsjh/model_data/u-ab747'

firstyear=1989

nyears = 20

years=tuple(range(firstyear,firstyear+nyears))

type(years)

#print the years
years


# In[3]:


len(years)

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


# In[ ]:


for period in ['ann','djf','mam','jja','son']:
    
    print period
    sys.stdout.flush()
    
    if period == 'ann':
        sys.stdout.flush()
        fnames = [full_dir+'/*py*{}*'.format(year) for year in years]
        print fnames
        sys.stdout.flush()
    else:
        fnames = [full_dir+'/*ps*{}*'.format(year)+period+'*' for year in years]
        print fnames
        sys.stdout.flush()

    native = iris.load(fnames)
    nativemean = native 
    
    for i in range(len(native)):
        nativemean[i] = native[i].collapsed('time',iris.analysis.MEAN)
    
    os.chdir(full_dir)

    if not os.path.exists(full_dir+'supermeans'):
        os.makedirs(full_dir+'supermeans')

    iris.save(nativemean,full_dir+'supermeans'+'/'+runid+'a.m'+supermeanlabel+str(years[-1])+period+'.pp')
    



