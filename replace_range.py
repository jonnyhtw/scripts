#!/usr/bin/env python2

#https://unix.stackexchange.com/questions/409167/replace-range-of-lines-with-range-of-lines-sed-or-others

#example usage (jw)
###
for file in *.nc; do  echo $file ; ncdump  $file  >   header/$file.cdl ; python ~/scripts/replace_range.py header/$file.cdl 22,1326 header/aw310/cice_aw310i_1m_19600101-19600201.cdl 22,1326 > header/$file.new.cdl; ncgen -o header/$file.nc header/$file.new.cdl ; rm header/*.cdl ; done
###

# -*- coding: ascii  -*-
"""replace_range.py"""

import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "matchfile",
    help="File in which to replace lines",
)
parser.add_argument(
    "matchrange",
    help="Comma-separated range of Lines to match and replace",
)
parser.add_argument(
    "replacementfile",
    help="File from which to get replacement lines"
)
parser.add_argument(
    "replacementrange",
    help="Comma-separated range of lines from which to get replacement"
)

if __name__=="__main__":

    # Parse the command-line arguments
    args = parser.parse_args()

    # Open the files
    with \
    open(args.matchfile, 'r') as matchfile, \
    open(args.replacementfile, 'r') as replacementfile:

        # Get the input from the match file as a list of strings 
        matchlines = matchfile.readlines()

        # Get the match range (NOTE: shitf by -1 to convert to zero-indexed list)
        mstart = int(args.matchrange.strip().split(',')[0]) - 1
        mend = int(args.matchrange.strip().split(',')[1]) - 1

        # Get the input from the replacement file as a list of strings 
        replacementlines = replacementfile.readlines()

        # Get the replacement range (NOTE: shitf by -1 to convert to zero-indexed list)
        rstart = int(args.replacementrange.strip().split(',')[0]) -1
        rend = int(args.replacementrange.strip().split(',')[1]) - 1

        # Replace the match text with the replacement text
        outputlines = matchlines[0:mstart] + replacementlines[rstart:rend+1] + matchlines[mend+1:]

        # Output the result
        sys.stdout.write(''.join(outputlines))
