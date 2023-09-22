#!/bin/bash -l

# DIRECTIVES:
#SBATCH --time=00:30:00
#SBATCH --partition=nesi_prepost
#SBATCH --cpus-per-task=1
#SBATCH --account=niwa00013
#SBATCH --hint=nomultithread
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --array=2015-2100

cd /nesi/nobackup/niwa00013/williamsjh/nearline/niwa00013/williamsjh/cylc-run/u-bp908/share/data/History_Data

peter.py --year $SLURM_ARRAY_TASK_ID


