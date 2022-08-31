import matplotlib.pyplot as plt
import iris
import numpy as np

all_data = iris.load('/scale_wlg_nobackup/filesets/nobackup/niwa00013/williamsjh/nearline/niwa00013/williamsjh/cylc-run/u-bl658/share/data/History_Data/nzwam/temp*197101*.pp')

all_data = []

for i in range(len(cubes)):
        samples = [('latitude',-40),('longitude',165)]
        all_data.append(cubes[i].interpolate(samples, iris.analysis.Nearest()).data)

foo = np.concatenate(all_data)

plt.plot(foo,'-o')
