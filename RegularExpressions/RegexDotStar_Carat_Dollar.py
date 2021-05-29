#Check the second argument of re.compile() function re.DOTALL "prints all the matched pattern including new lines"
#re.compile(r'pattern',re.I) or re.compile(r'pattern',re.IGNORECASE) "This ignores the case sensitive nature of the pattern"
import re

#'^' can be used to find if the string passed starts with the pattern
beginsWithHelloRegex=re.compile(r'^Hello')	
print(beginsWithHelloRegex.search("Hello There!"))
print(beginsWithHelloRegex.search("He said 'Hello!'"))

#endWith using $
beginsWithHelloRegex=re.compile(r'There!$')	
print(beginsWithHelloRegex.search("Hello there!"))
print(beginsWithHelloRegex.search("Hello There!"))

#Using both '^' and '$' to indicate startswith and endswith
#Both means the entire string must match
allDigitsRegex=re.compile(r'^\d+$')
print(allDigitsRegex.search("1245746757657"))
print(allDigitsRegex.search("12457467 57657"))

#Using Dot character. '.' it means any character except a new line
atRegex=re.compile(r'.at')
print(atRegex.findall("The cata in the hata sate on the flato matr.h\nat "))
atRegex=re.compile(r'at.')
print(atRegex.findall("The cata in the hata sate on the flato matr.hat\n"))
atRegex=re.compile(r'.at.')
print(atRegex.findall("The cata in the hata sate on the flato matr.\nhat\n"))
atRegex=re.compile(r'.{1,2}at')													#It adds spaces
print(atRegex.findall("The cat in the hat sat on the flat mat."))
print("------------------------------------------------------------------------")
#Using Dot-Star pattern to avoid spaces '.' means any character and '*' means 1 or more
#'(.*)' uses greedy mode to use non greedy mode use '(.*?)'
string="First Name : Ash Last Name : Deshmukh"
nameRegex=re.compile(r'First Name : (.*) Last Name : (.*)') #Greedy expresion
print(nameRegex.findall(string))

serve = '<To serve humans> for dinner.>'
nonGreedyRegex=re.compile(r'<(.*?)>')		#NonGreedy Version
print(nonGreedyRegex.findall(serve))

greedyRegex=re.compile(r'<(.*)>')			#Greedy version
print(greedyRegex.findall(serve))

prime = "Serve the public.\nProtect the innocent.\nUphold the Laws."
print(prime)
dotStar=re.compile(r'.*')				#Greedy version
print(dotStar.search(prime))

dotStar=re.compile(r'.*',re.DOTALL)
print(dotStar.search(prime))

vowelRegex=re.compile(r'[aeiou]')			#Returns only lowercase vowels
print(vowelRegex.findall("Al, why does your programming book talk about RoboCop so much."))

vowelRegex=re.compile(r'[aeiou]',re.IGNORECASE)			#Ignores the case senstiveness
print(vowelRegex.findall("Al, why does your programming book talk about RoboCop so much."))

vowelRegex=re.compile(r'[aeiou]',re.I)			#Ignores the case senstiveness
print(vowelRegex.findall("Al, why does your programming book talk about RoboCop so much."))
