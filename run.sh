#!/bin/bash

shopt -s expand_aliases
source ~/.bashrc

### ~/.bashrc
### function quickPyPlot { python3.5 path/main.py $@;}



### guess options (options file is not provided):
#quickPyPlot input/csd/aa/c*/csd.res

### set options (option file is not provided):
#quickPyPlot -s input/csd/*/c*/csd.res

### read options (option file is provided):"
quickPyPlot -o plt.opt input/csd/*/c*/csd.res
