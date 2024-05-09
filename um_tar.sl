#!/bin/bash -l

# DIRECTIVES:
#SBATCH --time=24:00:00
#SBATCH --job-name=um_tar
#SBATCH --partition=nesi_prepost
#SBATCH --cpus-per-task=1
#SBATCH --account=niwa00013
#SBATCH --hint=nomultithread
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --array=1950-2014
#SBATCH --mem-per-cpu=20G

export suite=dc545

cd /home/williamsjh/cylc-run/u-${suite}/runN/share/data/History_Data/

find . -maxdepth 1 -iname "*a.p${stream}${SLURM_ARRAY_TASK_ID}*" -exec tar --remove-files -rvf ${suite}a.p${stream}${SLURM_ARRAY_TASK_ID}.tar {} \; 

