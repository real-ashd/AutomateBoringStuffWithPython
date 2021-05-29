#Global and Local Scope

#We have Global and Local Scope to isolate the area of bug
#If a variable has bad value in all the program check for global scope
#If only one or two var have bad value check for local scope

#1. Local variable can't be used in global Scope
#2. Code in a global scope can't use any local variable
#3. Code in local scope can access global variable
#4. Code in one function's local scope can't use variables in another local scope

n = 40      #Global Variable (created when the program starts and destroyed when the program ends)

def eggs():
    n = 42      #Local Variable -temporary (created when the function is called within that scope and when the function returns these variables are destroyed)
    print("Local var"+str(n))

print("Some code here")
print("Some more code")
print("Global var : "+str(n))
eggs()

"""Output:
Some code here
Some more code
Global var : 40
Local var42"""

"""eg:
def samp():
    eggs=99
spam()
print(eggs)

"""
