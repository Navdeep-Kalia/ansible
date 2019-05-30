loginid=raw_input("please enter the login id: ")
users=['alice','bob','john','peter']
i=0
while i < len(users):
	if loginid==users[i]:
		print "Login:" + users[i] + "- you have successfully logged in"
		break
	else:
		print "login failed - sorry, unknown user."
	i+=1
	