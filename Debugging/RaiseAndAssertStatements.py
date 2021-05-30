#Debugging
#Raise and Assert statement
"""
>>> 42/0
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    42/0
ZeroDivisionError: division by zero
>>> raise Exception("This is an error message.")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    raise Exception("This is an error message.")
Exception: This is an error message.
"""

"""

************
*          *
*          *
*          *
************

"""
# def boxPrint(symbol,height,width):
# 	if len(symbol)!=1:
# 		raise Exception("'Symbol' needs to be of length 1.")
# 	if width<=2 or height<=2:
# 		raise Exception("'width; and 'height' must be greater than 1.")
# 	print(symbol*width)

# 	for i in range(height-2):
# 		print(symbol+(' '*(width-2))+symbol)

# 	print(symbol*width)

# boxPrint('^',6,17)
# boxPrint('9',6,16)
# boxPrint('*(',3,3)

print('-----------------------------------\n')

#Using traceback module for getting the error in string format
#this function is used to get error in str format traceback.format_exc()
import traceback
try:
	raise Exception("This is an error message.")
except:
	errorFile=open('F:\\Python Project\\Debugging\\error_log.txt','a')
	errorFile.write(traceback.format_exc())
	errorFile.close()
	print("Please check the errorFile at 'F:\\Python Project\\Debugging\\error_log.txt'")

#Using Assertion, It is another kind of exception
#syntax 	assert condition,'error_message'
# assert False,"Fatal Error"
#Assertion errors are for programmer errors
print('-----------------------------------\n')

market_2nd = {'ns':'Green','ew':'Red'}
def switchlights(intersection):
	for key in intersection.keys():
		if intersection[key] == 'Green':
			intersection[key]="Yellow"
		elif intersection[key] == 'Yellow':
			intersection[key]="Red"
		elif intersection[key]=="Red":
			intersection[key]="Green"
	assert 'red' in intersection.values(),"Neither light is Red! "+str(intersection)

print(market_2nd)
switchlights(market_2nd)
print(market_2nd)