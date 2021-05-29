#Escape Characters
"""print('This is Alice's cat)
  File "F:\Python Project\Learning4\StringSyntax.py", line 2
    print('This is Alice's cat)
                         ^
SyntaxError: invalid syntax
Escape Characters			Print as
\'							Single Quote
\"							Double Quote
\t 							Tab
\n 							NewLine (Line Break)
\\ 							Backslash
"""
print('This is Alice\'s cat.')
print("\n---------------------------\nHello There\nHow are you?\nI am fine\n")
#Raw string
print("Hey there,\' How you doiin?")
print(r"Hey there,\' How you doiin?")	#Prints as it is
print("\nTriple quote defining.")
pr = """Hey there sjfjgkjdfklglkdjfklgjkldfjgkljgklgjkjdfgklfkgklfjgkljdfgjlkdfjgkldfjgkljlk;fdgj;dkjg;lkdjgl;kdjf;gjdfljgl;dkfj
ehjhrejhruerdjhfjkchkjhdsfhjksdhvjjfjsdhf
dfhsdkhfsdhfjdfhshfjhfkjhkjhfdjfaklhfhj"""
print(len(pr))

#Strings uses indices and splices similar to lists
a="Hello World!"
print(a[0])
print(a[1:7])
print(a[-1])
print("Hello" in a)			#Using in operator on string
print('x' in a)
print("------------------------------------------------------------\n")
print(r"Using %value to format the string")
name ="Ash"
place="Eden Garden"
time="7pm"
food="Burgers"
print("Hello "+name+", you are invited to the party at "+place+" at "+time+". Please do bring "+food+".")
print("Same string using string format '%'")
print("Hello %s, you are invited to the party at %s at %s. Please do bring %s."%(name,place,time,food))