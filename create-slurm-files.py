import os
import numpy as np
import subprocess

stashmodel = '01'
rawstashs=np.array(['34001','03236','30207','30201','30202','00409','30204']) 
descriptions = np.array(['O3_MMR','Temperature_at_1.5m','Geopotential_height_on_P_levs','U_wind_on_P_levs','V_wind_on_P_levs','Surface_pressure','Temperature_on_P_levs'])
descriptions = np.array(['U_wind_on_P_levs','V_wind_on_P_levs'])
suite = 'u-bn013'
years = range(2015,2100)
months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

for k in range(len(years)):

    for j in range(len(rawstashs)):

        for i in range(len(months)):

            indir = '/nesi/nobackup/niwa00013/williamsjh/nearline/niwa00013/williamsjh/cylc-run/'+suite+'/share/data/History_Data/'

            outdir ='/nesi/project/niwa00013/williamsjh/NZESM/quick-access-data/u-bn013/' 

            mulecom = 'mule-select '+indir+suite[2:]+'a.pm'+str(years[k])+months[i]+'.pp'+outdir+' m'+stashmodel+'s'+rawstashs[j][0:2]+'i'+rawstashs[j][2:]+'-'+descriptions[j]+'-'+suite[2:]+'a.pm'+str(years[k])+months[i]+'.pp --include lbuser4='+rawstashs[j]

            os.system('module load Mule;'+  mulecom)

