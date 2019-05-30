def myBMI(height,weight):
	BMI= weight*703/height**2
	if BMI<18.5:
		print "Underweight"
	elif 18.5<=BMI <25:
		print "Normal"
	else:
		print "	OverWeight"

myBMI(100,20)