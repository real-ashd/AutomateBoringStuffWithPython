#Copying and Moving Files and Folders
#Using shutil module for copy, paste, move, rename files
#F:\Python Project\FileSystem\hello.txt
import shutil

#Now we copy the file hello.txt to a folder Folder1 using copy() function, it takes 2 args
print(shutil.copy("C:\\Users\\Abc\\Documents\\hello.txt","C:\\Users\\Abc\\Documents\\Folder1"))
#This prints out the path where the file is copied
#We can also copy and rename the file at the same time by specifying the filename at the end 
print(shutil.copy("C:\\Users\\Abc\\Documents\\hello.txt","C:\\Users\\Abc\\Documents\\Folder1\\helloworld.txt"))

#To copy an entire folder and all files and folder inside it use copytree() function, it takes 2 args
print(shutil.copytree("C:\\Users\\Abc\\Documents\\Folder1","C:\\Users\\Abc\\Documents\\Folder1_backup"))

#To move a file from one place to another use move function
#Now we move the file hello.txt to a folder Folder1\Folder2
print(shutil.move("C:\\Users\\Abc\\Documents\\hello.txt","C:\\Users\\Abc\\Documents\\Folder1\\Folder2"))

#To rename a file we have to use move function
print(shutil.move("C:\\Users\\Abc\\Documents\\Folder1\\Folder2\\hello.txt","C:\\Users\\Abc\\Documents\\Folder1\\Folder2\\helloworld.txt"))