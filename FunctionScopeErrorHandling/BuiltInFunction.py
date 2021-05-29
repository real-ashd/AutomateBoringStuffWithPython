#Built in Function
import random
import sys
i=1
while i!=5:
	i=random.randint(1,10)
	print(i)
#Prints a random integer in range from 1 to 10


#Second method for importing functions using "From"

# >>> from random import random
# >>> randint(1,10)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'randint' is not defined
# >>> from random import *
# >>> randint(1,10)
# 2
# >>> randint(1,10)
# 8
# >>> randint(1,10)
# 4
# >>>