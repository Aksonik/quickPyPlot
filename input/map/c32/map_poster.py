from pylab import *
from numpy import *

import matplotlib.pyplot as plt
import sys

#fig=figure(figsize=(8,6))
#fig.subplots_adjust(left=0.12,bottom=0.12,right=0.94,top=0.94)

#input="contacts.res"
input="contacts_20x36.res"
#input="contacts_36x30.res"
output="map_poster.png"

d=np.loadtxt(input)

dx=d[:,0]
dy=d[:,1]
dz=d[:,2]

### matrix dimension

for i in range(1,len(dy)):	# x1,y1 -> x1,y2 -> x1,y3 -> ...
 if(dy[i]<dy[i-1]):
  ny=i
  nx=int(len(dx)/ny)
  break

for i in range(1,len(dx)):	# x1,y1 -> x2,y1 -> x3,y1 -> ...
 if(dx[i]<dx[i-1]):
  nx=i
  ny=int(len(dy)/nx)
  break

print("dimension:",nx,ny)

### matrix

Z=np.zeros((nx,ny))

for i in range(0,len(dx)):
 ix=int(dx[i]-1)
 iy=int(dy[i]-1)
 Z[ix,iy]=dz[i]

Z=np.transpose(Z)	# pyplot interprets x column as y, and vice versa

extent=(0,nx,0,ny)

my_cmap=matplotlib.cm.get_cmap('jet_r')
#my_cmap.set_over('w')
#my_cmap.set_under('w')

vmin=min(dz[nonzero(dz)])
vmax=max(dz[nonzero(dz)])
#print(vmin,"-",vmax)


valmin=min(dz)
valmax=max(dz)

dz[dz>valmax]=valmin
dz[dz==0.0]=valmax


bbcont=arange(valmin,valmax+1.0,1.0)
bb=arange(valmin,valmax+0.2,0.2)

#palette=plt.matplotlib.colors.LinearSegmentedColormap('jet3',plt.cm.datad['jet'],2048)

#plt.imshow(Z,extent=extent,cmap="hot",origin='lower',vmin=min(dz),vmax=max(dz),aspect='auto',interpolation='lanczos')
### origin='lower',aspect='auto',interpolation='lanczos' 
map=plt.contour(Z,bbcont,extent=extent,vmin=valmin,vmax=valmax,linewidths=0.5,colors='k',alpha=0.5)
map=plt.contourf(Z,bb,extent=extent,cmap=my_cmap,vmin=valmin,vmax=valmax)

cb=plt.colorbar(map)
cb.set_clim(vmin=valmin,vmax=valmax)
cb.set_ticks(arange(valmin,valmax+2.0,2.0))
cb.ax.tick_params(labelsize=20)
cb.set_ticklabels(arange(valmin,valmax+2.0,2.0))

cb.set_label(r'average minimum C$\alpha$ distance [$\AA$]',fontsize=24)

plt.ylabel(r'closest residue',fontsize=24)
plt.xlabel(r'residue',fontsize=24)

xlim(0,nx)
ylim(0,ny)

#xticks(arange(5,40,5),fontsize=20)
#yticks(arange(5,40,5),fontsize=20)

savefig(output)
plt.show()
