def eggs(sP):
	#local scope
	sP.append("Hello")	#Changes made inside the function is having effect on list outside the function
	#CHanges are made to the original values of list

#Global scope
samp = [1,2,3]
eggs(samp)	#We are only passing refences
print(samp)

#The copy.deepcopy() Function
import copy	#This module creates a copy of the list for specific situations
print("\nUsing copy module")
spam = [1,2,3,4]
cheese = copy.deepcopy(spam)
cheese[1]=42
print("Cheese :")
print(cheese)
print("\nSpam : ")
print(spam)