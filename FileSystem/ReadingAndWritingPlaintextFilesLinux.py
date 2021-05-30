#Reading and Writing Plaintext (.txt) files
#All other file types such as .doc,.ppt,.pdf are binary files

#open(), read() and close() methods 
#readlines()
# import os
# print(os.getcwd())
#Shelve Module
"""
The shelve module can be used as a simple persistent storage option for Python objects when a relational database is overkill.
The shelf is accessed by keys, just as with a dictionary.
The values are pickled and written to a database created and managed by anydbm.
The objects created are stored in the form of binary files
"""
import shelve
shelfFile = shelve.open('mydata')							#Use this code only once
#you can treat shelfFile variable as a dictionary			#Use this code only once
shelfFile['cats'] = ['zophie','puka','simon','fat-tail']	#Use this code only once
shelfFile.close()											#Use this code only once
"""
The above code will create 3 files in current working directory if os is windows, files are mydata.bak, mydata.dat and mydata.dir
and only one file if the os is linux based i.e. mydb

print(shelfFile)
Output : <shelve.DbfilenameShelf object at 0x000001B420037F70>
"""
shelfFile = shelve.open('mydata')
print(shelfFile['cats'])			#'cats' is a key and zophie, puka, simon are values bound to 'cats' key
shelfFile.close()