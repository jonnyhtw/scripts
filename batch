#!/bin/bash -l

# DIRECTIVES:
#SBATCH --time=24:00:00
#SBATCH --partition=nesi_prepost
#SBATCH --cpus-per-task=1
#SBATCH --account=niwa00013
#SBATCH --hint=nomultithread
#SBATCH --mem-per-cpu=200G
#SBATCH --nodes=1
#SBATCH --ntasks=1


module load Mule

/opt/nesi/CS500_centos7_skl/Anaconda2/2019.10-GCC-7.1.0/bin/python batch-u-be509.py
