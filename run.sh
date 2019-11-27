#!/bin/bash

shopt -s expand_aliases
source ~/.bashrc

### ~/.bashrc
### function quickPyPlot { python3.5 path/main.py $@;}

### regular plot

#quickPyPlot input/csd/*/c*/csd.res
#quickPyPlot -s input/csd/*/c*/csd.res
#quickPyPlot -o plt.opt input/csd/*/c*/csd.res
#quickPyPlot -f input/rcf/rcf_?.res			# fit a function

### color map

#quickPyPlot -m input/map/c{8,16,32}/contacts.res
#quickPyPlot -m input/map/c32/contacts_20x36.res	# other shape of data
#quickPyPlot -m -s input/map/c{8,16,32}/contacts.res
#quickPyPlot -m -s -d plt.dat
#quickPyPlot -m -o plt_map.opt -d plt.dat
