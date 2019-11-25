class readDataClass():
 def readData(self,readDataFile):
  fileData=open(str(readDataFile),"r")
  data=[]
  for f in fileData:
   data.append(f.rstrip('\n	'))
  fileData.close()
  return data

