import argparse
import sys

import plot	# module

parser=argparse.ArgumentParser(description="All arguments that are unknown are assumed\
 to be paths to input data files.")
parser.add_argument("-o",type=str,help="options file")
parser.add_argument("-d",type=str,help="data file")
parser.add_argument("-s","--ask",action="store_true",help="set options interactively")
parser.add_argument("-f","--fit",action="store_true",help="fit a function")
args,data=parser.parse_known_args()

plotObj=plot.plotClass()

if((args.o==None)&(args.ask==False)):	# default options [none]
 optMode="defOpt"
 plotObj.optionsPlot(data,optMode,args.fit)

if(args.ask==True):		# ask for options [-s] (generates an options file)
 optMode="setOpt"
 plotObj.optionsPlot(data,optMode,args.fit)

if(args.o!=None):		# read options from a file [-o file]
 plotObj.optFile=args.o

 optMode="readOpt"
 plotObj.optionsPlot(data,optMode,args.fit)








if(args.d!=None):
 print("Read from a data file:",args.d)
 print("Data:",data)
