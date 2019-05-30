player1=raw_input("Please enter the word you want other user to guess: ")
i=0
while i<len(player1):
	print "word: "+"_ "*len(player1)
	break
i=0
correctGuess=0
incorrectGuess=0
#checking for 3 chances only
while i<3:
	player2=raw_input("please enter try the word: ")
	if (player1==player2):
		correctGuess+=1
		print "you win..."
		break
	else:
		incorrectGuess+=1
		if incorrectGuess>2:
			print "you lost... all your chances gone..good bye!!!"
			break
		else:			
			print "word: "+"_ "+player1[incorrectGuess]+" "+"_ "
			print "guesses Remaining: "+str(3-incorrectGuess)