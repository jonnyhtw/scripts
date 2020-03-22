import iris
import glob
import matplotlib as plt
import numpy.ma as ma

stash_constraint = iris.AttributeConstraint(STASH='m01s00i507')
desired_cell_method = iris.coords.CellMethod(method='mean', coords='time', intervals='1 hour')
cell_method_constraint = iris.Constraint(cube_func=lambda cube: desired_cell_method in cube.cell_methods)

files = glob.glob('/nesi/nobackup/niwa00013/williamsjh/cylc-run/u-bl658/share/data/History_Data/*a.pm*.pp')

for file in files:
    print('now doing... ',file)
    cubes = iris.load(file, stash_constraint & cell_method_constraint)
    cubes[0].data = ma.array(cubes[0].data, mask=mask[0].data)
    iris.save(cubes,'./'+os.path.basename(file)[:-3]+'-masked-monthly-sst.nc')

