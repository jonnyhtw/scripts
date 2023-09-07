#!/nesi/nobackup/niwa00013/williamsjh/miniconda3/envs/metpy/bin/python

import iris
import iris.coords
import os
import glob
from tqdm import tqdm

stash_constraint  =iris.AttributeConstraint(STASH='m01s03i236')
desired_cell_method = iris.coords.CellMethod(method='mean', coords='time', intervals='6 hour')
cell_method_constraint = iris.Constraint(cube_func=lambda cube: desired_cell_method in cube.cell_methods)

for file in tqdm(sorted(glob.glob('*.pp'))):
    print(file)
    iris.save(iris.load(file, stash_constraint & cell_method_constraint), file[:-3]+'.nc')

