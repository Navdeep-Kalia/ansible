words=['bat','ball','barn','badminton']
matcher=['ball+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++']
print cmp(words,matcher)
i=0
print words
print len(words)
while i<len(words):
	print words[i]
	i+=1
	if (i==len(words)-1):
		words[i]='beach'
		print words	