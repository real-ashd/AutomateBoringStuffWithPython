#Dictionary		It is a key value pairs
#Dictionaries are mutable, they hold 'references' and not 'values'
#Unlike List items in dictionaries are unordered, there are no indexes starting from 0
#Accessing a key that does't exist will result in a key error
#Check if key exists or not using 'in' or 'not in' operator
#Dictionary methods : keys(), values(), items(), get(), setdefault(),etc [These will return list values of keys, values or both]
#Check Character counting program for setdefault() method's use and learn about pprint module

myCat = {'size':'fat', 'color':'grey', 'disposition':'loud'}		#Syntax
print(myCat)
print(myCat['size'])						#Accessing the value in dictionary
#print(myCat['loud'])
print("My cat has",myCat['color'],"fur.")	#Concatenating with other strings
spam = {12345:'Hello',42:"The Answer"}

"""
print(spam[0])
Traceback (most recent call last):
  File "F:\Python Project\Learning4\Dictionary.py", line 8, in <module>
    print(spam[0])
KeyError: 0					Because key '0' doesn't exist
"""

print("-------------------------------------------------")
print("List and DictionaryComparison")
print([1,2,3]=={3,2,1})
pet1 = {'name':'Barbie','species':'cat','age':8}
pet2 = {'age':8,'name':'Barbie','species':'cat'}
print(pet1==pet2)

print("-------------------------------------------------")
pet1 = {'name':'Barbie','species':'cat','age':8}
print("Check if key exists in dictionary using 'in' and 'not in' operator")
print('name' in pet1)
print('height' in pet1)
print('name' not in pet1)
print('height' not in pet1)

print("-------------------------------------------------")
pet3 = {'name':'Barbie','species':'dog','age':5}
print("Dictionary Methods")
print(pet3.keys())
print(pet3.values())
print(pet3.items())
print("\nDictionary methods with list function")
print(list(pet3.keys()))
print(list(pet3.values()))
print(list(pet3.items()))

print("\nDictionary methods work correctly when used with loops")
for x in pet3.keys():
	print(x)
print()
for x in pet3.values():
	print(x)
for x,y in pet3.items():
	print(str(x)+" : "+str(y))
print("\t\t\t\t\t\t\t\t\tOR")
for x in pet3.items():
	print(x)
#Checking if value exist in Dictionary
pet4 = {'name':'Barbie','species':'dog','age':5}
print('dog' in pet4.values())
print('cat' in pet4.values())
print("\nget() method")
#It accepts two args
"""
Consider this example, if a key doesn't exist it will throw an error and crash the program. To avoid this we can use
if 'color' in pet4:
	print(pet4['color'])
But we can use get() method for the same
"""
print(pet4.get('age',"Key doesn't exist"))
print(pet4.get('height',"Key doesn't exist"))

#Actual use
picnicItems = {'apples': 6,'water bottle': 3}
print("\nI am bringing "+str(picnicItems.get('oranges',0))+" oranges to the picnic.")

print("\nsetdefault() method")
pet5 = {'name':'Barbie','species':'dog','age':5}
print(pet5)
pet5.setdefault('color','black')
print(pet5)
pet5.setdefault('color','orange')	#This doesn't affect the dictionary as it already has a color value
print(pet5)