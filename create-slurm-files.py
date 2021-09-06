import os
import numpy as np
import subprocess

time = '24:00:00'
job_name = 'nzesm-quick-access-data-creation'
partition = 'nesi_prepost'
cpus_per_task = '1'
account = 'niwa00013'
hint = 'nomultithread'
nodes = '1'
ntasks = '1'
stashmodel = '01'
rawstashs=np.array(['34001','03236','30207',]) 
descriptions = np.array(['O3_MMR','Temperature_at_1.5m','Geopotential_height_on_P_levs'])
suite = 'u-bn013'
years = range(2015,2016)
months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

for j in range(len(rawstashs)):

    for i in range(len(months)):

        mulecom = ' mule-select /nesi/nobackup/niwa00013/williamsjh/nearline/niwa00013/williamsjh/cylc-run/'+suite+'/share/data/History_Data/'+suite[2:]+'a.pm2015'+months[i]+'.pp /nesi/project/niwa00013/williamsjh/NZESM/quick-access-data/u-bn013/m'+stashmodel+'s'+rawstashs[j][0:2]+'i'+rawstashs[j][2:]+'-'+descriptions[j]+'-'+suite[2:]+'a.pm2015'+months[i]+'.pp --include lbuser4='+rawstashs[j]

        os.system('module load Mule;'+  mulecom)








