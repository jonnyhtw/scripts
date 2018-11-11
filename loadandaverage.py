# series of commands to read in files and perform a time mean on them (e.g.
# creating seasonal means or supermeans).

import iris, copy
from braceexpand import braceexpand

files=list(braceexpand('./ba369a.ps18{5[1-9],60}djf.pp'))

vars=iris.load(files)

foo=copy.copy(vars)

for i in range(len(vars)):
    foo[i] = vars[i].collapsed('time',iris.analysis.MEAN)


iris.save(foo,'myfile.pp')
