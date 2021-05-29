import pprint

message='''"Hello, I am Ken Adams.I just came here from Italy, How you doiin."
			Hey hello there Handome.
'''
count = {}
for character in message.lower():
	count.setdefault(character,0)	#If we comment this out, we will get an error. as it will not find a key, coz count{} is empty
	count[character] += 1
pprint.pprint(count)		#To print a nicer version of count{}