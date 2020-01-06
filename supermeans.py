import iris
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

prefix=args.runid
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

if len(years) == 2:
    supermeanlabel = '2'

if len(years) == 3:
    supermeanlabel = '3'

if len(years) == 10:
    supermeanlabel = 'a'
    
if len(years) == 20:
    supermeanlabel = 'k'
    
if len(years) >= 30 and len(years) <40:
    supermeanlabel = 't'

if len(years) >= 50 and len(years) <100:
    supermeanlabel = 'l'

if not os.path.exists('out_dir'):
    print 'supermean dir not there, creating it now...'
    os.makedirs('out_dir')
    print 'done'
else:
    print 'supermeans dir already there'

times = ['djf','mam','jja','son','ann']

for time in times:

    print(time)

    files_grabbed = []
    for year in years:
        print('year is')
        print(year)

        if time == 'djf':
            types = (prefix+'a.pm'+str(year - 1)+'dec.pp',prefix+'a.pm'+str(year)+'jan.pp',prefix+'a.pm'+str(year)+'feb.pp')
        if time == 'mam':
            types = (prefix+'a.pm'+str(year)+'mar.pp',prefix+'a.pm'+str(year)+'apr.pp',prefix+'a.pm'+str(year)+'may.pp')
        if time == 'jja':
            types = (prefix+'a.pm'+str(year)+'jun.pp',prefix+'a.pm'+str(year)+'jul.pp',prefix+'a.pm'+str(year)+'aug.pp')
        if time == 'son':
            types = (prefix+'a.pm'+str(year)+'sep.pp',prefix+'a.pm'+str(year)+'oct.pp',prefix+'a.pm'+str(year)+'nov.pp')
        if time == 'ann':
            types = (prefix+'a.pm'+str(year - 1)+'dec.pp',prefix+'a.pm'+str(year)+'jan.pp',prefix+'a.pm'+str(year)+'feb.pp',prefix+'a.pm'+str(year)+'mar.pp',prefix+'a.pm'+str(year)+'apr.pp',prefix+'a.pm'+str(year)+'may.pp',prefix+'a.pm'+str(year)+'jun.pp',prefix+'a.pm'+str(year)+'jul.pp',prefix+'a.pm'+str(year)+'aug.pp',prefix+'a.pm'+str(year)+'sep.pp',prefix+'a.pm'+str(year)+'oct.pp',prefix+'a.pm'+str(year)+'nov.pp')

        for files in types:
            if os.path.exists(in_dir+'/'+files):
                print(in_dir+'/'+files)
                files_grabbed.extend(glob.glob(in_dir+'/'+files))
            else:
                print(in_dir+'/'+files+' does not exist!')
                quit()

    allfiles = copy.copy(files_grabbed)

    print('files_grabbed...')
    print(files_grabbed)
    print('allfiles...')
    print(allfiles)        

    vars = iris.load(allfiles)

    foo=copy.copy(vars)

    for i in range(len(vars)):
        foo[i] = vars[i].collapsed('time',iris.analysis.MEAN)

    iris.save(foo,out_dir+'/all-vars-'+runid+'a.m'+supermeanlabel+str(years[-1])+time+'.pp')

