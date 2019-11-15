from pylab import *
from numpy import *

import matplotlib.pyplot as plt
import sys

fig=figure(figsize=(8,6))
fig.subplots_adjust(left=0.12,bottom=0.12,right=0.94,top=0.94)

#input="interactionmap.20"
input="interactionmap.nocut"

#output="map_cut.png"
output="map_poster.png"

d=np.loadtxt(input)

dx=d[:,0]
dy=d[:,1]
dz=d[:,2]

print(min(dz),"-",max(dz))

valmin=15.0
valmax=25.0

#valmin=min(dz)
#valmax=max(dz)

dz[dz>valmax]=valmin
dz[dz==0.0]=valmax

#for i in dz:
# print i

matrix=np.loadtxt(dx)
matriy=np.loadtxt(dy)
matriz=np.loadtxt(dz)

jy=0
jx=1
Z=np.zeros((36,36))

for i in range(matrix.shape[0]):

   jy+=1
   Z[jx-1,jy-1]=matriz[i]
   if np.mod(jy,36)==0:
      jy=0
      jx+=1
   if np.mod(jx,36)==0:
      jx=0


x=np.arange(0,36,1)
y=np.arange(0,36,1)

X,Y=np.meshgrid(x,y)

extent=(0,36,0,36)



#palette=plt.matplotlib.colors.LinearSegmentedColormap('jet3',plt.cm.datad['jet'],2048)

#plt.imshow(Z,extent=extent,cmap="hot",origin='lower',vmin=min(matriz),vmax=max(matriz),aspect='auto',interpolation='lanczos')



my_cmap = matplotlib.cm.get_cmap('jet_r')
#my_cmap.set_over('w')
#my_cmap.set_under('w')

vmin=min(matriz[nonzero(matriz)])
vmax=max(matriz[nonzero(matriz)])
print(vmin,"-",vmax)

#b=(vmax-vmin)/20.0
#bb=arange(vmin,vmax+b,b)

bbcont=arange(valmin,valmax+1.0,1.0)
bb=arange(valmin,valmax+0.2,0.2)

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

xlim(0,36)
ylim(0,36)

xticks(arange(5,40,5),fontsize=20)
yticks(arange(5,40,5),fontsize=20)

savefig(output)
#plt.show()
