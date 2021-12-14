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
import multiprocessing
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
import shutil
import re
import argparse
from os import listdir
import os
import mule
import copy

import argparse

parser = argparse.ArgumentParser()
   
parser.add_argument('--year0', required=True, type=int)
parser.add_argument('--year', required=True, type=int)
parser.add_argument('--suite', required=True, type=str)
parser.add_argument('--base', required=True, type=str)

args = parser.parse_args()

print(args.year0)
print(args.year)
print(args.suite)

remove_interim_files_directory = False
generate_monthly_means = True
generate_annual_and_seasonal_means = True
generate_supermeans = False

suite = args.suite
year0= args.year0
year= args.year
base = args.base

print('the suite ID is ',suite)

user = 'williamsjh'

use_pm = True

if use_pm == True:
    stream = 'pm'
else:
    stream = 'p5'


#base = '/home/'+user+'/cylc-run/'+suite+'/share/data/History_Data/'
#base = 

def load_cube(filename):
    return iris.load(filename)

pool = multiprocessing.Pool(int(os.environ.get('NPROC',1)))





s_or_y = ['y','s','s','s','s']
suffices = ['ann.pp','djf.pp','mam.pp','jja.pp','son.pp']

stash = iris.AttributeConstraint(STASH='m01s00i024')




if not os.path.exists(base+'/climate-meaning'):
    print('creating '+'climate-meaning')
    os.makedirs(base+'/climate-meaning')
else:
    print('climate-meaning directory already exists')
os.chdir(base)

if generate_monthly_means == True:

    if not os.path.exists('interim-files-for-climate-meaning'):
        print('creating '+'interim-files-for-climate-meaning'+' directory')
        os.makedirs('interim-files-for-climate-meaning')
    else:
       print('interim-files-for-climate-meaning directory already exists')

    os.system('for file in *a.'+stream+str(year-1)+'dec*.pp *a.'+stream+str(year)+'{jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov}*.pp   ;do echo $file ; mule-select $file interim-files-for-climate-meaning/$file --include lbtim=122,24022 --exclude lbuser4=30464,30465,30466,30467; done')

else:
    pass

for j in range(len(s_or_y)):

    if generate_annual_and_seasonal_means == True:

        print('creating means for '+str(suffices[j]))

        os.chdir(base+'/interim-files-for-climate-meaning/')

        if j == 0:#ann
            files=list(braceexpand('*'+stream+'{'+str(year-1)+'dec'+','+str(year)+
                                   '{jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov}}*.pp'))
        if j == 1:#djf
            files=list(braceexpand('*'+stream+'{'+str(year-1)+'dec'+','+str(year)+
                                   '{jan,feb}}*.pp'))
        if j == 2:#mam
            files=list(braceexpand('*'+stream+str(year)+'{mar,apr,may}*.pp'))
        if j == 3:#jja
            files=list(braceexpand('*'+stream+str(year)+'{jun,jul,aug}*.pp'))
        if j == 4:#son
            files=list(braceexpand('*'+stream+str(year)+'{sep,oct,nov}*.pp'))

        print('loading all the cubes for',year,suffices[j])


        #files_with_full_path = [base+'interim-files-for-climate-meaning/' +s  for s in files]

        #cubes = pool.map(load_cube, files_with_full_path)

        cubes = iris.load(files)#,stash)

        print('now doing the meaning for ... ',suffices[j])

        #reset foo
        if 'foo' in globals():
                del foo

        foo = iris.cube.CubeList()

        for cube in cubes:
            newcube = cube.collapsed('time', iris.analysis.MEAN)
            newcube.cell_methods = (iris.coords.CellMethod('mean', 'time', intervals='1 hour'),)
            foo.append(newcube)
            outfile = suite[2:]+'a.p'+s_or_y[j]+str(year)+suffices[j]

        print('now saving '+outfile)
        iris.save(foo, base+'/climate-meaning/'+outfile)

        os.chdir(base+'/climate-meaning/')
                 
        fields=pp.fields_from_pp_file(outfile)

        for i in range(len(fields)):
            if str(fields[i].lbuser4).startswith('19') and len(str(fields[i].lbuser4)) == 5:
                print(fields[i].lbuser4)
                print('setting lbtim in STASH code '+str(fields[i].lbuser4)+' to 24022')
                fields[i].lbtim = 24022
                
        pp.fields_to_pp_file('new-'+outfile,fields)

        os.rename('new-'+outfile, outfile)

    else:
        pass

