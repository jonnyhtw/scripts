#!/bin/bash -l

# DIRECTIVES:
#SBATCH --time=24:00:00
#SBATCH --job-name=rebuild_nemo_batch
#SBATCH --partition=nesi_prepost
#SBATCH --cpus-per-task=1
#SBATCH --account=niwa00013
#SBATCH --hint=nomultithread
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --array=1951-2015

module unload netCDF/4.6.1-GCC-7.1.0
module unload HDF5/1.10.1-GCC-7.1.0
module unload Szip
module load netCDF-Fortran/4.4.4-iccifort-2018.1.163-GCC-7.1.0

export suite=cy574
export nprocs_nemo=240
export nprocs=40

cd /home/williamsjh/cylc-run/u-${suite}/runN/share/data/History_Data/NEMOhist/

#physics
rebuild_nemo -t $nprocs ${suite}o_${SLURM_ARRAY_TASK_ID}0101_restart $nprocs_nemo 
#tracers
rebuild_nemo -t $nprocs ${suite}o_${SLURM_ARRAY_TASK_ID}0101_restart_trc $nprocs_nemo 

#cd /home/williamsjh/cylc-run/u-${suite}/runN/share/data/History_Data/1_NEMO/
#agrif physics
#rebuild_nemo -t $nprocs 1_${suite}o_${SLURM_ARRAY_TASK_ID}0101_restart $nprocs_nemo 
