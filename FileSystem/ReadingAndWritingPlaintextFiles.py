#Reading and Writing Plaintext (.txt) files
#All other file types such as .doc,.ppt,.pdf are binary files

#open(), read() and close() methods 
#readlines()
# import os
# print(os.getcwd())

print('Reading from a file\n')
#open('filename.ext') method, this will open the file 'filename.ext' in read mode
#read mode is default mode

#Using open(), read() and close() methods 
hellofile = open('F:\\Python Project\\FileSystem\\hello.txt')
print(hellofile.read())			#We can only read the contents of the file once to read again we have to open the file again.
# content=hellofile.read()
hellofile.close()
# print(content)
print()

#Using readlines() method
#read() returns a single string but readlines() returns a list of strings
hellofile = open('F:\\Python Project\\FileSystem\\hello.txt')
print(hellofile.readlines())
hellofile.close()
print('--------------------------------------------')

print('Writing to a file\n')
#Writing to a file is not possible in read mode so we have to use append mode('a') or write mode('w')
#append mode writes at the end of a file and write mode overwrites the files
#In both these mode if the file doesn't exist then a new file will be created
heyFile = open('F:\\Python Project\\FileSystem\\hey.txt','w')
print(heyFile.write("Hello!!!!!!!!!!!!!!!!!!!!!!!!!!\n"))		#Returns how many bytes were written to the file
print(heyFile.write("Hello!!!!!!!!!!!!!!!!!!!!!!!!!!\n"))
print(heyFile.write("Hello!!!!!!!!!!!!!!!!!!!!!!!!!!\n"))
heyFile.close()
heyFile = open('F:\\Python Project\\FileSystem\\hey.txt')
print(heyFile.read())
heyFile.close()
print('--------------------------------------------')

#Shelve Module
"""
The shelve module can be used as a simple persistent storage option for Python objects when a relational database is overkill.
The shelf is accessed by keys, just as with a dictionary.
The values are pickled and written to a database created and managed by anydbm.
The objects created are stored in the form of binary files
"""
import shelve
shelfFile = shelve.open('mydata')							
#you can treat shelfFile variable as a dictionary			
shelfFile['cats'] = ['zophie','puka','simon','fat-tail']	
shelfFile.close()											
"""
The above code will create 3 files in current working directory if os is windows, files are mydata.bak, mydata.dat and mydata.dir
and only one file if the os is linux based i.e. mydb

print(shelfFile)
Output : <shelve.DbfilenameShelf object at 0x000001B420037F70>
"""
shelfFile = shelve.open('mydata')
print(shelfFile['cats'])			#'cats' is a key and zophie, puka, simon are values bound to 'cats' key
shelfFile.close()
