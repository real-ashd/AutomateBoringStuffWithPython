import pyperclip
import re
#To Dos
#1 Create a regex for phone numbers
phoneRegex=re.compile(r'''(
	#415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
((\d\d\d)|(\(\d\d\d\)))?	#area code
(\s|-)						#first separator space or -
\d\d\d						#first 3 digits
-							#second separator
\d\d\d\d					#last four digits
)''',re.VERBOSE)

#2 Create a regex for email ids
emailRegex=re.compile(r'''
	#real_ashd@protonmail.com

[a-zA-Z0-9_.+]+	#name part
@	#@ symbol
[a-zA-Z0-9_.+]+	#domain name part

''', re.VERBOSE)

#3 Get the text off the clipboard
text=pyperclip.paste()

#4 Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers=[]
for phoneNumber in extractedPhone:
	allPhoneNumbers.append(phoneNumber[0])

# print(allPhoneNumbers,len(allPhoneNumbers))
# print(extractedEmail,len(extractedEmail))
#5 Copy the extracted email/phone to the clipboard

results='\n'.join(allPhoneNumbers)+'\n\n'+'\n'.join(extractedEmail)
pyperclip.copy(results)