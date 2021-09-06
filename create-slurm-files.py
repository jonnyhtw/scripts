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
descriptions = np.array(['O3-MMR','Temperature-at-1.5m','Geopotential-height-on-P-levs'])
suite = 'u-bn013'
years = range(2015,2016)
months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

os.system('rm ./*.{sl,out}')

for rawstash in rawstashs:

    for year in years:

        for month in months:

            with open('slurm.file.'+suite+'.'+str(rawstash)+'.'+str(year)+'.'+month+'.sl', 'w') as f:
                    f.write('#!/usr/bin/env bash')
                    f.write('\n')
                    f.write('\n')
                    f.write('# DIRECTIVES:\n')
                    f.write('#SBATCH --time='+time+'\n')
                    f.write('#SBATCH --job-name='+job_name+'\n')
                    f.write('#SBATCH --array='+str(firstyear)+'-'+str(lastyear)+'\n')
                    f.write('#SBATCH --partition='+partition+'\n')
                    f.write('#SBATCH --cpus-per-task='+cpus_per_task+'\n')
                    f.write('#SBATCH --account='+account+'\n')
                    f.write('#SBATCH --hint='+hint+'\n')
                    f.write('#SBATCH --nodes='+nodes+'\n')
                    f.write('#SBATCH --ntasks='+ntasks+'\n')
                    f.write('\n')
                    f.write('module load Mule\n')
                    f.write('export outdir=/nesi/project/niwa00013/williamsjh/NZESM/quick-access-data/'+suite+'/\n')
                    f.write('mkdir -p $outdir\n')
                    f.write('export file='+suite[2:]+'a.pm'+str(year)+month+'.pp\n')
                    f.write('export lbuser4='+str(rawstash).lstrip('0')+'\n')
                    f.write('mule-select /nesi/nobackup/niwa00013/williamsjh/nearline/niwa00013/williamsjh/cylc-run/'+suite+'/share/data/History_Data/$file ${outdir}/STASH-CODE-'+rawstash+'_'+descriptions[np.where(rawstash == rawstashs)][0]+'_$file --include lbuser4=${lbuser4}\n')
                    f.close()

subproc ='for file in *'+suite+'*.sl;  do sbatch $file; done' 

subprocess.run(subproc, shell=True)







