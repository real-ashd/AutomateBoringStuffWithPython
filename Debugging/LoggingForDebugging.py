#Logging for debugging
#Using logging module
import logging

#There are five levels of logging
# debug() -> info() -> warning() -> error() -> critical()

#This is the setup code for logging in python
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#This puts the output to a log file
# logging.basicConfig(filename='MyProgramLog.txt',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#The following statement disables all the logging statements
# logging.disable(logging.CRITICAL)		#This disables the logging at critical level or lower
# logging.disable(logging.ERROR)
# logging.disable(logging.WARNING)
# logging.disable(logging.INFO)
# logging.disable(logging.DEBUG)

logging.debug('Start of Program')
#Example : Buggy Factorial Program
def fact(n):
	logging.info('Start of factorial(%s)' %(n))
	total=1
	for i in range(n+1):		#Use range(1,n+1)
		total*=i
		logging.warning('i is %s, total is %s' %(i,total))	
		#print('i is %s, total is %s' %(i,total))
	logging.critical('Return value is %s'%(total))
	return total
print(fact(5))		#Returns 0
logging.debug('End of Program')