# Script to plot UM run speeds as a function of processors decomposition
# and complexity.

import matplotlib.pyplot as plt
import numpy as np

processor_decomposition=[16*8,16*16,32*16,32*32]

n96=np.array([(36.*60.+59.)-(29.*60.+43.),(21.*60.+24.)-(17.*60.+1.),(28.*60.+37.)-(25.*60.+20.),float('nan')])

n96_ompthr2=np.array([(43.*60.+32.)-(35.*60.+.53),(31.*60.+21.)-(26.*60.+46.),(13.*60.+31.)-(9.*60.+29.),float('nan')])


n96_chem=np.array([(63.*60.+17.)-(46.*60.+.17),(18.*60.+11.)-(9.*60.+2.),(29.*60.+19.)-(22.*60.+53.),float('nan')])

n216=np.array([(0.*60.+0.)-(0.*60.+0.),(0.*60.+0.)-(0.*60.+0.),(48.*60.+59.)-(36.*60.+18.),(36.*60.+30.)-(26.*60.+22.)])

#'n96' is the number of seconds taken to run one day of simulation. We need to convert this to years of simulation per wallclock day.

ypd_n96=1./n96/360.*(24.*60.*60.)
ypd_n96_ompthr2=1./n96_ompthr2/360.*(24.*60.*60.)
ypd_n96_chem=1./n96_chem/360.*(24.*60.*60.)
ypd_n216=1./n216/360.*(24.*60.*60.)

plt.plot(processor_decomposition,ypd_n96,'-ok',ms=10)
plt.plot(processor_decomposition,ypd_n96_ompthr2,'-ok',ms=10,mfc='w')
plt.plot(processor_decomposition,ypd_n96_chem,'-sk',ms=10)
plt.plot(processor_decomposition,ypd_n216,'-^k',ms=10)
plt.xlabel('number of processors')
plt.ylabel('years $\cdot$ day $^{-1}$')
plt.grid(True)
plt.axis([0,1100,0,1.4])
plt.legend(['n96','n96_ompthr2','n96_chem','n216'])
plt.show()
