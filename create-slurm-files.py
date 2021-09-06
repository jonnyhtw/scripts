import os
import subprocess

time = '24:00:00'
job_name = 'nzesm-quick-access-data-creation'
partition = 'nesi_prepost'
cpus_per_task = '1'
account = 'niwa00013'
hint = 'nomultithread'
nodes = '1'
ntasks = '1'
stashmodel = 01
rawstashs=[34001,03206,30207, 
stashs = ['m01s34i001','m01s03i236']
suite = 'u-bn013'
years = range(2015,2100)
months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

for stash in stashs:

    for year in years:

        for month in months:

            with open('slurm.file.'+suite+'.'+str(stash)+'.'+str(year)+'.'+month+'.sl', 'w') as f:
                    f.write('#!/usr/bin/env bash')
                    f.write('\n')
                    f.write('\n')
                    f.write('# DIRECTIVES:\n')
                    f.write('#SBATCH --time='+time+'\n')
                    f.write('#SBATCH --job-name='+job_name+'\n')
                    f.write('#SBATCH --partition='+partition+'\n')
                    f.write('#SBATCH --cpus-per-task='+cpus_per_task+'\n')
                    f.write('#SBATCH --account='+account+'\n')
                    f.write('#SBATCH --hint='+hint+'\n')
                    f.write('#SBATCH --nodes='+nodes+'\n')
                    f.write('#SBATCH --ntasks='+ntasks+'\n')
                    f.write('\n')
                    f.write('module load Mule\n')
                    f.write('export outdir=/nesi/project/niwa00013/williamsjh/NZESM/quick-access-data/'+suite+'/\n')
                    f.write('rm $outdir/slurm-*.out\n')
                    f.write('mkdir -p $outdir\n')
                    f.write('export file='+suite[2:]+'a.pm'+str(year)+month+'.pp\n')
                    f.write('export stash='+str(stash)+'\n')
                    f.write('export lbuser4=34001\n')
                    f.write('mule-select /nesi/nobackup/niwa00013/williamsjh/nearline/niwa00013/williamsjh/cylc-run/'+suite+'/share/data/History_Data/$file $outdir/${stash}-$file --include lbuser4=${lbuser4}\n')
                    f.close()

#syscom = 'for file in *suite*.slsbatch *'+suite+'*.sl'
#print('now running...'+syscom)

#os.system(syscom)


subprocess.run('for file in *'+suite+'*.sl;  do sbatch $file; done', shell=True)







