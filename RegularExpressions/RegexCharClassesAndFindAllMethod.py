#findall() method in python Regular Expressions
#re_object.search('str') method allows us to find the first match in 'str' whereas findall() method allows us to find all the matches and return it in list form
import re
phoneRegex = re.compile(r'\+91\d\d\d\d\d\d\d\d\d\d')
print(phoneRegex)
msg = '''This is my phone number 9881821054.
For emergencies please contact my Mom, her cell number is +919011714107'''
obj_matches = phoneRegex.findall(msg)
print(obj_matches)

#NOTE : REMEMBER IT
phoneRegex = re.compile(r'(\+91)?(\d\d\d\d\d\d\d\d\d\d)')	
print(phoneRegex.findall(msg))							#If the pattern has groups then finall() returns tuples in a list
phoneRegex = re.compile(r'((\+91)?(\d\d\d\d\d\d\d\d\d\d))')		#Returns 3 groups if we put the patter in ()
print(phoneRegex.findall(msg))


#Character class
"""
\d = (0|1|2|3|4|5|6|7|8|9)		: Any Numeric value from 0-9
\D 								: Any Non-Numeric value that is not in 0-9
\w ('w',small)					: Any Alphanumeric values i.e. 0-9,a-z,A-Z and _ character (word chars)
\W ('W',Capital)				: Any Non-Alphanumeric values i.e. not 0-9,a-z,A-Z and _ character (word chars)
\s ('s',small)					: Any space, tab or newline character. (Matching space characters)
\S ('S',Capital)				: Any character that is not space, tab or newline
"""
lyrics = """12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 gold rings, 4 calling birds, 3 french hens, 2 turtle doves and 1 partridge in a pear tree walk into a bar.
"""
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

#Create your own character classes using [] in pattern eg. r'[QWERTY]' will find if the passed string has these chars(Case Sensitive)
vowelRegex = re.compile(r'[aeiouAEIOU]')		#[a-z] means all lowercase letters
print(vowelRegex.findall(lyrics))

doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')		#{n} at the end of pattern means two vowels in a row
print(doubleVowelRegex.findall(lyrics))

#Negative Character Classes. Just add '^' in front of the chars while defining. eg: r'[^01234]'
consonantsRegex=re.compile(r'[^aeiouAEIOU]')		#Consonants+Numeric+spaces
print(consonantsRegex.findall(lyrics))