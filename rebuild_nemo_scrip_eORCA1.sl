#!/bin/bash
#SBATCH --job-name=rebuild_nemo
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --account=niwa00016
#SBATCH --partition=NeSI
#SBATCH --cpus-per-task=1
#SBATCH --output=out.%j.o
#SBATCH --error=error.%j.e
#SBATCH --mem=10000


ulimit
export OMP_NUM_THREADS=4
MPI_DSM_VERBOSE=1; export MPI_DSM_VERBOSE

export DATADIR=/nesi/nobackup/roachla/cylc-run/NCKLR03-clim-wfsd

export ID=NCKLR03-clim-wfsd

export NP=120


if [ -f ${ID}*T.nc ] 
then  
rm ${ID}*T.nc
fi

if [ -f ${ID}*U.nc ]
then
rm ${ID}*U.nc
fi

if [ -f ${ID}*V.nc ]
then
rm ${ID}*V.nc
fi


##
module load cray-netcdf
module load cray-hdf5
module load craype-broadwell 
echo "Modules loaded"

## base model monthly
export TFILE1m=`ls -1 ${ID}*1m*_T_0000.nc`
export UFILE1m=`ls -1 ${ID}*1m*_U_0000.nc`
export VFILE1m=`ls -1 ${ID}*1m*_V_0000.nc`



#combine T
/home/behrense/bin/rebuild_nemo_intel -t 4  `basename $TFILE1m _0000.nc` $NP

#combine U
/home/behrense/bin/rebuild_nemo_intel -t 4  `basename $UFILE1m _0000.nc` $NP

#combine V
/home/behrense/bin/rebuild_nemo_intel -t 4  `basename $VFILE1m _0000.nc` $NP

#combine W

#mv files to STOREAGE

mv ${ID}*T.nc $DATADIR
mv ${ID}*U.nc $DATADIR
mv ${ID}*V.nc $DATADIR


