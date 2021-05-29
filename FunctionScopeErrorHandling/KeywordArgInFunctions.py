#Keyword args in Functions but they are optional

#print() adds a line at the end every time it ends
print("Hello")
print("World")

#We can avoid above situation by adding a keyword argument
print("Hello", end="")
print("World")

#print() adds a single space between them when you pass multiple args
print('cat','dog','mouse')

#we can use sep argument to change the value of separation to our choice
print('cat','dog','mouse',sep="ABC")

"""
Output :
Hello
World
HelloWorld
cat dog mouse
catABCdogABCmouse

"""
