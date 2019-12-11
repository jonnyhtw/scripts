#!/usr/bin/env bash

cd /nesi/nobackup/niwa00013/williamsjh/cylc-run/u-bl274/share/data/History_Data

for year in {1962..1963} ; do echo $year ; tar -cvzf bl274a.${year}.tar.gz --remove-files *${year}* ; done

