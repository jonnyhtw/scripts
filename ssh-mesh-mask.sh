#!/usr/bin/env bash

module load CDO
module load NCO

cdo sellevidx,1 -selvar,tmask ~/ocean_assess/mesh_mask_eORCA1.nc /nesi/project/niwa00013/williamsjh/NZESM/ssh-mask/mesh_mask_eORCA1-tmask-sellevidx1.nc

export runid=bl658

cd ~/cylc-run/u-${runid}/share/data/History_Data/NEMOhist/ocean_assess/

for file in *1y*grid*T*

do

    echo $file

    rsync -rvLP $file /nesi/project/niwa00013/williamsjh/NZESM/ssh-mask/

    cdo selvar,zos $file /nesi/project/niwa00013/williamsjh/NZESM/ssh-mask/zos.nc

    cdo mul /nesi/project/niwa00013/williamsjh/NZESM/ssh-mask/zos.nc /nesi/project/niwa00013/williamsjh/NZESM/ssh-mask/mesh_mask_eORCA1-tmask-sellevidx1.nc /nesi/project/niwa00013/williamsjh/NZESM/ssh-mask/zos-new.nc

    cdo setctomiss,0 /nesi/project/niwa00013/williamsjh/NZESM/ssh-mask/zos-new.nc /nesi/project/niwa00013/williamsjh/NZESM/ssh-mask/zos-new-miss.nc

    ncks -A -v zos /nesi/project/niwa00013/williamsjh/NZESM/ssh-mask/zos-new-miss.nc /nesi/project/niwa00013/williamsjh/NZESM/ssh-mask/$file

done

rm /nesi/project/niwa00013/williamsjh/NZESM/ssh-mask/zos*


