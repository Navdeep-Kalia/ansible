def even(n):
	for x in range(0,n+2):
		if(x%2==0) & (x<9):
			print x
even(10)

def decend(n):
	for x in range(0,n+1):
			if(x<10):
				print n-x
decend(10)