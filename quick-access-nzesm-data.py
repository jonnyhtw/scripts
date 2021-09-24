import os
import iris
import glob
import numpy as np
import subprocess
import argparse

stashmodel = '01'
rawstashs=np.array(['34001','03236','30207','30201','30202','00409','30204','00024','03234','01208','02205','34049','34992','34010','34081','00010','00408','50219','50245','00002','00003','50228','50229','51001']) 

descriptions = np.array(['O3_MMR','Temperature_at_1.5m','Geopotential_height_on_P_levs','U_wind_on_P_levs','V_wind_on_P_levs','Surface_pressure','Temperature_on_P_levs','Surface_temperature','Surface_latent_heat_flux','TOA_outgoing_SW','TOA_outgoing_LW','N2O_MMR','HCl_MMR','CO_MMR','OH_MMR','Specific_humidity','Pressure_on_theta_levs','Ozone_column_in_DU','Photolysis_rate_JO2','U_wind_on_model_levels','V_wind_on_model_levels','Photolysis_rate_JO1D','Photolysis_rate_JNO2','O3_MMR_on_P_levs'])




streams = np.array(['m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','4','4','4','4','m'])



print(len(rawstashs))
print(len(descriptions))
print(len(streams))

if ( len(rawstashs) == len(descriptions) != len(streams) ):
    print('rawstashs descriptions and streams must be the same length')
    exit()
    

months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

#####################################################
#parse some args
parser = argparse.ArgumentParser()
parser.add_argument('--year', required=True, type=int)
parser.add_argument('--suite', required=True, type=str)
args = parser.parse_args()
year = args.year
suite = args.suite
#####################################################

for j in range(len(rawstashs)):

    for i in range(len(months)):

        indir = '/nesi/nobackup/niwa00013/williamsjh/nearline/niwa00013/williamsjh/cylc-run/'+suite+'/share/data/History_Data/'

        infile = suite[2:]+'a.p'+streams[j]+str(year)+months[i]+'.pp'

        outdir ='/nesi/project/niwa00013/williamsjh/NZESM/quick-access-nzesm-data/'+suite+'/' 

        outfile = 'm'+stashmodel+'s'+rawstashs[j][0:2]+'i'+rawstashs[j][2:]+'-'+descriptions[j]+'-'+suite[2:]+'a.p'+streams[j]+str(year)+months[i]+'.pp'

        #create outdir if it's not there
        os.system('mkdir -p '+outdir)

        #define mule command
        mulecom = 'mule-select '+\
                  indir+\
                  infile+\
                  ' '+\
                  outdir+\
                  outfile+\
                  ' '+\
                  '--include lbuser4='+rawstashs[j]

        #run mule command
        os.system('module load Mule;'+  mulecom)

        #convert to netcdf
        iris.save(iris.load(outdir+outfile), outdir+outfile[:-3]+'.nc')
       
        #remove pp files
        os.system('rm '+outdir+outfile)

