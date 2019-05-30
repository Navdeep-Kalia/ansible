def f(x):
	return x % 2 !=0 and x % 3 !=0

print f(20)

print filter(f, range(2,25))

def cube(x):
	return x*x*x

print cube(3); print map(cube, range(1,11));
tup=1,2,3,'hello'; print tup[0]; print tup[2]; print len(tup); print min(tup);

d={'a':1,'b':2,'c':3}; print d;print d.items(); print d.keys(); print d.values();
for key in d:
	print key, d[key]

del d['a']; print d; print len(d); print str(d); 
print d.copy();print d.keys();print d.items();d.clear(); print d;

x=20
if x<0:
	print "negative value"
elif x==0:
	print "value is zero"
elif x==11:	
	print "value is 11"
else:
	print "dont know"
	
print range(1,10); print range(5,10); print range(0,10,4); print range(-10,-100,-30);

num=1;
while num<10:
	print num*2
	num+=1
	
for i in range(3):
	print i

num=[10,20,30,40]
for i in num:
	print i
	break

count=0
while True:
	print count
	count+=1 
	if count>=5:
		break

for num in range(2,20):
	if num%2==0:
		print num
		
