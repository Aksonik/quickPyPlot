#!/bin/bash

shopt -s expand_aliases
source ~/.bashrc

### ~/.bashrc
### function quickPyPlot { python3.5 path/main.py $@;}



### generates a simple plot:
#quickPyPlot input/csd/*/c*/csd.res

### asks for options:
#quickPyPlot -s input/csd/*/c*/csd.res

### read options:
#quickPyPlot -o plt.opt input/csd/*/c*/csd.res

### fit a function
quickPyPlot -f input/rcf/rcf_?.res
