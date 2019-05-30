def divide_bill(billTotal,numberOfPeople):
	total=(billTotal*numberOfPeople)+(billTotal*numberOfPeople*0.1)
	print "each person should pay: "+ str(total/numberOfPeople)

divide_bill(20,5)