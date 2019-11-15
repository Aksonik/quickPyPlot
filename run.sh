#!/bin/bash

shopt -s expand_aliases
source ~/.bashrc

### ~/.bashrc
### function quickPyPlot { python3.5 path/main.py $@;}



### guess options (options file is not provided):
#quickPyPlot input/csd/aa/c*/csd.res

### set options (option file is not provided):
quickPyPlot -s input/csd/*/c*/csd.res



### read options (option file is provided):"
#python main.py -o plt.opt input/csd/*/c*/csd.res








#python3.5 main.py input/csd/aa/c5/csd.res


#echo "set options (option file is not provided):"
#python main.py -s input/csd/aa/c{5,10,30}/csd.res

#echo "error (no data provided):"
#python main.py 
