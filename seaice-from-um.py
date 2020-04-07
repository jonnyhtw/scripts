import iris
import glob
import numpy as np
import matplotlib as plt
import os
import numpy.ma as ma

stash_constraint = iris.AttributeConstraint(STASH='m01s00i031')
mask_constraint = iris.AttributeConstraint(STASH='m01s00i030')
desired_cell_method = iris.coords.CellMethod(method='mean', coords='time', intervals='1 hour')
cell_method_constraint = iris.Constraint(cube_func=lambda cube: desired_cell_method in cube.cell_methods)

mask = iris.load_cube('/nesi/nobackup/niwa00013/williamsjh/cylc-run/u-bl658/share/data/History_Data/bl658a.pm1950jan.pp',mask_constraint)

for year in range(1950, 2015):

    files = np.sort(glob.glob('/nesi/nobackup/niwa00013/williamsjh/cylc-run/u-bl658/share/data/History_Data/*a.pm'+str(year)+'*.pp'))

    cubes = iris.load_cube(files, stash_constraint & cell_method_constraint)

    for i in range(0,cubes.data.shape[0]):
        cubes.data[i,:,:][mask.data == 1] = np.nan

    iris.save(cubes,'bl658-'+str(year)+'-masked-sea-ice.nc')
