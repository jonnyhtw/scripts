#!/bin/bash -l

# DIRECTIVES:
#SBATCH --time=24:00:00
#SBATCH --job-name=compress_for_nearline
#SBATCH --partition=nesi_prepost
#SBATCH --cpus-per-task=1
#SBATCH --account=niwa00013
#SBATCH --hint=nomultithread
#SBATCH --mem-per-cpu=50G
#SBATCH --array=1981-2014
#SBATCH --nodes=1
#SBATCH --ntasks=1

cd /nesi/nobackup/niwa00013/williamsjh/cylc-run/u-bl274/share/data/History_Data

export FILE=bl274a.${SLURM_ARRAY_TASK_ID}.tar.gz

if [ ! -f "$FILE" ]; then
    echo "$FILE does not exist"
    tar -cvzf $FILE --remove-files *a.p*${SLURM_ARRAY_TASK_ID}* 
fi

if [ -f "$FILE" ]; then
    echo "$FILE exists"
    tar -cvzfr $FILE --remove-files *a.p*${SLURM_ARRAY_TASK_ID}* 
fi
