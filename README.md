# quickPyPlot
## Interface for quick plotting high-quality figures with Python.

#### A path to the executable might be added to the *~/.bashrc*:

*function quickPyPlot { python3.5 path/main.py $@;}*

#### The executable might be called from scripts when the scripts include functions from *~/.bashrc*:

*shopt -s expand_aliases*

*source ~/.bashrc*

### Available options can be seen with:

*quickPyPlot -h*

#### If only input data are provided the program generates a simple plot with default options: 

*quickPyPlot input/csd/aa/c\*/csd.res*

#### If *-s* option is set the program asks for options and generates the options file (for further usage, as below):

*quickPyPlot input/csd/aa/c\*/csd.res -s*

#### If the options file is provided (-o file) the program reads options from this file: 

*quickPyPlot -o option.opt input/csd/aa/c\*/csd.res* 

#### If *-f* option is set the program fits a function: 

*quickPyPlot input/rcf/rcf_?.res -f*

For the present the function is defined in *fit.py* module. The example shows fitting of a double exponential function to rotatinal autocorrelation data.

#### If *-m* option is set the program plots a color map: 

*quickPyPlot -m input/map/c\{8,16,32\}/contacts.res -s*

#### If the data file is provided (*-d file*) the program reads paths to the data from this file: 

*quickPyPlot -d plt.dat*

#### Required libraries

python 3.5

pip install numpy

pip install matplotlib

#### REMARKS

*sets* option indicates number [int] of functions per plot/subplot.

#### TO-DO-LIST

Block averaging and skipping.

Documentation with examples.

Column-style, steps-style plots. 

Tabels.

Plotting a function.

Labels.

Common titles for a set of plots.

Common color bar for a set of color maps.

Colormap.
