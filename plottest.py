"""
Noddy code for testing various combinations of matplotlib marker size, marker colour,
and transparency settings.
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

print("mpl version:", mpl.__version__)

#from matplotlib.colors import is_color_like
#for col in ['red', 'fred', '#abc',  '#a1b2c3', '0.5', '123', '#456']:
#    print("Colour {} is {}".format(col, is_color_like(col)))

x = np.arange(10)
y1 = 2*x + 1
y2 = 3*x - 5
y3 = -2*x + 10
y4 = -4*x + 20

default_ms = mpl.rcParams['lines.markersize']
print("default markersize:", default_ms)

plt.plot(x, y1, 'o', lw=default_ms, ms=default_ms)
plt.plot(x, y1, '-', lw=default_ms, color='b', alpha=0.5, marker=None)

plt.plot(x, y2, '-o', lw=2, color='r', ms=10, markeredgecolor='r', markerfacecolor='none')

plt.plot(x, y3, '-o', lw=2, color='g', ms=10, markeredgecolor='g', markerfacecolor='none',
    alpha=0.5)

plt.plot(x, y4, 'd', ms=10, markeredgecolor='purple', markerfacecolor='none',
    alpha=0.5)

plt.show()
