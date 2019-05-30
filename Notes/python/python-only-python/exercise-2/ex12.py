value=raw_input("please enter a string: ")
vow={'a':0,'e':0,'i':0,'o':0,'u':0}
y=0
for x in value:
	if(x in vow):
		print x
		y+=1
		vow[x]+=1
	
print y
print vow