import iris
from braceexpand import braceexpand
import iris.plot as iplt
import iris.quickplot as qplt
import numpy as np
import glob
import datetime
import copy
import iris.analysis
import netCDF4
from netCDF4 import Dataset
import os
from pylab import *
import re
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
    print 'supermean dir not there, creating it now...'
    os.makedirs('out_dir')
    print 'done'
else:
    print 'supermeans dir already there'

################################
#do the annual mean
################################

print(in_dir)
print(out_dir)

files = list(braceexpand('all-vars-'+runid+'a.m'+supermeanlabel+str(years[-1])+'{djf,mam,jja,son}'+'.pp'))

print(files)

for file in files:

    print(file)
    
    print(out_dir+'/'+str(file)+' '+out_dir+'/1d_vars_removed_'+str(file)+' --exclude lbuser4=30464,30465,30466,30467')

    os.system('mule-select '+out_dir+'/'+str(file)+' '+out_dir+'/1d_vars_removed_'+str(file)+' --exclude lbuser4=30464,30465,30466,30467')

