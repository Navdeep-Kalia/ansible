first= raw_input("please enter the first string: ")
second=raw_input("please enter the second string: ")

if(len(first)==len(second)):
	print "The string are of same length"
	if(first==second):
		print "The string have same content"
else:
	print "The strings are not of same length"

x=first.lower()
y=second.upper()
print x;
print y;