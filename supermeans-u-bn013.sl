#!/bin/bash -l

# DIRECTIVES:
#SBATCH --time=24:00:00
#SBATCH --error=supermeans-u-bn013.err
#SBATCH --out=supermeans-u-bn013.out
#SBATCH --job-name=supermeans
#SBATCH --partition=nesi_prepost
#SBATCH --cpus-per-task=1
#SBATCH --account=niwa00013
#SBATCH --hint=nomultithread
#SBATCH --mem-per-cpu=200G
#SBATCH --nodes=1
#SBATCH --ntasks=1

export runid=bn013
export nyears=20
export firstyear=2081
export in_dir=/nesi/project/niwa00013/williamsjh/MASS/u-$runid/apm.pp
export in_dir=/home/williamsjh/cylc-run/u-$runid/share/data/History_Data
export in_dir=/nesi/nobackup/niwa00013/williamsjh/nearline/niwa00013/williamsjh/cylc-run/u-bn013/share/data/History_Data

echo $runid 'for ' $nyears ' years starting in' $firstyear '!'

export PATH=/nesi/nobackup/niwa00013/williamsjh/miniconda2/bin:$PATH

source activate python2-validation-note_env

/nesi/nobackup/niwa00013/williamsjh/miniconda2/envs/python2-validation-note_env/bin/python  -u ~/scripts/supermeans.py --nyears=$nyears --in_dir=$in_dir --runid=$runid --firstyear=$firstyear --prefix=$runid

source activate master

/nesi/nobackup/niwa00013/williamsjh/miniconda2/envs/master/bin/python  -u ~/scripts/supermeans-remove-1d-vars.py --nyears=$nyears --in_dir=$in_dir --runid=$runid --firstyear=$firstyear --prefix=$runid

source activate python2-validation-note_env

/nesi/nobackup/niwa00013/williamsjh/miniconda2/envs/python2-validation-note_env/bin/python  -u ~/scripts/supermeans-ann.py --nyears=$nyears --in_dir=$in_dir --runid=$runid --firstyear=$firstyear --prefix=$runid
