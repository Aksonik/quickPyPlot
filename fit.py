from scipy.optimize import curve_fit
from pylab import *
import matplotlib.pyplot as plt

class fitClass():

 def __init__(self,x,y):
  self.x=x
  self.y=y

 def fit(self):

  #slope,intercept,r_value,p_value,std_err=stats.linregress(xx,yy)

  def func(x,SR2,TRs,TRf):
   return SR2*exp(-x/TRs)+(1-SR2)*exp(-x/TRf)

  guess=[0.5,50.0,5.0]
  bounds=[(0.0,0.0,0.0),(1.0,1000.0,1000.0)]

  popt,pcov=curve_fit(func,self.x,self.y,p0=guess,sigma=None,absolute_sigma=False,bounds=bounds) 
  #maxfev=1000000

  SR2=popt[0]
  TRs=popt[1]
  TRf=popt[2]

  yfit=func(self.x,SR2,TRs,TRf)

  ### chi2

  sigma=None

  if sigma is None:
   chi2=sum((func(self.x,*popt)-self.y)**2)
  else:
   chi2=sum(((func(self.x,*popt)-self.y)/yerr)**2)
  dof=len(self.y)-len(popt)
  rchi2=chi2/dof

  """
  f=open("fit.res",'w')
  print("TRs:","%5.3f" % TRs,"TRf:","%5.3f" % TRf,"SR2:","%5.3f" % SR2,"chi2:","%5.3f" % chi2,file=f)
  f.close()

  f=open("fit.dat",'w')
  for l in range(0,len(yfit),1):
   print(x[l],yfit[l],file=f)
  f.close()

  text(20,0.70,r'$\tau_{Rs}$ = '+str("%5.3f" % TRs)+r' [ns]',fontsize=20)
  text(20,0.60,r'$\tau_{Rf}$ = '+str("%5.3f" % TRf)+r' [ns]',fontsize=20)
  text(20,0.50,r'$S_{R}^{2}$ = '+str("%5.3f" % SR2),fontsize=20)
  text(20,0.40,r'$\chi^{2}$ = '+str("%5.3f" % chi2),fontsize=20)
  """

  return yfit
