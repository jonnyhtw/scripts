n = 384
nxios = 32

f = open("distribute_xios_execs.txt", "w")

for j in range(8):

    f.write(str(40*j) + '-' + str(40*j+3) + " /opt/nesi/XC50_sles15_skl/XIOS/r2279-CrayIntel-23.02-19-NC4PAR-patched/bin/xios_server.exe\n")

    f.write(str(3+40*j+1)+'-'+str(3+40*j+36) + " /home/williamsjh/cylc-run/u-db797/run14/share/fcm_make_lfric/build/bin/lfric_atm configuration.nml\n")

f.write(str(8*40) + "-"+str(8*40 +  n-8*36-1) + " /home/williamsjh/cylc-run/u-db797/run14/share/fcm_make_lfric/build/bin/lfric_atm configuration.nml\n")


f.close()
