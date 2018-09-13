#!/bin/bash

export SUITE=u-bb016
echo $SUITE

for dir in /home/$USER/cylc-run/$SUITE/work/*/nemo_cice*/

    do
 
    echo $dir
  
    ulimit
    export OMP_NUM_THREADS=4
    MPI_DSM_VERBOSE=1; export MPI_DSM_VERBOSE


    cd $dir

    export DATADIR=$dir
    echo $dir


    export NP=72


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
    export TFILE5d=`ls -1 ${ID}*5d*_T_0000.nc`
    export UFILE5d=`ls -1 ${ID}*5d*_U_0000.nc`
    export VFILE5d=`ls -1 ${ID}*5d*_V_0000.nc`



    #combine T
    /home/behrense/bin/rebuild_nemo_intel -t 4  `basename $TFILE5d _0000.nc` $NP

    #combine U
    /home/behrense/bin/rebuild_nemo_intel -t 4  `basename $UFILE5d _0000.nc` $NP

    #combine V
    /home/behrense/bin/rebuild_nemo_intel -t 4  `basename $VFILE5d _0000.nc` $NP

    #combine W
    #foo


    done

cd ~/scripts/
