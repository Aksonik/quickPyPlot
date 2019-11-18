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

 def readOpt(self,optFile):
  print("Read options from hear:",optFile)

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
    labels_split=split[1].split(",")
    for i in range(0,len(labels_split)):		# substitutes empty labels
     self.labels[i]=labels_split[i]

   if(split[0]=="logSca"):
    self.logSca=split[1]

   if(split[0]=="xAxis"):
    self.xAxis[0]=int(split[1])
    self.xAxis[1]=int(split[2])

   if(split[0]=="yAxis"):
    self.yAxis[0]=int(split[1])
    self.yAxis[1]=int(split[2])

  gplt.close()





"""
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
"""
