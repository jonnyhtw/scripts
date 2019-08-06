

#Usage `python py-for-afterburner.dev.py u-bl274 1950 1964`
# that is, suite ID, first year, current year


import cartopy.crs as ccrs
import matplotlib
import matplotlib.pyplot as plt
import glob

import mule.pp as pp

import subprocess
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
import numpy as np
import matplotlib.pyplot as plt

from braceexpand import braceexpand

import numpy as np
import  copy
import matplotlib.pyplot as plt
from pylab import *
import cartopy.crs as ccrs
import os
import iris.analysis.cartography
import re
import argparse
from os import listdir
import mule

suite = sys.argv[1]
year0=int(sys.argv[2])
year=int(sys.argv[3])

print 'the suite ID is ',suite


user = 'williamsjh'


base = '/home/'+user+'/cylc-run/'+suite+'/share/data/History_Data/'

os.chdir(base)

if not os.path.exists('lbtim122and24022'):
    print('creating '+'lbtim122and24022'+' directory')
    os.makedirs('lbtim122and24022')
else:
    print('lbtim122and24022 directory already exists')

os.chdir(base)


os.system('for file in *a.pm'+str(year-1)+'dec*.pp *a.pm'+str(year)+'{jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov}*.pp   ;do echo $file ; mule-select $file lbtim122and24022/$file --include lbtim=122,24022 ; done')

os.chdir(base)
import os
if not os.path.exists(base+'/climate-meaning/lbtim122and24022'):
    print('creating '+'climate-meaning/lbtim122and24022')
    os.makedirs(base+'climate-meaning/lbtim122and24022')
else:
    print('climate-meaning/lbtim122and24022 directory already exists')

os.chdir(base+'lbtim122and24022/')

print year
foo = iris.cube.CubeList()
files=list(braceexpand('*pm'+'{'+str(year-1)+'dec'+','+str(year)+
                       '{jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov}}*.pp'))
cubes = iris.load(files)
print files                           
for cube in cubes:
    newcube = cube.collapsed('time', iris.analysis.MEAN)
    newcube.cell_methods = (iris.coords.CellMethod('mean', 'time', intervals='1 hour'),)
    foo.append(newcube)
    outfile = suite[2:]+'a.py'+str(year)+'ann.pp'

print 'now saving '+outfile
iris.save(foo, base+'/climate-meaning/lbtim122and24022/'+outfile)

os.chdir(base+'/climate-meaning/lbtim122and24022/')
         
for file in sorted(glob.glob('*.pp')):

    fields=pp.fields_from_pp_file(file)

    for i in range(len(fields)):
        if str(fields[i].lbuser4).startswith('19') and len(str(fields[i].lbuser4)) == 5:
            #print fields[i].lbuser4
            #print 'setting lbtim in STASH code '+str(fields[i].lbuser4)+' to 24022'
            fields[i].lbtim = 24022
            
    pp.fields_to_pp_file('new-'+file,fields)

os.system('rename new-b b new-b*')

