#!/usr/bin/env python3

import random
import os

os.chdir(os.path.expanduser('~/.vim/colors'))

colors = [ color[0:-4] for color in os.listdir('.') ]

with open(os.path.expanduser('~/scripts/randomvimcolorscheme.txt'),'w') as output:
    output.write(random.choice(colors))
