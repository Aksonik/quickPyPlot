class writeDataClass():

 def writeData(self,dataFiles):
  fileData=open("plt.dat","w")

  for f in range(0,len(dataFiles)):
   fileData.write("%s\n" % dataFiles[f])

  fileData.close()

