
# coding: utf-8

# # generate 'supermeans' for validation notes

# Firstly, clear all variables in the local memory.

# In[1]:


for name in dir():
    if not name.startswith('_'):
        del globals()[name]


# Now import modules etc.

# In[2]:


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


# # creating seasonal and annual means

# In[4]:


in_dir_base='/home/williamsjh/cylc-run/'
runid='bc048'

whoami='williamsjh'

project='niwa00013'

in_dir=in_dir_base+'u-'+runid+'/share/data/History_Data/'

out_dir=in_dir+'/climate-meaning'

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

firstyear=1961

nyears = 20

years=tuple(range(firstyear,firstyear+nyears))

type(years)

#print the years
print years

print out_dir


# In[56]:


import copy

year = 1961

####

#djf
print 'doing djf'

files = list(braceexpand(out_dir+'/../*pm*{'+str(year - 1)+'dec,'+str(year)+'{jan,feb}}.pp'))

vars = iris.load(files)

foo=copy.copy(vars)

for i in range(len(vars)):
    foo[i] = vars[i].collapsed('time',iris.analysis.MEAN)

out = out_dir+'/'+runid+'a.ps'+str(year)+'djf'    
pickle.dump(foo, open(out+'.pkl', "wb" ) )    
    
iris.save(foo,out+'.pp')

###########################################################################################################################

#mam
print 'doing mam'

files = list(braceexpand(out_dir+'/../*pm*'+str(year)+'*{mar,apr,may}.pp'))

vars = iris.load(files)
foo = copy.copy(vars)

for i in range(len(vars)):
    foo[i] = vars[i].collapsed('time',iris.analysis.MEAN)
    
out = out_dir+'/'+runid+'a.ps'+str(year)+'mam'    
    
pickle.dump(foo, open(out+'.pkl', "wb" ) )    
    
iris.save(foo,out+'.pp')

###########################################################################################################################

#jja       
print 'doing jja'

files = list(braceexpand(out_dir+'/../*pm*'+str(year)+'*{jun,jul,aug}.pp'))
                         
vars = iris.load(files)
foo = copy.copy(vars)

for i in range(len(vars)):
    foo[i] = vars[i].collapsed('time',iris.analysis.MEAN)

out = out_dir+'/'+runid+'a.ps'+str(year)+'jja'    
    
pickle.dump(foo, open(out+'.pkl', "wb" ) )    
    
iris.save(foo,out+'.pp')
###########################################################################################################################

#son          
print 'doing son'

files = list(braceexpand(out_dir+'/../*pm*'+str(year)+'*{sep,oct,nov}.pp'))
                         
vars = iris.load(files)
foo = copy.copy(vars)

for i in range(len(vars)):
    foo[i] = vars[i].collapsed('time',iris.analysis.MEAN)
    

out = out_dir+'/'+runid+'a.ps'+str(year)+'son'    
pickle.dump(foo, open(out+'.pkl', "wb" ) )    
    
iris.save(foo,out+'.pp')
