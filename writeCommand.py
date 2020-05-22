class writeCommandClass():

 def writeCommand(self,command):
  fileCommand=open("plt.sh","w")
  fileCommand.write("%s\n" % command)
  fileCommand.close()

