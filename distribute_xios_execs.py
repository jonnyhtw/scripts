#!/usr/bin/env python3

n = 384
nxios = 32

f = open("distribute_xios_execs.txt", "w")

for i in range(nxios):  
    
    f.write(str(2 * i) + ' /home/williamsjh/cylc-run/u-db797/run14/share/fcm_make_lfric/build/bin/lfric_atm configuration.nml\n')
    f.write(str(2 * i + 1) + ' xios_server.exe\n')

for i in range(nxios * 2, n + nxios):

    f.write(str(i) + ' /home/williamsjh/cylc-run/u-db797/run14/share/fcm_make_lfric/build/bin/lfric_atm configuration.nml\n')

f.close()
