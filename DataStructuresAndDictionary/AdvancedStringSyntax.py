#String Methods
#lower(), upper(), title(), isupper() or islower()
#	isalpha()			isalnum()			isdecimal()		isspace()				istitle()
#letters only		letters & nums only		numbers only	whitespaceonly		titlecase only
#startswith() and endswith()
#ljust(length,char/str), rjust(length,char/str), center(length,char/str), strip(), replace().
#pyperclip() module

sample="Hello world, how you doiin"
print(sample)
print("Using lower(), upper(), title(), isupper() and islower() respectively.")
print(sample.lower())
print(sample.upper())
print(sample.title())
sample=sample.upper()
print(sample.isupper())
sample=sample.lower()
print(sample.islower())

#If the string is blank
a = ""			#Same for integer values
print(a.isupper())
print(a.islower())
print("Hello".upper().isupper())

#isalpha()
print("\nValidation methods")
print("Hello".isalpha())
print("123".isalpha())
print()
print("Hello".isalnum())
print("123".isalnum())
print(" '".isalnum())
print()
print("Hello".isdecimal())
print("123".isdecimal())
print("1.2345".isdecimal())
print()
print("Hello".isspace())
print("Hello world"[5].isspace())
print("".isspace())
print(" ".isspace())
print()
print("Hello world".istitle())
print("Hello World".istitle())
print("1.2345".istitle())
print("------------------------------------------------\n")
sample = "Hello World!"
print(sample.startswith("H"))
print(sample.startswith("h"))		#Case Sensitive
print(sample.endswith("orld!"))
print(sample.endswith("!"))
print(sample.endswith("world!"))	#Case Sensitive
print("------------------------------------------------\n")
print("join() and split() method")
var = ', '.join(['cats','bats','hats','rats'])		#We are using join() to add "," in list items and concatenating it
print(var)
var = '\t\t'.join(['cats','bats','hats','rats'])
print(var)
var = "My name is Khan!"
print(var.split())
print(var.split('a'))
print(var.split('n'))
print("------------------------------------------------\n")
print("ljust(), rjust(), center(), strip(), replace() methods")
var = "Hello"
var1 = var.rjust(13)		#var.rjust() just returns a new string and doesn't change original string
print(var1)
print(len(var1))
var2 = var.ljust(10)
print(var2)
print(len(var2))
var2 = var.ljust(14,'#')
print(var2)
var1 = var.rjust(12,"*")
print(var1)
var3 = var.center(52,"-")
print(var3)
print()
var4 = "         Hello"
var5 = "          Hey there              "
print(var4.strip())
print(var5.strip())
print("SampSampSampSampEggsSampBaconSampSampSamp".strip('apmS'))
print()
var = "Hello there"
print(var.replace('e','ABC'))
print("------------------------------------------------\n")
# print("pyperclip module")
import pyperclip
#pyperclip has two methods pyperclip.copy() and pyperclip.paste()
pyperclip.copy("Hello!!!!!!!!!!!!!!!!!!!")
