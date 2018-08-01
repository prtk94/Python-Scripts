#!python3
#add a prefx to the start of the flename, such as adding my_ to
#rename eggs.txt to spam_eggs.txt
import shutil,os
for oldFilename in os.listdir('.'):
	newFilename= "my"+ oldFilename
	absWorkingDir = os.path.abspath('.')
	newFilename = os.path.join(absWorkingDir,newFilename)
	oldFilename = os.path.join(absWorkingDir,oldFilename)
	print('Renaming "%s" with "%s"...' %(oldFilename,newFilename))
	shutil.move(oldFilename,newFilename)