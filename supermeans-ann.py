import iris
from braceexpand import braceexpand
import iris.plot as iplt
import iris.quickplot as qplt
import numpy as np
import glob
import datetime
from iris.time import PartialDateTime
import copy
import iris.analysis
import netCDF4
from netCDF4 import Dataset
import os
from pylab import *
import re
from os import listdir
import argparse
import copy

parser = argparse.ArgumentParser()
   
parser.add_argument('--nyears', required=True, type=int)
parser.add_argument('--firstyear', required=True, type=int)
parser.add_argument('--runid', required=True, type=str)
parser.add_argument('--prefix', required=True, type=str)
parser.add_argument('--in_dir', required=True, type=str)
args = parser.parse_args()

runid=args.runid
print('runid is', runid)

prefix=args.prefix
print('raw data file prefix is ', prefix)

in_dir=args.in_dir
print('in_dir is', in_dir)

out_dir=in_dir+'/supermeans/'

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

firstyear=args.firstyear
print('firstyear is', firstyear)

nyears = args.nyears
print('nyears is', nyears)

print('%%%%%%%%%%%%%%%%%%')
print('nyears = ', nyears)
print('%%%%%%%%%%%%%%%%%%')

years=tuple(range(firstyear,firstyear+nyears))

if len(years) <= 9:
    supermeanlabel = str(len(years))
elif len(years) <= 10:
    supermeanlabel = 'a'
elif len(years) <= 19:
    supermeanlabel = 'b'
elif len(years) <= 24:
    supermeanlabel = 'k'
elif len(years) <= 29:
    supermeanlabel = 's'
elif len(years) <= 39:
    supermeanlabel = 't'
elif len(years) <= 49:
    supermeanlabel = 'q'
elif len(years) <= 99:
    supermeanlabel = 'l'
elif len(years) <= 249:
    supermeanlabel = 'u'
elif len(years) <= 499:
    supermeanlabel = 'w'
else:
    supermeanlabel = 'd'

print('%%%%%%%%%%%%%%%%%%')
print('supermeanlabel = ', supermeanlabel)
print('%%%%%%%%%%%%%%%%%%')

if not os.path.exists('out_dir'):
    print('supermean dir not there, creating it now...')
    os.makedirs('out_dir')
    print('done')
else:
    print('supermeans dir already there')

################################
#remove 1d vars
################################

print(in_dir)
print(out_dir)

print('now loading all seasons')

all_seasons_files = list(braceexpand(out_dir+'/1d_vars_removed_all-vars-'+runid+'a.m'+supermeanlabel+str(years[-1])+'{djf,mam,jja,son}'+'*.pp'))

print(all_seasons_files)

cubes = iris.load(all_seasons_files)

print('now creating annual mean')
bar = iris.cube.CubeList()
for cube in cubes:
    print(cube)
    newcube = cube.collapsed('time', iris.analysis.MEAN)
    bar.append(newcube)

iris.save(bar,out_dir+'/1d_vars_removed_all-vars-'+runid+'a.m'+supermeanlabel+str(years[-1])+'ann.pp')

os.system('rename 1d_vars_removed_all-vars-'+runid+' '+runid+' '+out_dir+'/1d_vars_removed_all-vars-'+runid+'*.pp')
