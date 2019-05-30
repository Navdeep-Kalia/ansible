#creating list with numbers or characters
numbers=[1,2,3,4,5]
char=['a','b','c','d']

#printing specified digit or character out of list
print numbers[0]; print numbers[3]; print char[0]; print numbers[-3:]

#putting two lists in one
c=[numbers,char]; print c;

#replacing number from list and deleting it
numbers[1]=200; print numbers; 
del numbers[0]; print numbers;

#list comprehension
new_list=[x for x in range(1,6)]; print new_list;

#list multiplication
new_list=[i ** 2 for i in range(1,10)]; print new_list;

#printing value starting after 5 and adding 2 into it and less than 11
print new_list[5:11:2]

#printing string length
print len([1,2,3])

#concatenating list
a=[1,2,3]+[4,5,6]; print a;
b=[4,4,3]+[1,2,3]; print b;

#check membership
print 3 in [1,2,3]; 
#repetition
print ["hi"]*4;
#iteration
for x in [1,2,3]: print x;

list1=[2,4,60];list=[1,2,2,2,3,4]; list.append(5); print list; print list.count(2);
print min(list);print len(list); print max(list); print cmp(list,list1);




