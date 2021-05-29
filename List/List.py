#List (or in Simple terms arrays)

""">>> spam = ['cat','dog','mouse']
>>> spam[0]
'cat'
>>> spam[1]
'dog'
>>> spam[2]
'mouse'
>>>"""

print("Accessing values in the list")
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])	
print("list1[1:3} : ",list1[1:3])#This will not include the first value and the last value which is defined, it is called as slice of a list.
#In above condition the value at index 3 is not included
print(list1[-2],list2[-1])
print("-------------------------------------------------------")

print("List inside the list can also be accessed")
sample = [[1,2,3,4,5,6,7,8,9,10], ['cat','dog','mouse','rat']]
print(sample[1])
print(sample[0])
print(sample[0][1])
print("-------------------------------------------------------")

print("Printing all the items of all list inside list")
spam = [[1,2,3,4,5,6,7,8,9,10],[10,90,30],['cat','dog','rat']]
for k in range(len(spam)):
	print("LIST",str(k+1))
	for y in range(len(spam[k])):
		print(spam[k][y])
print("-------------------------------------------------------")

print("Assigning the values to existing list")
samp = [1,2,3,4,5,6,7,8,9,10]
samp[1] = "Hello"
print(samp[1])
#Same can be done using slicing
samp[8:10] = ['cat','dog','rat']
print(samp)
print("-------------------------------------------------------")

"""
Slice Shortcuts
We can leave the first or last index blank

>>> spam = [1,2,3,4,5,6,7,8,9,10]
>>> spam[:2]
[1, 2]
>>> spam[5:]
[6, 7, 8, 9, 10]
>>> """

print("Deleting an item from the list")
list1 = ['physics', 'chemistry', 1997, 2000]
print(list1)
del list1[2]	#del = 'Un-assignment' statement
print("After deleting value at index 2 : ")
print(list1)
print("-------------------------------------------------------")

print("String and list similarities")
spam = [[1,2,3,4,5,6,7,8,9,10],[10,90,30],['cat','dog','rat']]
print(spam)
#Length of a list
print(len(spam))
print("-------------------------------------------------------")

"""Concatenation of list with "+" operator
>>> [1,2,3]+[4,5,6]
[1, 2, 3, 4, 5, 6]
>>> 

String and List replication
>>> "Hello" * 3
'HelloHelloHello'
>>> [1,2,3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
"""

print("Using list function which returns everything as a list")
print(list('Hello, How you doing'))  
print("-------------------------------------------------------")

print("Find if the item you are looking for is in the list or not using 'in' or 'not in'")
samp = [1,2,3,4,5,6,7,8,9,10]
print(samp)

#Using in operator
res = 42 in samp
res1 = 10 in samp
print("42 is present in list : ",res)
print("10 is present in list : ",res1)
#Using not in operator
res = 42 not in samp
res1 = 10 not in samp
print("42 is not present in list : ",res)
print("10 is not present in list : ",res1)

print("-------------------------------------------------------")