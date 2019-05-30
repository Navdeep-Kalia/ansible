class Hourlyemployee:
	
	def __init__(self,hourly_rate,number_of_hours):
		self.hourly_rate=hourly_rate
		self.number_of_hours=number_of_hours
	def employee_pay(self):
		return self.hourly_rate*self.number_of_hours
		
e1 = Hourlyemployee(10,20);
print e1.employee_pay();