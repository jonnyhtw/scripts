#!/bin/bash -l

# DIRECTIVES:
#SBATCH --time=12:00:00
#SBATCH --error=py-for-afterburner.err
#SBATCH --out=py-for-afterburner.out
#SBATCH --partition=nesi_prepost
#SBATCH --cpus-per-task=1
#SBATCH --account=niwa00013
#SBATCH --hint=nomultithread
#SBATCH --nodes=1
#SBATCH --ntasks=1

export PATH=/nesi/nobackup/niwa00013/williamsjh/miniconda2/bin:$PATH
source activate master

/nesi/nobackup/niwa00013/williamsjh/miniconda2/envs/master/bin/python  ~/scripts/py-for-afterburner.py --suite u-bl274 --year0 1950 --year $myyear --base /nesi/nobackup/niwa00013/williamsjh/cylc-run/u-bl274/share/data/History_Data/

