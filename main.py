import argparse
import sys

import plot	# module
import writeData
import readData

parser=argparse.ArgumentParser(description="All arguments that are unknown are assumed\
 to be paths to input data files.")
parser.add_argument("-o",type=str,help="options file")
parser.add_argument("-d",type=str,help="data file")
parser.add_argument("-s","--ask",action="store_true",help="set options interactively")
parser.add_argument("-f","--fit",action="store_true",help="fit a function")
parser.add_argument("-m","--map",action="store_true",help="plot a color map")
args,data=parser.parse_known_args()

if((args.d!=None)&(data==[])):
 print("Read from a data file:",args.d)
 readDataObj=readData.readDataClass()
 readDataObj.readData(args.d)
 data=readDataObj.readData(args.d)

if(args.d==None):
 writeDataObj=writeData.writeDataClass()
 writeDataObj.writeData(data)



plotObj=plot.plotClass()

if((args.o==None)&(args.ask==False)&(args.map==False)):	# default options [none]
 optMode="defOpt"
 plotObj.optionsPlot(data,optMode,args.fit)

if((args.ask==True)&(args.map==False)&(args.o==None)):	# ask for options [-s] (generates an options file)
 optMode="setOpt"
 plotObj.optionsPlot(data,optMode,args.fit)

if((args.o!=None)&(args.ask==False)&(args.map==False)):			# read options from a file [-o file]
 plotObj.optFile=args.o

 optMode="readOpt"
 plotObj.optionsPlot(data,optMode,args.fit)



if((args.map==True)&(args.o==None)&(args.ask==False)&(args.fit==False)):			# color map
 optMode="defOpt"
 plotObj.mapPlot(data,optMode)

if((args.map==True)&(args.o==None)&(args.ask==True)&(args.fit==False)):			# color map
 optMode="setOpt"
 plotObj.mapPlot(data,optMode)

