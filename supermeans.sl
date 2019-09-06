#!/bin/bash -l

# DIRECTIVES:
#SBATCH --time=12:00:00
##SBATCH --error=supermeans.err
##SBATCH --out=supermeans.out
#SBATCH --job-name=supermeans
#SBATCH --partition=nesi_prepost
#SBATCH --cpus-per-task=1
#SBATCH --account=niwa00013
#SBATCH --hint=nomultithread
#SBATCH --mem-per-cpu=2G
#SBATCH --nodes=1
#SBATCH --ntasks=1

export PATH=/nesi/nobackup/niwa00013/williamsjh/miniconda2/bin:$PATH
source activate foo

/nesi/nobackup/niwa00013/williamsjh/miniconda2/envs/master/bin/python  ~/scripts/supermeans.py

