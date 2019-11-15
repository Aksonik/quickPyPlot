import numpy as np
import matplotlib.pyplot
from pylab import *
import setOpt
import styles

class plotClass:

 def simplePlot(dataFiles):
  print("Only the data are provided - plot the simplest possible figure:")

  for f in dataFiles:
   data=np.loadtxt(f)
   x=data[:,0]
   y=data[:,1]

   plot(x,y)
  savefig("plt.png")
  show()

 def saveOpt(setOptObj):
  fileOpt=open("plt.opt","w")

  fileOpt.write("xyCol %d %d\n" % (setOptObj.xyCol[0],setOptObj.xyCol[1]))
  fileOpt.write("xyErrCol %d %d\n" % (setOptObj.xyErrCol[0],setOptObj.xyErrCol[1]))


  fileOpt.write("dataSets %i\n" % setOptObj.dataSets)
  fileOpt.write("xySubPlt %i %i\n" % (setOptObj.xySubPlt[0],setOptObj.xySubPlt[1]))

  fileOpt.write("labels ")
  for i in range(0,len(setOptObj.labels)):
   if(i<len(setOptObj.labels)-1):
    fileOpt.write("%s," % setOptObj.labels[i])
   else:
    fileOpt.write("%s" % setOptObj.labels[i])
  fileOpt.write("\n")

  fileOpt.write("logSca %s\n" % setOptObj.logSca)

  fileOpt.write("xAxis %d %d\n" % (setOptObj.xAxis[0],setOptObj.xAxis[1]))
  fileOpt.write("yAxis %d %d\n" % (setOptObj.yAxis[0],setOptObj.yAxis[1]))

  fileOpt.close()

 def optionsPlot(dataFiles):
  print("Only the data are provided - set plotting options interactively:")

  #fig=figure(figsize=(10,8))
  #fig.subplots_adjust(left=0.12,bottom=0.10,right=0.98,top=0.95,hspace=0.05,wspace=0.05)

  setOptObj=setOpt.setOptClass(dataFiles)
  setOptObj.setOpt()

  dataNum=len(dataFiles)		# total number of input data, e.g. 6
  dataSets=setOptObj.dataSets		# number of data sets, e.g. 2
  dataSubsets=int(dataNum/dataSets)	# number of data per set, e.g. 3

  dataFilesOrder=dataFiles
 
  if(dataSets>1):
   dataFilesOrder=[]
   for i in range(1,dataSubsets+1):
    for j in range(0,dataSets):
     dataFilesOrder.append(dataFiles[(i+j*dataSubsets)-1])	# order data, e.g. 1,4,2,5,3,6

  n=0
  subPltNum=0

  colorNum=0
  widthNum=0
  styleNum=0

  ax=subplot(1,1,1)

  for f in dataFilesOrder:
   n+=1
   data=np.loadtxt(f)

   if((dataSets>1)&((setOptObj.xySubPlt[0]!=1)|(setOptObj.xySubPlt[1]!=1))):

    if(n%2==1):
     subPltNum+=1
     ax=subplot(setOptObj.xySubPlt[0],setOptObj.xySubPlt[1],subPltNum)

   x=data[:,setOptObj.xyCol[0]-1]
   y=data[:,setOptObj.xyCol[1]-1]

   colorNum=int((n-1)%dataSubsets)
   styleNum=int((n-1)%dataSets)
   print(n,f,"color:",styles.colors[colorNum],"style:",styles.styles[styleNum])
  
   plot(x,y,\
        color=styles.colors[colorNum],\
        linewidth=styles.widths[widthNum],\
        linestyle=styles.styles[styleNum],\
        label=setOptObj.labels[n-1])

   if(setOptObj.xyErrCol[0]!=0):
    xerr=data[:,setOptObj.xyErrCol[0]-1]
    errorbar(x,y,xerr=xerr)
   if(setOptObj.xyErrCol[1]!=0):
    yerr=data[:,setOptObj.xyErrCol[1]-1]
    errorbar(x,y,yerr=yerr)

   if((setOptObj.logSca=="x")|(setOptObj.logSca=="xy")):
    ax.set_xscale("log")
   if((setOptObj.logSca=="y")|(setOptObj.logSca=="xy")):
    ax.set_yscale("log")

  if(setOptObj.labels[0]!="-"):
   legend(loc=1,fontsize=12,fancybox=True).get_frame().set_alpha(0.5)

  if(setOptObj.xAxis[0]<setOptObj.xAxis[1]):
   xlim(setOptObj.xAxis[0],setOptObj.xAxis[1])
  if(setOptObj.yAxis[0]<setOptObj.yAxis[1]):
   ylim(setOptObj.yAxis[0],setOptObj.yAxis[1])

  plotClass.saveOpt(setOptObj)

  savefig("plt.png")
  show()
