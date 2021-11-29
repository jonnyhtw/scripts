#adapted from https://pythonforundergradengineers.com/creating-taylor-series-functions-with-python.html

import math

def func_sinxoverx(x, n):
    sinxoverx_approx = 0
    for i in range(n):
        coef = (-1)**i
        num = x**(2*i+1)
        denom = math.factorial(2*i+1)*x
        sinxoverx_approx += ( coef ) * ( (num)/(denom) )
    
    return sinxoverx_approx

import math
import numpy as np
import matplotlib.pyplot as plt

angles = np.arange(-2*np.pi,2*np.pi,0.1)*2
p_sinxoverx = np.sin(angles)/angles

ax = plt.subplot(1,1,1)
ax.plot(angles,p_sinxoverx, label = 'sin(x)/x')

nterms = np.arange(2,7)*2

for i in nterms:
    t_sinxoverx = [func_sinxoverx(angle,i) for angle in angles]
    ax.plot(angles,t_sinxoverx,'-o',fillstyle = 'none',label = str(i), alpha = i/np.max(nterms))

plt.title('sin(x)/x and its taylor expansion to n terms')

plt.grid()

ax.set_ylim([-1,1])

plt.legend()

plt.show()
