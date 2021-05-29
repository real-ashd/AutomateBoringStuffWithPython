#List value is mutable datatype, it can have value added removed or changed
#However String is immutable data type, its value can't be changed



"""
>>> list["Hello"]
list['Hello']
>>> list("Hello")
['H', 'e', 'l', 'l', 'o']
>>> name='Sophie'
>>> name[0]
'S'
>>> name[1:3]
'op'
>>> name[-2]
'i'
>>> 'So' in name
True
>>> 'Abs' in name
False
>>> for letter in name:
	print(letter)

S
o
p
h
i
e
>>> name='Sophie the cat'
>>> name[7]
't'
>>> name[7]='X'
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    name[7]='X'
TypeError: 'str' object does not support item assignment
>>>
"""

#To Modify a string create a new variable and use splicing
"""
>>> name="Sophie a cat"
>>> newName=name[0:7]+"the"+name[8:]
>>> newName
'Sophie the cat'
>>> 
"""

#List uses reference while strings do not
"""
>>> s=42
>>> c=s
>>> s=100
>>> s
100
>>> c
42
>>> 
>>> 
>>> 
>>> s=[1,2,3,4,5,6]
>>> c=s
>>> c[4]="Hello"
>>> c
[1, 2, 3, 4, 'Hello', 6]
>>> s
[1, 2, 3, 4, 'Hello', 6]
>>>
"""