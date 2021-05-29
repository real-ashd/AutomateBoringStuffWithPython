#Regular Functions

# A non-regular expression in India, +919875755689
def isPhoneNumber(text):	# +919875755689
	if len(text) == 10 or len(text) == 13:		#Check if length is 10 or 13(Including country code)
		if len(text) == 10:
			for i in range(0,9):
				if not text[i].isdecimal():		#Check if all chars are number
					return False
				if not text.startswith('9') or text.startswith('8') or text.startswith('7'):
					return False
		else:
			if not text.startswith("+919") or text.startswith("+918") or text.startswith("+917"):
				return False
		return True
	else:
		return False

print("1st Situation",isPhoneNumber("+919881821054"))
print("2nd Situation",isPhoneNumber("9881821054"))
print("3rd Situation",isPhoneNumber("+918881821054"))
print("4th Situation",isPhoneNumber("0881821054"))
print("5th Situation",isPhoneNumber("+91988182105A"))
print("6th Situation",isPhoneNumber("988182105H"))
print("7th Situation",isPhoneNumber("+9198818210547"))
print("8th Situation",isPhoneNumber("98818210547"))

message = "Call me at my number +919881821954"
foundNumber = False

for i in range(len(message)):
	chunk1 = message[i:i+10]
	if isPhoneNumber(chunk1):
		print("Phone Number found :",chunk1)
		foundNumber = True
if not foundNumber:
	print("Phone Number not found.")

print("----------------------------------------------------------------------")

#Regular Expression performs same function as above in less line of code
import re
msg = "Call me at my number 9881821954 or 7898577869"
phoneNumRegex = re.compile(r"\d\d\d\d\d\d\d\d\d\d")		#We often use \ backslashes so they are often raw strings: r'\d'
match_object = phoneNumRegex.search(msg)				#This search method finds 1st occurance
print(match_object.group())

print(phoneNumRegex.findall(msg))						#This findall method finds all occurance in a list


#Call the re.compile("pattern") function to create a regex object.
#Call the method search() to create a match object
#Call the method group() to get the matched string
#Call the method findall() to find all occurances in the string