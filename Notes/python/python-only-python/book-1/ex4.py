num=20
if num==10:
	print num
else:
	pass
	#print num

name="navi"
it=iter(name)
print it.next();print it.next();print it.next();

def func1():
	print "hello world to all"

x=0
while x <5:
	func1()
	x+=1

def area(width,height):
	area=width*height
	print area

area(12,10)

def square(n):
	return n*n*n
	
print square(10)

def func1(n):
	return n*2

def func2():
	return func1(10)*10

print func2()

def printInfo(name, age,*subject):
	print "name: ", name;
	print "age: ", age;
	for s in subject:
		print s
	return;

printInfo("navi",12,"python","java","math"); printInfo("bob",32); printInfo("martin",35);
