#!/bin/python

import numpy as np
import math
import matplotlib.pyplot
from pylab import *
import sys

fig=figure(figsize=(8,4))
fig.subplots_adjust(left=0.14,bottom=0.12,right=0.98,top=0.95,hspace=0.05,wspace=0.05)

ax=plt.subplot(1,1,1)

data=np.loadtxt("tra_a.dat")

x=data[:,0]
y=data[:,1]
yerr=data[:,2]

print(x,y)

barwidth=0.4
plt.bar(x,y,barwidth,color='b',label='non-membrane',yerr=yerr,alpha=0.8,capsize=7)

###

data=np.loadtxt("tra_b.dat")

x=data[:,0]
y=data[:,1]
yerr=data[:,2]

plt.bar(x+barwidth,y,barwidth,color='g',label="membrane",yerr=yerr,alpha=0.8,capsize=7)

xlim(0.6,4)
ylim(0,3.0)
#xticks(np.arange(1.00,1.22,0.02))
yticks(arange(0,3.5,0.5),fontsize=24)

legend(loc=1,fontsize=24,fancybox=True).get_frame().set_alpha(0.5)
#grid()
#show()

#plt.xlabel(r'cluster size',fontsize=20)
plt.ylabel(r'D$_t$ [nm$^2$/ns]', fontsize=20)

plt.xticks([1,2,3],['1VII','1GB1','1UBQ'],fontsize=28)

savefig("tra.png")
plt.show()
