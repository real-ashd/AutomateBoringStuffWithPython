#Delting files and folders
#Be careful as this doesn't sent the file/folders to Recycle bin
import shutil
import os
"""Using os module"""
# print(os.unlink(r'C:\Users\Abc\Documents\Folder1\hello.txt'))	#Use os.unlink() to delete a file

# print(os.rmdir(r'C:\Users\Abc\Documents\Folder1\Folder2'))	#To use os.rmdir() the folder must be completely empty


"""Using shutil module"""

# print(shutil.rmtree(r'C:\Users\Abc\Documents\Folder1\Folder2'))	#shutil module has a function shutil.rmtree() which removes the complete tree

#Program to verify what we are deleting
#use the below program by commenting and uncommenting the statements to verify
"""
print(os.getcwd())
os.chdir('C:\\Users\\Abc\\Documents\\Folder1')
for filename in os.listdir():
	if filename.endswith('.txt'):
		#os.unlink
		print(filename)
"""

print("Using send2trash module.")
#Install the send2trash module using pip as it doesn't come with standard python package
#py -m pip install send2trash(Windows)		pip install send2trash(Linux)
import send2trash
# send2trash.send2trash((r'C:\Users\Abc\Documents\Folder1\hello.txt'))	#Check your recycle bin