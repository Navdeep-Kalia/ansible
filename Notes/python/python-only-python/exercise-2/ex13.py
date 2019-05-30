name='albert einstein'
new_name='bertie'
result=''
for x in new_name:
	for y in name:
		if y==x:
			result=result+y
			break
print result