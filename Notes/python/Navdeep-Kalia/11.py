class employee:
	
	def __init__(self,name):
		self.name=name
	def get_name(self):
		return self.name
		
e1 = employee("navi");
print e1.get_name();