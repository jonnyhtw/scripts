

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
import copy

suite = sys.argv[1]
year0=int(sys.argv[2])
year=int(sys.argv[3])

print 'the suite ID is ',suite


user = 'williamsjh'


base = '/home/'+user+'/cylc-run/'+suite+'/share/data/History_Data/'

os.chdir(base)

if not os.path.exists('interim-files-for-climate-meaning'):
    print('creating '+'interim-files-for-climate-meaning'+' directory')
    os.makedirs('interim-files-for-climate-meaning')
else:
    print('interim-files-for-climate-meaning directory already exists')

os.chdir(base)

#os.system('for file in *a.pm'+str(year-1)+'dec*.pp *a.pm'+str(year)+'{jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov}*.pp   ;do echo $file ; mule-select $file interim-files-for-climate-meaning/$file --include lbtim=122,24022 ; done')

os.chdir(base)
import os
if not os.path.exists(base+'/climate-meaning'):
    print('creating '+'climate-meaning')
    os.makedirs(base+'/climate-meaning')
else:
    print('climate-meaning directory already exists')

sory = ['y','s','s','s','s']
suffices = ['ann.pp','djf.pp','mam.pp','jja.pp','son.pp']

stash = iris.AttributeConstraint(STASH='m01s00i024')


for j in range(len(sory)):

    print 'creating means for '+str(suffices[j])

    os.chdir(base+'interim-files-for-climate-meaning/')

    if j == 0:#ann
        files=list(braceexpand('*pm'+'{'+str(year-1)+'dec'+','+str(year)+
                               '{jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov}}*.pp'))
    if j == 1:#djf
        files=list(braceexpand('*pm'+'{'+str(year-1)+'dec'+','+str(year)+
                               '{jan,feb}}*.pp'))
    if j == 2:#mam
        files=list(braceexpand('*pm'+str(year)+'{mar,apr,may}*.pp'))
    if j == 3:#jja
        files=list(braceexpand('*pm'+str(year)+'{jun,jul,aug}*.pp'))
    if j == 4:#son
        files=list(braceexpand('*pm'+str(year)+'{sep,oct,nov}*.pp'))

    print 'loading all the cubes for',year,suffices[j]

    cubes = iris.load(files)#,stash)

    print 'now doing the meaning for ... ',suffices[j]                          

    #reset foo
    if 'foo' in globals():
            del foo

    foo = iris.cube.CubeList()

    for cube in cubes:
        newcube = cube.collapsed('time', iris.analysis.MEAN)
        newcube.cell_methods = (iris.coords.CellMethod('mean', 'time', intervals='1 hour'),)
        foo.append(newcube)
        outfile = suite[2:]+'a.p'+sory[j]+str(year)+suffices[j]

    print 'now saving '+outfile
    iris.save(foo, base+'/climate-meaning/'+outfile)

    os.chdir(base+'/climate-meaning/')
             
    fields=pp.fields_from_pp_file(outfile)

    for i in range(len(fields)):
        if str(fields[i].lbuser4).startswith('19') and len(str(fields[i].lbuser4)) == 5:
            print fields[i].lbuser4
            print 'setting lbtim in STASH code '+str(fields[i].lbuser4)+' to 24022'
            fields[i].lbtim = 24022
            
    pp.fields_to_pp_file('new-'+outfile,fields)

    os.rename('new-'+outfile, outfile)

    os.chdir(base)



