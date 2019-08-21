#!/bin/bash -l

# DIRECTIVES:
#SBATCH --time=12:00:00
#SBATCH --partition=nesi_research
#SBATCH --cpus-per-task=40
#SBATCH --account=niwa00013
#SBATCH --hint=nomultithread
#SBATCH --nodes=1
#SBATCH --ntasks=1

export PATH=/nesi/nobackup/niwa00013/williamsjh/miniconda2/bin:$PATH
source activate master

python  ~/scripts/py-for-afterburner.dev.py --suite u-bb075 --year0 1950 --year 1961 --base /nesi/project/niwa00013/williamsjh/MASS/u-bb075/apm.pp/

