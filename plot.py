import numpy as np
import matplotlib.pyplot
from pylab import *
import setOpt
import readOpt
import styles

class plotClass():

 def __init__(self):
  self.optFile="-"

 def simplePlot(self,dataFiles):
  for f in dataFiles:
   data=np.loadtxt(f)
   x=data[:,0]
   y=data[:,1]

   plot(x,y)
  savefig("plt.png")
  show()

 def saveOpt(insertOptObj):
  fileOpt=open("plt.opt","w")

  fileOpt.write("xyCol %d %d\n" % (insertOptObj.xyCol[0],insertOptObj.xyCol[1]))
  fileOpt.write("xyErrCol %d %d\n" % (insertOptObj.xyErrCol[0],insertOptObj.xyErrCol[1]))

  fileOpt.write("dataSets %i\n" % insertOptObj.dataSets)
  fileOpt.write("xySubPlt %i %i\n" % (insertOptObj.xySubPlt[0],insertOptObj.xySubPlt[1]))

  fileOpt.write("labels ")
  for i in range(0,len(insertOptObj.labels)):
   if(i<len(insertOptObj.labels)-1):
    fileOpt.write("%s," % insertOptObj.labels[i])
   else:
    fileOpt.write("%s\n" % insertOptObj.labels[i])

  fileOpt.write("logSca %s\n" % insertOptObj.logSca)

  fileOpt.write("xAxis %d %d\n" % (insertOptObj.xAxis[0],insertOptObj.xAxis[1]))
  fileOpt.write("yAxis %d %d\n" % (insertOptObj.yAxis[0],insertOptObj.yAxis[1]))

  fileOpt.close()

 def optionsPlot(self,dataFiles,optMode):

  #fig=figure(figsize=(10,8))
  #fig.subplots_adjust(left=0.12,bottom=0.10,right=0.98,top=0.95,hspace=0.05,wspace=0.05)

  if(optMode=="setOpt"):
   insertOptObj=setOpt.setOptClass(dataFiles)
   insertOptObj.setOpt()

  if(optMode=="readOpt"):
   insertOptObj=readOpt.readOptClass(dataFiles)
   insertOptObj.readOpt(self.optFile)

  ### 1.  1.a) AA: 10%
  ### 2.  1.b) AA: 30%
  ### 3.  1.c) AA:  5%
  ### 4.  2.a) CG: 10%
  ### 5.  2.b) CG: 30%
  ### 6.  2.c) CG:  5%

  dataNum=len(dataFiles)			# total number of input data, e.g. 6
  dataSets=insertOptObj.dataSets		# number of data sets, e.g. 2 - AA, CG
  dataSubsets=int(dataNum/dataSets)		# number of data per set, e.g. 3 - 5%, 10%, 30%

  ### order

  dataFilesOrder=dataFiles
  labelsOrder=insertOptObj.labels 

  if(dataSets>1):
   dataFilesOrder=[]
   labelsOrder=[]
   for i in range(1,dataSubsets+1):
    for j in range(0,dataSets):
     dataFilesOrder.append(dataFiles[(i+j*dataSubsets)-1]) # e.g. 1,4,2,5,3,6
     labelsOrder.append(insertOptObj.labels[(i+j*dataSubsets)-1])

  subPltNum=0

  colorNum=0
  widthNum=0
  styleNum=0

  ax=subplot(1,1,1)

  n=0
  for f in dataFilesOrder:
   n+=1
   data=np.loadtxt(f)

   ### subplots

   if((insertOptObj.xySubPlt[0]>1)|(insertOptObj.xySubPlt[1]>1)):
    if(dataSets>1):
     if(n%dataSets==1):
      subPltNum+=1
      ax=subplot(insertOptObj.xySubPlt[0],insertOptObj.xySubPlt[1],subPltNum) # e.g (1,4)(2,5)(3,6)
    elif(dataSets==1):
     subPltNum+=1
     ax=subplot(insertOptObj.xySubPlt[0],insertOptObj.xySubPlt[1],subPltNum) # e.g (1)(2)(3)(4)(5)(6)

   colorNum=int((n-1)%dataSets)		# e.g. (red,blue)(red,blue)(red,blue)

   ### styles (only when no subplots)

   styleNum=0

   if((insertOptObj.xySubPlt[0]==1)&(insertOptObj.xySubPlt[1]==1)):
    if(dataSets!=1):
     styleNum=int((n-1)%dataSets)
     colorNum=int((n-1)/dataSets)
    if(dataSets==1):
     colorNum=int(n-1)
     styleNum=0

   ### data   

   x=data[:,insertOptObj.xyCol[0]-1]
   y=data[:,insertOptObj.xyCol[1]-1]

   print(n,f,"label:",labelsOrder[n-1],"color:",styles.colors[colorNum],"style:",styles.styles[styleNum])

### plot plot plot plot plot plot plot plot plot plot plot plot plot plot plot plot plot
  
   plot(x,y,\
        color=styles.colors[colorNum],\
        linewidth=styles.widths[widthNum],\
        linestyle=styles.styles[styleNum],\
        label=labelsOrder[n-1])

   if(insertOptObj.xyErrCol[0]!=0):
    xerr=data[:,insertOptObj.xyErrCol[0]-1]
    errorbar(x,y,xerr=xerr)
   if(insertOptObj.xyErrCol[1]!=0):
    yerr=data[:,insertOptObj.xyErrCol[1]-1]
    errorbar(x,y,yerr=yerr)

   if((insertOptObj.logSca=="x")|(insertOptObj.logSca=="xy")):
    ax.set_xscale("log")
   if((insertOptObj.logSca=="y")|(insertOptObj.logSca=="xy")):
    ax.set_yscale("log")

   if(labelsOrder[0]!="-"):
    legend(loc=1,fontsize=12,fancybox=True).get_frame().set_alpha(0.5)

  if(insertOptObj.xAxis[0]<insertOptObj.xAxis[1]):
   xlim(insertOptObj.xAxis[0],insertOptObj.xAxis[1])
  if(insertOptObj.yAxis[0]<insertOptObj.yAxis[1]):
   ylim(insertOptObj.yAxis[0],insertOptObj.yAxis[1])

### plot plot plot plot plot plot plot plot plot plot plot plot plot plot plot plot plot

  if(optMode=="setOpt"):
   plotClass.saveOpt(insertOptObj)

  savefig("plt.png")
  show()
