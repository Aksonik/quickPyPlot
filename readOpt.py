import numpy as np
import math
import matplotlib.pyplot
from pylab import *
import sys
import os
import glob

class readOptClass():

 def __init__(self,dataFiles):
  self.xyCol=[1,2]
  self.xyErrCol=[0,0]
  self.dataSets=1
  self.xySubPlt=[1,1]

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

  self.xMargin=[0.15,0.96]
  self.yMargin=[0.18,0.95]

  self.xySize=[6,3]

  self.xySubSpace=[0.05,0.05]

  self.colors=["red","blue","black","orange","magenta","brown","gray","green","pink","violet","gold","turquoise","navy","silver"]
  self.widths=[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,2.0,3.0,4.0,5.0]
  self.styles=["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","--",":","-.","-",""]
  self.markers=["","","","","","","","","","","","","","","","","","","","","","","","","","",".","o","s","^","d","p","*","x","+"]
  self.alphas=[1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,0.75,0.50]

  # map

  self.xyzCol=[1,2,3]	

 def readOpt(self,optFile):
  print("Read options from:",optFile)

  gplt=open(str(optFile),"r")

  for line in gplt:
   split=line.split(" ")

   if(split[0]=="xyCol"):
    self.xyCol[0]=int(split[1])
    self.xyCol[1]=int(split[2])
   if(split[0]=="xyErrCol"):
    self.xyErrCol[0]=int(split[1])
    self.xyErrCol[1]=int(split[2])
   if(split[0]=="dataSets"):
    self.dataSets=int(split[1])
   if(split[0]=="xySubPlt"):
    self.xySubPlt[0]=int(split[1])
    self.xySubPlt[1]=int(split[2])


   if(split[0]=="labels"):
    labels_split=str(" ".join(split[1:])).split(",")
    for i in range(0,len(labels_split)):		# substitutes empty labels
     self.labels[i]="".join(labels_split[i].rstrip())		# rstrip removes \n

   if(split[0]=="logSca"):
    self.logSca=split[1]

   if(split[0]=="xAxis"):
    self.xAxis[0]=float(split[1])
    self.xAxis[1]=float(split[2])

   if(split[0]=="yAxis"):
    self.yAxis[0]=float(split[1])
    self.yAxis[1]=float(split[2])

   if(split[0]=="xTitle"):
    self.xTitle=str(" ".join(split[1:]))
   if(split[0]=="yTitle"):
    self.yTitle=str(" ".join(split[1:]))

   if(split[0]=="title"):
    self.title=str(" ".join(split[1:]))

   if(split[0]=="grid"):
    self.grid=split[1]

   if(split[0]=="xMargin"):
    self.xMargin[0]=float(split[1])
    self.xMargin[1]=float(split[2])

   if(split[0]=="yMargin"):
    self.yMargin[0]=float(split[1])
    self.yMargin[1]=float(split[2])

   if(split[0]=="xySize"):
    self.xySize[0]=float(split[1])
    self.xySize[1]=float(split[2])

   if(split[0]=="xySubSpace"):
    self.xySubSpace[0]=float(split[1])
    self.xySubSpace[1]=float(split[2])

   if(split[0]=="colors"):
    colors_split=split[1].split(",")
    for i in range(0,len(colors_split)):
     self.colors[i]=colors_split[i].rstrip()

   if(split[0]=="widths"):
    widths_split=split[1].split(",")
    for i in range(0,len(widths_split)):
     self.widths[i]=widths_split[i].rstrip()

   if(split[0]=="styles"):
    styles_split=split[1].split(",")
    for i in range(0,len(styles_split)):
     self.styles[i]=styles_split[i].rstrip()

   if(split[0]=="markers"):
    markers_split=split[1].split(",")
    for i in range(0,len(markers_split)):
     self.markers[i]=markers_split[i].rstrip()

   if(split[0]=="alphas"):
    alphas_split=split[1].split(",")
    for i in range(0,len(alphas_split)):
     self.alphas[i]=alphas_split[i].rstrip()

  gplt.close()

 def readOptMap(self,optFile):
  print("Read options from:",optFile)

  gplt=open(str(optFile),"r")

  for line in gplt:
   split=line.split(" ")

   if(split[0]=="xyzCol"):
    self.xyzCol[0]=int(split[1])
    self.xyzCol[1]=int(split[2])
    self.xyzCol[2]=int(split[3])
   if(split[0]=="dataSets"):
    self.dataSets=int(split[1])
   if(split[0]=="xySubPlt"):
    self.xySubPlt[0]=int(split[1])
    self.xySubPlt[1]=int(split[2])

  gplt.close()
