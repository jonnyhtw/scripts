import iris, glob

suite = 'u-bl658'

stash = ['m01s16i222','m01s05i216','m01s00i024']

for year in range(1950,2015):

    print(year)

    for i in range(len(stash)):

        stash_constraint = iris.AttributeConstraint(STASH=stash[i])

        files = sorted(glob.glob('/home/williamsjh/cylc-run/'+suite+'/share/data/History_Data/*a.pm*'+str(year)+'*.pp'))
        print(files)

        cubes = iris.load(files, stash_constraint)

        for cube in cubes:
            print(cube.cell_methods[0].intervals[0])
            if cube.cell_methods[0].intervals[0] == '1 hour' or cube.cell_methods[0].intervals[0] == '6 hour':
                iris.save(cube, '/nesi/project/niwa00013/williamsjh/NZESM/brett-validation-metrics/'+suite+'-'+stash[i]+'-'+str(year)+'-monthly.nc')

        del cubes, cube

