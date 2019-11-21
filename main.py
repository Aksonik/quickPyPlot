import argparse
import sys

import plot	# module

parser=argparse.ArgumentParser(description="All arguments that are unknown are assumed\
 to be paths to input data files.")
parser.add_argument("-o",type=str,help="options file")
parser.add_argument("-d",type=str,help="data file")
parser.add_argument("-s","--foo",action="store_true",help="set options interactively")
args,data=parser.parse_known_args()

plotObj=plot.plotClass()

if((args.o==None)&(args.foo==False)):
 plotObj.simplePlot(data)

if(args.foo==True):
 optMode="setOpt"
 plotObj.optionsPlot(data,optMode)

if(args.o!=None):
 plotObj.optFile=args.o

 optMode="readOpt"
 plotObj.optionsPlot(data,optMode)








if(args.d!=None):
 print("Read from a data file:",args.d)
 print("Data:",data)
