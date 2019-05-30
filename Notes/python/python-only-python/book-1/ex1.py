#print simple string
print "hello world"

#use split function
a="compare python with java"
print a.split();

#reading file and printing it
# myfile=open("C:\Users\Navdeep\Desktop\software.txt")
# print myfile.read();

#printing some of additions multiplications etc
print(1+1); print (100-50*10); print(8/5.0); print(3**2); print(2**6);

#printing remainder and quotient
print (3%2); print(9//4);

#adding values and printing them
a=0
a+=2; print(a); 
a*=3; print(a); 
a**=2; print(a);

#checking thw value is greater or less than
print (a<10); print(a>10);

#printing answer in boolean
print(1 is 1); print(1 is not 1); print(1 is True);

#boolean and/or
a= True; b=True; c=False;
print(a and b); print (a and c); print (a and not(b or c));

#using different quotes in one variable
var ='doesn\'t'; var1="doesn't"
print var; print var1;         

#repeating same word in front of another word
print 3*'un'+'this'

#printing word from the string
word='navdeep kalia'
print word[10]; print word[7]; print word[8]; print word[-1]; print word[-7];

#multiline string
para="""this is a beautiful world
		and i am part of it
			and u r part of it"""
print para

#printing variables using the % sign
good="sun"
bad="nothing"
print "look there %s is out and %s is bad" %(good,bad)

#string %
good="g"
print "the apple is %c ood" %(good)

print repr(1.0/7.0); print str(1.0/7.0)


