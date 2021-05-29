#While statement with continue
spam =0
while spam<5:
	spam=spam+1;
	if spam==3:
		continue
	print("spam is "+str(spam))

# Output:
# spam is 1
# spam is 2
# spam is 4
# spam is 5

#3 is missing Continue jumps to while again and rechecks the condition without
#executing the rest