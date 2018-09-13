#!/bin/csh

module load slurm

set DIR=/nesi/nobackup/roachla/cylc-run/NCKLR03-clim-wfsd/work


foreach file (`ls -d /nesi/nobackup/roachla/cylc-run/NCKLR03-clim-wfsd/work/*/nemo_cice/`)

cd $file

cp /nesi/nobackup/roachla/cylc-run/NCKLR03-clim-wfsd/rebuild_nemo_scrip_eORCA1.sl .

echo $file

echo sbatch rebuild_nemo_scrip_eORCA1.sl

sbatch rebuild_nemo_scrip_eORCA1.sl

end

