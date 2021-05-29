import re

#Condition 1
phoneNumRegex = re.compile(r'(\W\d\d)(\d\d\d\d\d\d\d\d\d\d)')		#\d is for numeric value and \W is for non alpha numeric values
mo = phoneNumRegex.search("My phone number is +919881821054")
print(mo.group())		#Prints the first occurance of matched string
print(mo.group(1))		#Prints the country code which was enclosed in "()" while creating phoneNumRegex object
print(mo.group(2))		#Prints the Phone Number of 10 digit

#Condition 2
phoneNumRegex = re.compile(r'\(\W\d\d\)(\d\d\d\d\d\d\d\d\d\d)')		#Use \( as escape char to look for literal paranthesis
mo = phoneNumRegex.search("My phone number is (+91)9881821054")
print(mo.group())
print(mo.group(1))
print("---------------------------------------------------------------------")

#Using Pipe "|" character in regex
batRegex = re.compile(r'Bat(man|mobile|copter|arang)')
mo = batRegex.search("Batarang is a boomarang which comes back after throwing.")
print(mo.group())

phoneNumRegex = re.compile(r'(\W\d\d)(9|8|7)\d\d\d\d\d\d\d\d\d')
#Number is invalid
msg1 = "My phone number is +916881821054"
mo = phoneNumRegex.search(msg1)					#This returns None as the value was not found
if mo != None:
	print(mo.group())
else:
	print("Pattern not found")
#Number is valid
msg2 = "My phone number is +918881821054"
mo = phoneNumRegex.search(msg2)
if mo != None:
	print(mo.group())
	print(mo.group(1))
else:
	print("Pattern not found")