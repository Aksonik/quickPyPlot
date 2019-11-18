# quickPyPlot
## An interface for quick plotting high quality figures with Python.

#### A path to the executable might be added to the *~/.bashrc*:

*function quickPyPlot { python3.5 path/main.py $@;}*

#### The executable might be called from scripts when the scripts include functions from *~/.bashrc*:

*shopt -s expand_aliases*

*source ~/.bashrc*

#### If only input data is provided the program generates a simple plot: 

*python main.py input/csd/aa/c*/csd.res*

#### If *-s* option is set the program asks for options and generates the options file (for further usage):

*python main.py -s input/csd/aa/c*/csd.res*

#### If the options file is provided the program reads options from this file: 

*python main.py -o option.opt input/csd/aa/c*/csd.res* 



#### Required libraries

python 3.5

pip install numpy
pip install matplotlib
