def safe_open(value):
	try:
		#open
		myfile=open(value,"r")
		#read
		print myfile.read()
		#close
		myfile.close()
	except IOError, e:
		print 'catching Io Exception'

safe_open("C:\Users\d14129148\Desktop\sampleData.txt")	
