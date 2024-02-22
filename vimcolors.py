#!/usr/bin/env python3

import random
import os

os.chdir(os.path.expanduser('~/.vim/colors'))

colours = [ colour[0:-4] for colour in os.listdir('.') ]

with open(os.path.expanduser('~/scripts/randomvimcolorscheme.txt'),'w') as output:
    output.write(random.choice(colours))
