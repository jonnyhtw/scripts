import iris

def area_avg_cube(cube, guess_bounds=False, missing_data_value=None, stdev=False):
    if guess_bounds:
        cube_coord_guess_bounds(cube)

    if missing_data_value is not None: 
        my_masked_array = np.ma.masked_values(cube.data, missing_data_value, copy=False)
        cube.data = my_masked_array

    grid_areas = iris.analysis.cartography.area_weights(cube)
    
    if stdev:
        collapsed_cube = cube.collapsed(['longitude', 'latitude'], iris.analysis.STD_DEV, weights=grid_areas)
        return collapsed_cube.data
    else:
        collapsed_cube = cube.collapsed(['longitude', 'latitude'], iris.analysis.MEAN, weights=grid_areas)
        return collapsed_cube.data
