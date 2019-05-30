x=raw_input("Input first string: ")
y=raw_input("Input second string ")

if(len(x)==len(y)):
	print "Strings are of equal lengths"
	if(x==y):
		print "same content strings"
	else:
		print "content is not same"
		
else:
	print "Strings are not of equal length"
	