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
#quickPyPlot -f input/rcf/rcf_?.res

### plot a color map
#quickPyPlot -m input/map/c32/contacts.res
#quickPyPlot -m input/map/c16/contacts.res
#quickPyPlot -m input/map/c8/contacts.res
#quickPyPlot -m input/map/c32/contacts_36x30.res
#quickPyPlot -m input/map/c32/contacts_20x36.res

#quickPyPlot -m input/map/c{8,16,32}/contacts.res -s
#quickPyPlot -m input/map/c{8,16,32}/contacts.res

quickPyPlot -m -d plt.dat
