#!/bin/python

import numpy as np
import math
import matplotlib.pyplot
from pylab import *
import sys
import os
import glob

m=len(sys.argv)-1

if(m==0):
 print("Provide input files.")
 quit()
else:
 print("There is/are "+str(m)+" input file/files.")

for f in sys.argv:
 if not os.path.isfile(str(f)):
  print("File "+str(f)+" does not exist.")
  quit()

if os.path.isfile("gplt.prm"):
 print("Set parameters from the file.")

 gplt=open("gplt.prm","r")

 for line in gplt:
  split=line.split(" ")

  if(split[0]=="Columns:"):
   colx=int(split[1])
   coly=int(split[2])

  if(split[0]=="ErrorColumn:"):
   colxerr=int(split[1])
   colyerr=int(split[2])
 
  if(split[0]=="DataSets:"):
   datasets=int(split[1])

  if(split[0]=="Labels:"):
   labels=split[1].split(",")

  if((split[0]=="Log:")&(len(split)!=1)):
   log=split[1]
 
  if((split[0]=="Xaxis:")&(len(split)==3)):
   xaxis=split[1]





else:
 print("Set parameters interactively:")

 columns_input=raw_input("Which columns plot? [two integers with SPACE] ")
 columns=columns_input.split(" ")

 colx=int(columns[0])
 coly=int(columns[1])

 error_input=raw_input("Do you have errors in the subsequent columns [ENTER - NO, y - YES]?")

 sets=raw_input("How many sets of data do you have here? [enter means 1] ")

 if(sets==""):
  sets=1

 subsets=m/int(sets)
 print "You have",sets,"sets and",subsets,"subsets."

 labels_input=raw_input("Do you want labels? [enter means NO or separate with COMMAS] ")

 if(labels_input!=""):
  labels=labels_input.split(",")
  for l in labels:
   print l

 logsca=raw_input("Do you want logarithmic scales? [enter means NO or X or Y or XY] ")

 xaxis_input=raw_input("Do you want X axis? [enter means NO or two values with SPACE] ")
 yaxis_input=raw_input("Do you want Y axis? [enter means NO or two values with SPACE] ")




colors=["red","blue","black","orange","magenta","brown","gray","green","pink","violet","gold","turquoise"]
linewidth=[4,2,4,4,4,4,4,4,4,4,4,4]
linestyle=["-","-","--",":","-.","-","-","-","-","-","-","-"]
markers=["s"]
alpha=[1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00]


fig=figure(figsize=(10,8))
fig.subplots_adjust(left=0.12,bottom=0.10,right=0.98,top=0.95,hspace=0.05,wspace=0.05)

ax=plt.subplot(1,1,1)

c=-1



labels=["","","","","","","","","","","","","","","","","","","","","","","","","","","",""]


xaxis=xaxis_input.split(" ")
yaxis=yaxis_input.split(" ")

for i in range(1,m+1):
 c=c+1
 print "===",sys.argv[i],"==="

 data=np.loadtxt(sys.argv[i])
 if(columns_input!=""):
  x=data[:,colx-1]
  y=data[:,coly-1] #*10000
  if((error_input=="y")|(error_input=="Y")):
   yerr=data[:,int(columns[2])-1] #*10000
 else:
  x=data[:,0]
  y=data[:,1] #*10000
  if((error_input=="y")|(error_input=="Y")):
   yerr=data[:,2] #*10000

 if((m>12)&(sets==1)):
  plot(x,y)
 else:

#  print "set:",wid,"line width =",linewidth[wid],"line style =",linestyle[0],"subset:",col,"color =",colors[col]

  wid=(i-1)/subsets		### distinguish between sets
  print "   set:",wid,"line width =",linewidth[wid],"line style =",linestyle[wid]
 
  col=(i-1)%subsets		### distinguish between subsets
  print "      subset:",col,"color =",colors[col]

#  plot(x,y,color=colors[c],marker=marker[n],markersize=linewidth[n],linewidth=ls,label=lb[c])
  plot(x,y,color=colors[col],linewidth=linewidth[wid],linestyle=linestyle[wid],alpha=alpha[wid],label=labels[c])
  print(labels)

  if((error_input=="y")|(error_input=="Y")):
   plt.errorbar(x,y,yerr=yerr,color=colors[col])


### label=str(sys.argv[i])

#grid()

#xlabel(r'z [A]',fontsize=20)
#ylabel(r'density [1/nm$^{3}$]',fontsize=20)

xlim(0.8,2.2)

if(xaxis_input!=""):
 xlim(float(xaxis[0]),float(xaxis[1]))
if(yaxis_input!=""):
 ylim(float(yaxis[0]),float(yaxis[1]))
#xticks(np.arange(30,100,2))
#yticks(np.arange(0,60,5))

if((logsca=="X")|(logsca=="XY")|(logsca=="x")|(logsca=="xy")):
 ax.set_xscale("log")
if((logsca=="Y")|(logsca=="XY")|(logsca=="y")|(logsca=="xy")):
 ax.set_yscale("log")

if(labels_input!=""):
 legend(loc=3,fontsize=12,fancybox=True).get_frame().set_alpha(0.5)

#plt.xlabel(r'$z$ [A]',fontsize=20)
#plt.ylabel(r'density [1/nm$^{3}$]', fontsize=20)

plt.xlabel(r'cluster size',fontsize=20)
plt.ylabel(r'proteins [%]', fontsize=20)

#plt.xlabel(r'time [ns]',fontsize=20)
#plt.ylabel(r'contacts', fontsize=20)


#plt.xlabel(r'time [us]',fontsize=20)
#plt.ylabel(r'number of contacts', fontsize=20)

#plt.xlabel(r'time [ns]',fontsize=20)
#plt.ylabel(r'RMSD [A]', fontsize=20)

#plt.xlabel(r'$R$ [nm]',fontsize=20)
#plt.ylabel(r'density [1/nm$^{3}$]', fontsize=20)

grid()
#show()
savefig("plt.png")


show()



### find energy at
# ze=1.1+2.2

# for i in range(0,len(pzz)-1):
#  if((pzz[i]<ze)&(pzz[i+1]>=ze)):
#   print(name,pzz[i],vzz[i])


