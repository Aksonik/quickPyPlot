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
 print("Read data from a file:",args.d)
 readDataObj=readData.readDataClass()
 readDataObj.readData(args.d)
 data=readDataObj.readData(args.d)

if((args.d==None)&(data!=[])):
 print("Read data:",data)
 writeDataObj=writeData.writeDataClass()
 writeDataObj.writeData(data)



plotObj=plot.plotClass()

if(args.map==False):
 print("Plot type: regular")

 if(args.fit==True):
  print(" Fit a function:")

 if((args.o==None)&(args.ask==False)):
  print(" Default options:")
  optMode="defOpt"
  plotObj.optionsPlot(data,optMode,args.fit)

 if((args.o==None)&(args.ask==True)):
  print(" Set options [-s]:")
  optMode="setOpt"
  plotObj.optionsPlot(data,optMode,args.fit)

 if((args.o!=None)&(args.ask==False)):
  print(" Read options from a file [-o]:", args.o)
  plotObj.optFile=args.o
  optMode="readOpt"
  plotObj.optionsPlot(data,optMode,args.fit)



if((args.map==True)&(args.fit==False)):
 print("Plot type: color map [-m]:")

 if((args.o==None)&(args.ask==False)):
  print(" Default options:")  
  optMode="defOpt"
  plotObj.mapPlot(data,optMode)

 if((args.o==None)&(args.ask==True)):	
  print(" Set options [-s]:")  
  optMode="setOpt"
  plotObj.mapPlot(data,optMode)

 if((args.o!=None)&(args.ask==False)):
  print(" Read options from a file [-o]:", args.o)
  plotObj.optFile=args.o
  optMode="readOpt"
  plotObj.mapPlot(data,optMode)
