#We know search(), findall() and group()
#This program will let us know about the find and replace application of Regular Expression
import re

#Using sub() method : Substitution 
msg="Agent Alice gave the secret document to Agent Bob"
nameRegex=re.compile(r'Agent \w+')
print(nameRegex.findall(msg))
print(nameRegex.sub('REDACTED',msg))

#Changing the name to their first letter of their name
nameRegex=re.compile(r'Agent (\w)\w+')			#Returns only first letter of the name.
print(nameRegex.findall(msg))
print(nameRegex.sub(r'Agent \1***',msg))		#\1 means 1st group in regex

#Verbose Regular Expression string
#Verbose Format example
#(\W\d\d)?(9|8|7)\d\d\d\d\d\d\d\d\d'
phoneNumRegex = re.compile(r'''
	(\W\d\d)?					#Country code
	(9|8|7)						#First digit should be 7,8 or 9	
	\d\d\d\d\d\d\d\d\d\d		#Unique Phone Number
	''',re.VERBOSE | re.DOTALL | re.I)
mo=phoneNumRegex.search("+91881821965")
print(mo.group())

# #Using BitWise or operator | in second arg of compile eg :
# phoneNumRegex = re.compile(r'(+91)(\d\d\d\d\d\d\d\d\d\d)',re.DOTALL | re.I | re.VERBOSE)

