print("How many cats do you have?")
numCats = input()
try :
    if int(numCats) >= 4 :
        print("That is a lot of cats")
    else:
        print("That is not many cats")
except ValueError:  #can be used without ValueError
    print("You did not enter a number.")
    
"""Output:
How many cats do you have?
siz
You did not enter a number.
>>> 
============= RESTART: F:/Python Project/Learning2/TryAndExcept2.py =============
How many cats do you have?
-4
That is not many cats
>>>



Example :
Input :
print("How many cats do you have?")
numCats = input()
if int(numCats) >= 4 :
    print("That is a lot of cats")
else:
    print("That is not many cats")

Output:
How many cats do you have?
1
That is not many cats
>>> 
============= RESTART: F:/Python Project/Learning2/TryAndExcept2.py =============
How many cats do you have?
0
That is not many cats
>>> 
============= RESTART: F:/Python Project/Learning2/TryAndExcept2.py =============
How many cats do you have?
5
That is a lot of cats
>>>
============= RESTART: F:/Python Project/Learning2/TryAndExcept2.py =============
How many cats do you have?
six
Traceback (most recent call last):
  File "F:/Python Project/Learning2/TryAndExcept2.py", line 3, in <module>
    if int(numCats) >= 4 :
ValueError: invalid literal for int() with base 10: 'six'
>>> 
"""
