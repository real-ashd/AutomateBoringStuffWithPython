#Files And Folders In Python
"""
Functions of os module
os.path.join()		: Combine the folders with correct slashes
os.sep 				: returns the separator of the os
os.path.getcwd()	: returns the current working directory
os.chdir()			: will change the current working directory
os.path.abspath()	: returns the absolute form of the path which is passed
os.path.isabs()		: returns true if the path passed is absolute path (F:\\Folder1\\Folder2)
os.path.relpath()	: returns the relative path between the 2 paths passed. Takes '2' args.
os.makedirs()		: makes folders which is passed to it (abspath or relpath)
os.path.getsize()	: returns a file's size
os.listdir()		: returns a list of string of filenames present in the path passed
os.path.exists()	: returns True if the path exists
os.path.isfile()	: returns True if the path passed is a file
os.path.isdir()		: returns True if the path passed is a dir

"""
#Use '\\' to use escape characters
#This code only works on Windows
print('C:\\spam\\eggs.png')
print('\\')
print(r'C:\spam\eggs.png')
print('\\'.join(['Folder1','Folder2','Folder3','file.png']))
print('------------------------------------------------------')

#For Using path in all Operating systems we use os module
import os

#Using os.path.join() function which is used to join a bunch of strings
print(os.path.join('Folder1','Folder2','Folder3','file.png'))		#Windows use '\' and linux and mac uses '/'
print(os.sep)			#Prints the path separator

#Using os.getcwd() function which prints the current working directory
print(os.getcwd())		#Current Working Directory

#Using os.chdir('C:\') function 
os.chdir('C:\\')		#Changes the current working directory
print(os.getcwd())

# 'spam.png' is an example of Relative Paths
#There are two file paths Absolute File Path or full path ('F:\Python Project\FileSystem\spam.png') and Relative File Path ('spam.png')

#Using '.'(means current folder) and '..'(means parent folder)
#eg : IF cwd is 'F:\Python Project\FileSystem' then '.' means "FileSystem" folder and '..' means "Python Project"

os.chdir('F:\\Python Project\\FileSystem\\')		#Changes the current working directory
print(os.getcwd())
print('------------------------------------------------------')

#Using os.path.abspath() function and os.path.isabs() function
print(os.path.abspath('spam.png'))			#This returns the absolute path from a relative path 
print(os.path.abspath('..\\..\\spam.png'))

print(os.path.isabs('spam.png'))			#This returns True if the path passed is absolute path
print(os.path.isabs('F:\\Python Project\\FileSystem\\spam.png'))

#Using os.path.relpath() function. This function takes two args, 1st is the abs path and 2nd a starting point
print(os.path.relpath('C:\\Folder1\\Folder2\\Folder3\\spam.png','C:\\Folder1'))		#This returns the relative path from absolute path
print('------------------------------------------------------')

#Using functions os.path.dirname() and os.path.basename()
#To find out the directory part or filename part from a path
print(os.path.dirname('F:\\Python Project\\FileSystem\\spam.png'))		#Prints the directory part
print(os.path.basename('F:\\Python Project\\FileSystem\\spam.png'))		#Prints the filename with extention part
print(os.path.basename('F:\\Python Project\\FileSystem'))				#It pulls out the last foldername if filename is not present
print('------------------------------------------------------')

#Using os.path.exists(), this checks if a path exists or not in your system
print(os.path.exists('F:\\Python Project\\FileSystem'))
print(os.path.exists('F:\\Python Project\\FileSystem\\spam.png'))
print()

#Using os.path.isfile() and os.path.isdir() to find if a file or directory exists in your system
print(os.path.isdir('F:\\Python Project\\FileSystem'))
print(os.path.isdir('F:\\Python Project\\FileSystem\\Folder1'))
print(os.path.isdir('F:\\Python Project\\FileSystem\\spam.png'))
print()

print(os.path.isfile('F:\\Python Project\\FileSystem\\spam.png'))
print(os.path.isfile('F:\\Python Project\\FileSystem'))
print(os.path.isfile('F:\\Python Project\\FileSystem\\FilesAndFoldersInPython.py'))
print('------------------------------------------------------')

#Using os.path.getsize(), this prints the size of the file or folder
#Using os.listdir(), this lists the files and folder in the specified path
print(os.path.getsize('F:\\Python Project\\FileSystem\\FilesAndFoldersInPython.py'))
print(os.path.getsize('F:\\Python Project\\'))
print(os.listdir('C:\\'))
print(os.listdir('F:\\Python Project\\'))
print('------------------------------------------------------')

#Program to find the total size of all the files in a folder
totalsize=0
for filename in os.listdir("F:\\Python Project\\LoopsAndControlStatements"):
	if not os.path.isfile(os.path.join("F:\\Python Project\\LoopsAndControlStatements",filename)):
		continue
	totalsize+=os.path.getsize('F:\\Python Project\\LoopsAndControlStatements')
print(totalsize)
print('------------------------------------------------------')

#Using os.makedirs(), this will create the folder in the path specified
print(os.path.isdir('F:\\Folder1'))
os.makedirs('Folder1\\Folder2\\Folder3')
print(os.path.isdir('F:\\Folder1\\Folder2\\Folder3'))
print(os.getcwd())
print(os.listdir(os.getcwd()+"\\Folder1"))