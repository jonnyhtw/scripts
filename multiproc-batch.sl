#!/bin/bash -l

# DIRECTIVES:
#SBATCH --time=0:10:00
#SBATCH --partition=nesi_research
#SBATCH --cpus-per-task=40
#SBATCH --account=niwa00013
#SBATCH --hint=nomultithread
#SBATCH --nodes=1
#SBATCH --ntasks=1

export NPROC=$SLURM_CPUS_PER_TASK

python ./multiproc2.py
