import sys

n = 384
ppn = 40
nxios = 32
nxios_on_each_node = 4

if nxios > n:

    print('nxios must be less than n, mpmd file not produced!')

    sys.exit()

else:

    pass

f = open("distribute_xios_execs.txt", "w")

for i in range(int(nxios/nxios_on_each_node)):

    f.write(str(ppn*i) + '-' + str(ppn*i+(nxios_on_each_node-1)) + " /opt/nesi/XC50_sles15_skl/XIOS/r2279-CrayIntel-23.02-19-NC4PAR-patched/bin/xios_server.exe\n")

    f.write(str((nxios_on_each_node -1 )+ppn*i+1)+'-'+str((nxios_on_each_node-1)+ppn*i+(ppn - nxios_on_each_node)) + " /home/williamsjh/cylc-run/u-db797/run16/share/fcm_make_lfric/build/bin/lfric_atm configuration.nml\n")

f.write(str((nxios/nxios_on_each_node)*ppn) + "-"+str((nxios/nxios_on_each_node)*ppn +  n-(nxios/nxios_on_each_node)*(ppn - nxios_on_each_node)-1) + " /home/williamsjh/cylc-run/u-db797/run16/share/fcm_make_lfric/build/bin/lfric_atm configuration.nml\n")


f.close()
