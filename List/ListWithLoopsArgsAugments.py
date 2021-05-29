#List part 2
print("Range Function")
print(range(4))
print("---------------------------------------------")

print("Using range function to generate a list")
sample = list(range(0,100,5))	#range(initial_index, last_index, difference[optional])
samp = list(range(1,35,3))
print(sample)
print(samp)
print("---------------------------------------------")

print("Simple List to list all the numbers in the list using for loop")
sample =[1,2,3,4,5,6,7,8,9,10]
for i in range(len(sample)):
    print(sample[i],"\tIndex :\t",str(i))	#We can access the list with index numbers starting from 0-....
#We can use i for index as well as for printing value of item in the list
print("-------------------------------------------------------")

print("Another way of listing items using for loop")
for x in sample:
	#if x%2==0:		This will print only even numbers
		print(x)
print("-------------------------------------------------------")

print("Assigning values normally")
cat = ['fat','orange','loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
print(size,color,disposition) 
print("\nAssigning values with list")
cat = ['fat','orange','loud']
s, c, d=cat		#Assigning values in one line
print(s,c,d)

print("\nAnother Example for assigning values")
size, color, disposition = 'Skinny', 'White', 'Queit'
print(size,color,disposition) 
a='ABC'
b='BCD'
print("Before Changing : ",a,b)
a,b = b,a	#Interchaging the values (SWAP)
print("After Changing : ",a,b)
print("-------------------------------------------------------")

"""
Input : 
spam = 42
spam = spam + 1
#We can use +=, -=, *=, /= and %=
spam = 42
spam+=1
print(spam)
spam-=1
print(spam)
spam*=2
print(spam)
spam/=2
print(spam)
spam%=5
print(spam)

Output:
43
42
84
42.0
2.0
"""
