grades=[9,7,7,10,3,9,6,6,2]
x=0
for y in grades:
	if(y==7):
		x+=1
print x
print grades


grades[len(grades)-1]=4
print grades

print max(grades)
print sorted(grades)
print sum(grades)/len(grades)