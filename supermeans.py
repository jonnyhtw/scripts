
# coding: utf-8

# # generate 'supermeans' for validation notes

# Firstly, clear all variables in the local memory.

# In[29]:


for name in dir():
    if not name.startswith('_'):
        del globals()[name]


# Now import modules etc.

# In[30]:


import cartopy.crs as ccrs
import matplotlib
import matplotlib.pyplot as plt
import iris
import iris.plot as iplt
import iris.quickplot as qplt
import numpy as np
import datetime
from iris.time import PartialDateTime
import copy
import pickle
import iris.analysis
import netCDF4
from netCDF4 import Dataset
from braceexpand import braceexpand
import os
from pylab import *
import cartopy.crs as ccrs
import iris.analysis.cartography
import re
from os import listdir
import copy



# # creating seasonal and annual means

# In[32]:


in_dir_base='/home/williamsjh/cylc-run/'
runid='bb075'
runid='bl274'

whoami='williamsjh'

project='niwa00013'

in_dir=in_dir_base+'u-'+runid+'/share/data/History_Data/'

#in_dir = '/nesi/project/niwa00013/williamsjh/MASS/u-'+runid+'/apm.pp/'

out_dir=in_dir+'/supermeans'

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

firstyear=1951

nyears = 2

years=tuple(range(firstyear,firstyear+nyears))

type(years)

#print the years
print years

print out_dir


# In[33]:


len(years)

if len(years) == 2:
    supermeanlabel = '2'

if len(years) == 10:
    supermeanlabel = 'a'
    
if len(years) == 20:
    supermeanlabel = 'k'
    
if len(years) >= 30 and len(years) <40:
    supermeanlabel = 't'

if len(years) >= 50 and len(years) <100:
    supermeanlabel = 'l'


# In[38]:


if not os.path.exists('out_dir'):
    print 'supermean dir not there, creating it now...'
    os.makedirs('out_dir')
    print 'done'
else:
    print 'supermeans dir already there'


# In[ ]:


times = ['djf','mam','jja','son','ann']
times = ['mam','jja','son','ann']

for time in times:

    for year in years:
        if time == 'djf':
            files = list(braceexpand(out_dir+'/../*pm*{'+str(year - 1)+'dec,'+str(year)+'{jan,feb}}.pp'))
        if time == 'mam':
            files = list(braceexpand(out_dir+'/../*pm*'+str(year)+'{mar,apr,may}.pp'))
        if time == 'jja':
            files = list(braceexpand(out_dir+'/../*pm*'+str(year)+'{jun,jul,aug}.pp'))
        if time == 'son':
            files = list(braceexpand(out_dir+'/../*pm*'+str(year)+'{sep,oct,nov}.pp'))
        if time == 'ann':
            files = list(braceexpand(out_dir+'/../*pm*{'+str(year - 1)+'dec,'+str(year)+
                                     '{jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov}}.pp'))

        if year == firstyear:
            allfiles = files
        else:
            allfiles.extend(files)    

    vars = iris.load(allfiles)

    foo=copy.copy(vars)

    for i in range(len(vars)):
        foo[i] = vars[i].collapsed('time',iris.analysis.MEAN)

    iris.save(foo,out_dir+'/'+runid+'a.m'+supermeanlabel+str(years[:])+time+'.pp')


os.chdir(out_dir)

files = out_dir+'/b*.pp'

for file in glob.glob(runid+'*'):
    os.system('mule-select '+str(file)+' 1d_vars_removed_'+str(file)+' --exclude lbuser4=30464,30465,30466,30467')




