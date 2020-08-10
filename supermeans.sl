#!/bin/bash -l

# DIRECTIVES:
#SBATCH --time=12:00:00
##SBATCH --error=supermeans.err
##SBATCH --out=supermeans.out
#SBATCH --job-name=supermeans
#SBATCH --partition=nesi_research
#SBATCH --cpus-per-task=1
#SBATCH --account=niwa00013
#SBATCH --hint=nomultithread
#SBATCH --mem-per-cpu=2G
#SBATCH --nodes=1
#SBATCH --hint=nomultithread
#SBATCH --ntasks=40

export PATH=/nesi/nobackup/niwa00013/williamsjh/miniconda2/bin:$PATH
source activate foo

/nesi/nobackup/niwa00013/williamsjh/miniconda2/envs/foo/bin/python  -u ~/scripts/supermeans.py --nyears=20 --in_dir=/nesi/project/niwa00013/williamsjh/MASS/u-bb075/apm.pp/ --runid=bb075 --firstyear=1989 --prefix=bb075
#/nesi/nobackup/niwa00013/williamsjh/miniconda2/envs/foo/bin/python  -u ~/scripts/supermeans.py --nyears=20 --in_dir=/nesi/project/niwa00013/williamsjh/MASS/u-bb075/apm.pp/ --runid=bb075 --firstyear=1989

