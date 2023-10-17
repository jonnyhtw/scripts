#!/bin/bash -l

# DIRECTIVES:
#SBATCH --time=00:01:00
#SBATCH --partition=nesi_prepost
#SBATCH --cpus-per-task=1
#SBATCH --account=niwa00013
#SBATCH --hint=nomultithread
#SBATCH --nodes=1
#SBATCH --ntasks=1

echo 'cheese'
