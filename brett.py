import iris
import numpy as np
import glob, os

suite = 'u-bl658'

stash = ['m01s16i222','m01s05i216','m01s00i024']

hourly_constraint = iris.Constraint(cube_func=lambda cube: cube.cell_methods[0].intervals[0]=="1 hour")

for i in range(len(stash)):

    print(i)
    print(stash[i])

    stash_constraint = iris.AttributeConstraint(STASH=stash[i])

    files = sorted(glob.glob('/home/williamsjh/cylc-run/'+suite+'/share/data/History_Data/*a.pm*1950*.pp'))
    print(files)

    #if stash[i] == 'm01s05i216' or stash[i] == 'm01s00i024':
    #    print('i am in the if statement')
    #    cubes = iris.load(files, stash_constraint & hourly_constraint)
    #else:
    #    print('i am in the else statement')
    cubes = iris.load(files, stash_constraint)

    for cube in cubes:
        print(cube.cell_methods[0].intervals[0])
        if cube.cell_methods[0].intervals[0] == '1 hour' or cube.cell_methods[0].intervals[0] == '6 hour':
            iris.save(cube, '/nesi/project/niwa00013/williamsjh/NZESM/brett-validation-metrics/'+suite+'-'+stash[i]+'-monthly.nc')

    del cubes, cube


