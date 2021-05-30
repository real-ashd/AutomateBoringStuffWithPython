#Walking A Directory Tree
import os
import shutil
#Using os.walk() function
for folderName, subFolders, fileNames in os.walk(r"C:\Users\Abc\Documents\Folder1"):
	print("The folder is",folderName)
	print("The subfolder in",folderName,"are:",str(subFolders))
	print("The files in",folderName,"are:",str(fileNames))
	print()

	# for subFolder in subFolders:
	# 	if 'fish' in subFolder:
	# 		#os.rmdir(subFolder)
	# 		print('rm on',subFolder)

	# for file in fileNames:
	# 	if file.endswith('.txt'):
	# 		shutil.copy(os.join(folderName,file),os.join(folderName,file+'.backup'))
	# 		print('\t',file)