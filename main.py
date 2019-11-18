import argparse
import sys

import readOpt
import plot	# module

parser=argparse.ArgumentParser(description="Parse options.")
parser.add_argument("-o",type=str,help="options file")
parser.add_argument("-d",type=str,help="data file")
parser.add_argument("-s","--foo",action="store_true",help="set options")
args,data=parser.parse_known_args()

plotObj=plot.plotClass()
readOptObj=readOpt.readOptClass(data)

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




#else:
# print("set options")


#m=len(sys.argv)-1
#print(m) 

"""
m=len(sys.argv)-1

if(m==0):
 opt=setOpt.setOptClass
 opt.setOpt()
elif(m==1):
 readOptFun()
"""



"""
 print("There is/are "+str(m)+" input file/files.")

for f in sys.argv:
 if not os.path.isfile(str(f)):
  print("File "+str(f)+" does not exist.")
  quit()

if os.path.isfile("gplt.prm"):
 print("Set parameters from the file.")

"""

