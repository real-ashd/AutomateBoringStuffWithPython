#Match Specific number of repititions
import re

#'?' when used in pattern means it can appear 0 or 1 times
batRegex = re.compile(r"Bat(wo)?man")			#the pattern (str)? can appear 1 or 0 times
												#To actually add '?' in the pattern use it with '\' as '\?'
mo = batRegex.search("The adventures of Batman")
print(mo.group())
mo1 = batRegex.search("The adventures of Batwoman")
print(mo1.group())
mo2 = batRegex.search("The adventures of Batwowowoman")
print(batRegex.search("The adventures of Batwowowoman"))
print("----------------------------------------------------------------")
#This is the pattern which will find the true Indian number
#For finding a valid number re.compile(r'(\W\d\d)?(9|8|7)\d\d\d\d\d\d\d\d\d')
phoneNumRegex = re.compile(r'(\+91)?(9|8|7)\d\d\d\d\d\d\d\d\d')			#Using '\+'' to have literal value of '+' in the pattern
#Condition 1
msg1 = "My phone number is +918881821054"
mo = phoneNumRegex.search(msg1)					#This returns None as the value was not found
if mo != None:
	print(mo.group())
else:
	print("Pattern not found")
#Condition 2
msg1 = "My phone number is 8881821054"
mo = phoneNumRegex.search(msg1)					#This returns None as the value was not found
if mo != None:
	print(mo.group())
else:
	print("Pattern not found")
print("----------------------------------------------------------------")

#'*' when used in pattern means it can appear 0 or more times
batRegex = re.compile(r"Bat(wo)*man")			#the pattern (str)? can appear 1 or 0 times
												#To actually add '?' in the pattern use it with '\' as '\?'
mo = batRegex.search("The adventures of Batman")
print(mo.group())
mo1 = batRegex.search("The adventures of Batwoman")
print(mo1.group())
mo2 = batRegex.search("The adventures of Batwowowoman")
print()
print(batRegex.search("The adventures of Batwowowoman"))
print(mo2.group())
print("----------------------------------------------------------------")
#'+' when used in pattern means it can appear 1 or more times
batRegex = re.compile(r"Bat(wo)+man")			#the pattern (str)? can appear 1 or 0 times
												#To actually add '?' in the pattern use it with '\' as '\?'
mo = batRegex.search("The adventures of Batman")
print(batRegex.search("The adventures of Batman"))
mo1 = batRegex.search("The adventures of Batwoman")
print(mo1.group())
mo2 = batRegex.search("The adventures of Batwowowoman")
print(mo2.group())
print("----------------------------------------------------------------")

regex = re.compile(r'\+\?\*')
mo = regex.search("I just learned about +?* regex syntax in this lesson")
print(mo.group())

regex = re.compile(r'(\+\?\*)+')
mo = regex.search("I just learned about +?*+?*+?*+?*+?*+?* regex syntax in this lesson")
print(mo.group())
print("----------------------------------------------------------------")

#'{n}' when used in pattern means it can appear n times
#With this we avoid repitions in pattern eg[((\+91)?(9|8|7)\d\d\d\d\d\d\d\d\d(,)?)((\+91)?(9|8|7)\d\d\d\d\d\d\d\d\d(,)?)((\+91)?(9|8|7)\d\d\d\d\d\d\d\d\d(,)?)]
haRegex = re.compile(r'(Ha){2}')							#This is case sensitive
print(haRegex.search("He said'HaHa'"))

#This will 3 find phone numbers in a row where ',' is optional and '+91' country code is optional. Also first digit of 10 digit must be 7,8 or 9
phoneNumRegex = re.compile(r'((\+91)?(9|8|7)\d\d\d\d\d\d\d\d\d(,)?){3}')
print(phoneNumRegex.search("My numbers are +919881821054,9198818210,8050607030"))

haRegex = re.compile(r'(Ha){2,7}')						
print(haRegex.search("He said'HaHaHaHaHaHaHa'"))
print(haRegex.search("He said'HaHaHaHaHaHaHaHaHa'"))		#This matches 'Ha', but only the first 7 times

haRegex = re.compile(r'(Ha){3,}')							#As in list, splicing indexes
print(haRegex.search("He said'HaHa'"))						#This doesn't match 'Ha' less than 3 times
print(haRegex.search("He said'HaHaHaHa'"))
print(haRegex.search("He said'HaHaHaHaHaHaHaHaHa'"))		#This matches 'Ha', but only the first 7 times

haRegex = re.compile(r'(Ha){,4}')							#Splicing minimum will always match none
print(haRegex.search("He said'HaHa'"))						#This doesn't match 'Ha' less than 3 times
print(haRegex.search("He said'HaHaHaHa'"))
print(haRegex.search("He said'HaHaHaHaHaHaHaHaHa'"))		#This matches 'Ha', but only the first 7 times

#Greedy Match
digitRegex = re.compile(r'(\d){3,5}')						#This matches '12345', coz by default python re do greedy matches(Longest possible  first)
print(digitRegex.search("1234567890"))

#Non-Greedy Match
digitRegex = re.compile(r'(\d){3,5}?')						#This '?' in pattern is different from ? that means 0 or 1, here it means do a non greedy match
print(digitRegex.search("1234567890"))						#Smallest posslible match i.e. "123"