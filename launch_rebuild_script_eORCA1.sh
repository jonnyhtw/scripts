#!/bin/bash

module load slurm

export suite=u-bb016

echo "$SUITE"

for dir in /home/$USER/cylc-run/$SUITE/work/*/nemo_cice*/

    do

    echo "$dir"

    cd "$dir"

    echo 'rebuilding files in...'
    echo "$dir"


    echo sbatch rebuild_nemo_scrip_eORCA1.sl

    sbatch rebuild_nemo_scrip_eORCA1.sl

done



