#!/bin/bash -l

# DIRECTIVES:
#SBATCH --time=24:00:00
#SBATCH --partition=nesi_prepost
#SBATCH --cpus-per-task=1
#SBATCH --account=niwa00013
#SBATCH --hint=nomultithread
#SBATCH --mem-per-cpu=50G
#SBATCH --nodes=1
#SBATCH --ntasks=1

cd /nesi/nobackup/niwa00013/williamsjh/nearline/niwa00013/williamsjh/cylc-run/u-bp908/share/data/History_Data
tar -xvf bp908a.2026.tar \*a.{p{c,8}\*.pp,pr\*}
