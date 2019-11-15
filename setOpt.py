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

  self.labels=[]
  for i in range(0,len(dataFiles)):	# generates empty labels
   self.labels.append("-")

  self.logSca="-"
  self.xAxis=[0,0]
  self.yAxis=[0,0]

 def setOpt(self):
  xyCol_input=input("Columns - x y [int int] (ENTER - 1 2): ")
  if(xyCol_input!=""):
   xyColSplit=xyCol_input.split(" ")
   self.xyCol=[int(xyColSplit[0]),int(xyColSplit[1])]
#   self.yCol=int(xyColSplit[1])

  xyErrCol_input=input("Columns - xErr yErr [int int] (ENTER | 0 - none): ")
  if(xyErrCol_input!=""):
   xyErrColSplit=xyErrCol_input.split(" ")
   self.xyErrCol=[int(xyErrColSplit[0]),int(xyErrColSplit[1])]

  dataSets=input("Sets - n [int] (ENTER - 1): ")
  if(dataSets!=""):
   self.dataSets=int(dataSets)

  subPlt_input=input("Subplots - x y [int int] (ENTER - none): ")
  if(subPlt_input!=""):
   subPltSplit=subPlt_input.split(" ")
   self.xySubPlt=[int(subPltSplit[0]),int(subPltSplit[1])]

  labels_input=input("Labels - lab1,lab2, etc. [str,str etc.] (ENTER - none): ")
  if(labels_input!=""):
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