for j in range(len(s_or_y)):

    if generate_supermeans == True:

        os.chdir(base)
        os.chdir(base+'/climate-meaning/')

        os.system('pwd')

        #if not os.path.exists('supermeans'):
        #    print('creating '+'supermeans'+' directory')
        #    #os.makedirs('supermeans')
        #else:
        #    print('supermeans directory already exists')

        #if (year == year0+20) or (year == year0 + 50) or (year == year0+2):
        if (year == year0+20) or (year == year0 + 50):

            print('foo bar baz')

            if (year == year0+2):
                supermean_indicator = '2'

            if (year == year0+20):
                supermean_indicator = 'k'

            if (year == year0+50):
                supermean_indicator = 'l'

            # get filenames of files to be read in for supermeaning
            supermean_files = list()
            for i in range(year - year0):
                supermean_file = suite[2:]+'a.p'+s_or_y[j]+str(year0+1+i)+suffices[j]
                supermean_files.append(supermean_file)

            print('******')
            print(supermean_files)
            print('******')

            # get filenames of files to be read in for supermeaning after they've
            # had zero dimensional vars removed.
            #_1d_vars_removed_supermean_files = list()
            #for i in range(year - year0):
            #    _1d_vars_removed_supermean_file = '1d_vars_removed_'+suite[2:]+'a.p'+s_or_y[j]+str(year0+1+i)+suffices[j]
            #    _1d_vars_removed_supermean_files.append(_1d_vars_removed_supermean_file)

            #for file in supermean_files:
            #    print('==================')
            #    print(file)
            #    print('==================')
            #    os.system('mule-select '+str(file)+' 1d_vars_removed_'+str(file)+' --exclude lbuser4=30464,30465,30466,30467')

            print('making supermeans for these files...')
            #print(_1d_vars_removed_supermean_files)
            print(supermean_files)

            print('now loading the constituent supermean files for '+suffices[j])
            supermean_cubes = iris.load(supermean_files)

            print('now meaning the supermean files for '+suffices[j])

            #reset bar
            if 'bar' in globals():
                    del bar

            bar = iris.cube.CubeList()

            for cube in supermean_cubes:
                newcube = cube.collapsed('time', iris.analysis.MEAN)
                newcube.cell_methods = (iris.coords.CellMethod('mean', 'time', intervals='1 hour'),)
                bar.append(newcube)
                
            supermean_outfile = suite[2:]+'a.p'+supermean_indicator+str(year)+suffices[j]

            print('now saving '+supermean_outfile)
            iris.save(bar, base+'/climate-meaning/'+supermean_outfile)

            #for file in glob.glob('./1d_vars_removed*'):
            #    print(file)
            #    os.remove(file)

            supermean_fields=pp.fields_from_pp_file(supermean_outfile)

            for field in supermean_fields:
                if str(field.lbuser4).startswith('19') and len(str(field.lbuser4)) == 5:
                    print(field.lbuser4)
                    print('setting lbtim in STASH code '+str(field.lbuser4)+' to 24022')
                    field.lbtim = 24022
                    
            pp.fields_to_pp_file('new-'+supermean_outfile,supermean_fields)
            
            os.rename('new-'+supermean_outfile, supermean_outfile)

        else:
            pass

if remove_interim_files_directory == True:
    shutil.rmtree(base+'/interim-files-for-climate-meaning')
    



