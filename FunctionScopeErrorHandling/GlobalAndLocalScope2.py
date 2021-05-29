def spam():
    #global eggs (Add this to make eggs a global variable
    eggs= 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()

"""
Output:
    99
"""
