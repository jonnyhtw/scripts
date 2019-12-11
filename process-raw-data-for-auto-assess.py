'''

This is a script to generate data for input to auto assess from raw UM model output

This command gives the following output:

    command = fcm cat https://code.metoffice.gov.uk/svn/cma/autoassess/branches/dev/paulearnshaw/2017.12.02_rm_create_valnote/autoassess/moose_queries/stratosphere.monthly.g.txt@760

    output  =

        begin
            stash = (30201, 30204, 30205)
            lbproc = 192
        end
        begin
            stash = 34150
            lbproc = 128
        end

Information on lbproc can be found here https://code.metoffice.gov.uk/doc/um/latest/papers/umdp_F03.pdf

In this example lbproc = 192 = 64 + 128 which indicates a time mean (128) zonal mean (64) field and lbproc = 128 indicates a time mean field.
        
'''

with open('./stratosphere.monthly.g.txt') as f:
    lines = f.readlines()

for i in range(0,len(lines)):
    lines[i] = lines[i].replace(" ","")
    print lines[i]





#Import some modules

import iris
import iris.analysis

#Let's read in some raw model data...

stashcode=['m01s30i201','m01s30i204','m01s30i205','m01s34i150']

stash = iris.AttributeConstraint(STASH=str(iris.fileformats.pp.STASH(01, 30, 201)))

var30201 = iris.load('/home/williamsjh/cylc-run/u-ai955/share/data/History_Data/*pg*',stash)

stash = iris.AttributeConstraint(STASH=stashcode[1])

var30204 = iris.load('/home/williamsjh/cylc-run/u-ai955/share/data/History_Data/*pg*',stash)

stash = iris.AttributeConstraint(STASH=stashcode[2])

var30205 = iris.load('/home/williamsjh/cylc-run/u-ai955/share/data/History_Data/*pg*',stash)

stash = iris.AttributeConstraint(STASH=stashcode[3])

var34150 = iris.load('/home/williamsjh/cylc-run/u-ai955/share/data/History_Data/*pg*',stash)

#Concatenate the variables

cat = iris.cube.CubeList([var30201[0],var30204[0],var30205[0],var34150[0]])

#Save to an output file

#iris.save(cat,'apg.nc')


import iris.fileformats.pp as pp

with open('apg.pp', 'wb') as fh:
    i = 0
    for cube in cat:
        #  print i
        for sub_cube, field in pp.save_pairs_from_cube(cube):
            if field.lbnpt == 0:
                field.bdx = 1
                field.bzx = sub_cube.coord('longitude').points[0] - field.bdx
                field.lbnpt = 1
            else:
                pass
            field.save(fh)
        i=i+1
