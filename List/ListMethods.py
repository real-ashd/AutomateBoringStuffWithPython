#List Methods, we only call the method itself and do not assign them
#index('item_value'), append('item_value'), insert(index_number,'item_value'), remove('item_value'), sort() or sort(reverse=True) or sort(key=str.lower)
#As these method returns None value after execution
#These methods do not work with string or integer data types but only on list datatype
print("List Methods")
#Syntax for index method : listname.index('value/item')
list1 = ['A','B','C','D']
print(list1)
print(list1.index('C'))
#prints : 2 
print("--------------------------------------------")

print('In case of duplication, index method returns the index of first value it finds')
list2 = ['A','B','C','D','S','B']
print(list2)
print(list2.index('B'))
#prints : 1

print("--------------------------------------------")
print("append() and insert() methods\n")
print("Using Append method we can add items only at the end of the list")
list3 = ['A','B','C','D','E']
print(list3)
list3.append('F')
print("After appending 'F':")
print(list3)
print("\nUsing insert method we can add item at the desired index value as this method only accepts 2 args")
list3.insert(3,"G")
print(list3)
print("--------------------------------------------")

var1 = list3.append('cat') #will only return none value
print(var1)
print("--------------------------------------------")

print("Using remove() method")
#del statement allows you to delete the value at the index of the list, but remove method allows you to remove a specific value in the list
list4 = ['cat','hat','rat','bat']
print(list4)
list4.remove('rat')	#If we try to remove the item if it is not present in the list it returns an error


#list4.remove('elephant')
#Output:
#Traceback (most recent call last):
#  File "F:/Python Project/Learning3/ListMethods.py", line 40, in <module>
#    list4.remove('elephant')
#ValueError: list.remove(x): x not in list
#

print("\nAfter removing 'rat'")
print(list4)
list4 = ['cat','hat','rat','bat', 'hat']
print("\nIn case of duplicate value it only removes the first value it finds")
print(list4)
list4.remove('hat')
print("\nAfter removing 'hat'")
print(list4)
print("--------------------------------------------")

print("Using sort() method, [It uses ASCII-betical order meaning uppercase alphabets come before lowecase] :\nUnsorted lists")
list5 = [8,6,4,9,0,3,4,7,1, -3,6.2,5.3]
list6 = ['bat','Rat','elephant','cat','hat']
#Does not work if data types are different like mix of strings and integers

print(list5)
print(list6)
print("\nLists after using sort()")
list5.sort()
list6.sort()
print(list5)
print(list6)
print("\nLists in reverse order")
list5.sort(reverse=True)
list6.sort(reverse=True)
print(list5)
print(list6)
print("\nTo sort in truely alphabetical order use sort method argument 'list_name.sort(key=str.lower)")
list6 = ['bat','Rat','elephant','cat','hat']
print(list6)
print("After sorting")
list6.sort(key=str.lower)
print(list6)
print("--------------------------------------------")