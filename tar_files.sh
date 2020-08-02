#!/bin/bash -l

#SBATCH --time=00-24:00:00 # days-hh:mm:ss
#SBATCH --ntasks 20
#SBATCH --partition nesi_prepost

startdir=$(pwd -P) && \
tarball="archive.tar" && \
cd /home/revelll/cylc-run/00004 && \
find . -type f -and -size -100M -print0 | xargs -0 -I {} tar --remove-files -rvf "${tarball}" {}
# Optionally, compress the archive
# (see below for notes on compression options)
bzip2 -9 "${tarball}"
# Return to where you started
cd "${startdir}"
