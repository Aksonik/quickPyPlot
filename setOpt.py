import numpy as np
import math
import matplotlib.pyplot
from pylab import *
import sys
import os
import glob

class setOptClass():

 def __init__(self,dataFiles):
  self.xyCol=[1,2]
  self.xyErrCol=[0,0]
  self.dataSets=1
  self.xySubPlt=[1,1]
  self.dataFiles=dataFiles

  self.labels=[]
  for i in range(0,len(dataFiles)):	# generates empty labels
   self.labels.append("-")

  self.logSca="-"
  self.xAxis=[0,0]
  self.yAxis=[0,0]

  self.xTitle="-"
  self.yTitle="-"

  self.title="-"

  self.grid="-"

  self.xMargin=[0.15,0.95]
  self.yMargin=[0.15,0.95]

  self.xySize=[6,3]

  self.xySubSpace=[0.05,0.05]

  self.colors=["red","blue","black","orange","magenta","brown","gray","green","pink","violet","gold","turquoise","navy","silver"]
  self.widths=[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,2.0,3.0,4.0,5.0]
  self.styles=["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","--",":","-.","-",""]
  self.markers=["","","","","","","","","","","","","","","","","","","","","","","","","","",".","o","s","^","d","p","*","x","+"]
  self.alphas=[1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,0.75,0.50]

  ### map

  self.xyzCol=[1,2,3]

 ### regular plot

 def setOpt(self):
  xyCol_input=input("Columns - x y [int int] (ENTER - 1 2): ")
  if(xyCol_input!=""):
   xyColSplit=xyCol_input.split(" ")
   self.xyCol=[int(xyColSplit[0]),int(xyColSplit[1])]

  xyErrCol_input=input("Columns - xErr yErr [int int] (ENTER | 0 - none): ")
  if(xyErrCol_input!=""):
   xyErrColSplit=xyErrCol_input.split(" ")
   self.xyErrCol=[int(xyErrColSplit[0]),int(xyErrColSplit[1])]

  dataSets=input("Sets - n [int] (ENTER - 1): ")
  if(dataSets!=""):
   self.dataSets=int(dataSets)

  subPlt_input=input("Subplots - x y [int int] (ENTER - 1 1): ")
  if(subPlt_input!=""):
   subPltSplit=subPlt_input.split(" ")
   self.xySubPlt=[int(subPltSplit[0]),int(subPltSplit[1])]

  labels_input=input("Labels - lab1,lab2, etc. [str,str etc.] (ENTER - none, p - paths): ")
  if(labels_input!=""):
   if(labels_input=="p"):
    for i in range(0,len(self.dataFiles)):	# greek letters: $\lambda$
     self.labels[i]=self.dataFiles[i]
   else:
    labels_split=labels_input.split(",")
    for i in range(0,len(labels_split)):		# substitutes empty labels
     self.labels[i]=labels_split[i]

  logSca_input=input("Logarithmic scales - x | y | xy (ENETER - none): ")
  if(logSca_input!=""):
   self.logSca=logSca_input

  xAxis_input=input("X axis - float float (ENTER - none): ")
  if(xAxis_input!=""):
   xAxis=xAxis_input.split(" ")
   self.xAxis=[float(xAxis[0]),float(xAxis[1])]

  yAxis_input=input("Y axis - float float (ENTER - none): ")
  if(yAxis_input!=""):
   yAxis=yAxis_input.split(" ")
   self.yAxis=[float(yAxis[0]),float(yAxis[1])]

  xTitle_input=input("X axis title - string (ENTER - none): ")
  if(xTitle_input!=""):
   xTitle=xTitle_input
   self.xTitle=str(xTitle)

  yTitle_input=input("Y axis title - string (ENTER - none): ")
  if(yTitle_input!=""):
   yTitle=yTitle_input
   self.yTitle=str(yTitle)

  title_input=input("Figure title - string (ENTER - none): ")
  if(title_input!=""):
   title=title_input
   self.title=str(title)

  grid_input=input("Grid - yes | no [string] (ENTER - no): ")
  if(grid_input=="yes"):
   self.grid="yes"
  elif(grid_input=="no"):
   self.grid="-"

  xMargin_input=input("X margin - left right (ENTER - 0.15 0.95): ")
  if(xMargin_input!=""):
   xMargin=xMargin_input.split(" ")
   self.xMargin=[float(xMargin[0]),float(xMargin[1])]

  yMargin_input=input("Y margin - bottom top (ENTER - 0.15 0.95): ")
  if(yMargin_input!=""):
   yMargin=yMargin_input.split(" ")
   self.yMargin=[float(yMargin[0]),float(yMargin[1])]

  xySize_input=input("Canvas size - x y (ENTER - 6 3): ")
  if(xySize_input!=""):
   xySize=xySize_input.split(" ")
   self.xySize=[float(xySize[0]),float(xySize[1])]

  xySubSpace_input=input("Subplot space - x y (ENTER - 0.05 0.05): ")
  if(xySubSpace_input!=""):
   xySubSpace=xySubSpace_input.split(" ")
   self.xySubSpace=[float(xySubSpace[0]),float(xySubSpace[1])]

  colors_input=input("Colors - col1,col2, etc. [str,str etc.] (ENTER - default): ")
  if(colors_input!=""):
   colors_split=colors_input.split(",")
   for i in range(0,len(colors_split)):
    self.colors[i]=colors_split[i]

  widths_input=input("Widths - wid1,wid2, etc. [float,float etc.] (ENTER - default): ")
  if(widths_input!=""):
   widths_split=widths_input.split(",")
   for i in range(0,len(widths_split)):
    self.widths[i]=widths_split[i]

  styles_input=input("Styles - sty1,sty2, etc. [str,str etc.] (ENTER - default): ")
  if(styles_input!=""):
   styles_split=styles_input.split(",")
   for i in range(0,len(styles_split)):
    self.styles[i]=styles_split[i]

  markers_input=input("Markers - mar1,mar2, etc. [str,str etc.] (ENTER - default): ")
  if(markers_input!=""):
   markers_split=markers_input.split(",")
   for i in range(0,len(markers_split)):
    self.markers[i]=markers_split[i]

  alphas_input=input("Alphas - alp1,alp2, etc. [float,float etc.] (ENTER - default): ")
  if(alphas_input!=""):
   alphas_split=alphas_input.split(",")
   for i in range(0,len(alphas_split)):
    self.alphas[i]=alphas_split[i]

 ### color map

 def setOptMap(self):
  xyzCol_input=input("Columns - x y z [int int int] (ENTER - 1 2 3): ")
  if(xyzCol_input!=""):
   xyzColSplit=xyzCol_input.split(" ")
   self.xyzCol=[int(xyzColSplit[0]),int(xyzColSplit[1]),int(xyzColSplit[2])]

  dataSets=input("Sets - n [int] (ENTER - 1): ")
  if(dataSets!=""):
   self.dataSets=int(dataSets)

  subPlt_input=input("Subplots - x y [int int] (ENTER - 1 1): ")
  if(subPlt_input!=""):
   subPltSplit=subPlt_input.split(" ")
   self.xySubPlt=[int(subPltSplit[0]),int(subPltSplit[1])]
