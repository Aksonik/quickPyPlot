import numpy as np
import math
import matplotlib.pyplot
from pylab import *
import sys
import os
import glob

class readOptClass():

 def readOpt(optFile):
  print("Read options from hear:",optFile)

  gplt=open(str(optFile),"r")

  for line in gplt:
   split=line.split(" ")

   if(split[0]=="xCol"):
    xCol=int(split[1])
   if(split[0]=="yCol"):
    yCol=int(split[1])

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
