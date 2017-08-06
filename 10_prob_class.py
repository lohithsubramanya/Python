### Create a class employee which will have a function to get salary and the salary calculation will be based on the experience. Also, find out how many employees are there.

# class Employee:
# 	empcount = 0

# 	def __init__(self,name,experience):
# 		self.name = name
# 		self.experience = experience
# 		Employee.empcount += 1

# 	def getSal(self):
# 		if self.experience <= 2:
# 			salary = 50000
# 		elif self.experience > 2 and self.experience < 5:
# 			salary = 70000
# 		elif self.experience > 5 and self.experience < 10:
# 			salary = 100000
# 		elif self.experience > 10:
# 			salary = 200000
# 		print "The salary of",self.name,'per month is INR',salary

	# def count(self):
	# 	print "Total employees %d" %Employee.empcount


# emp1 = Employee("abc",17)
# emp2 = Employee("xyz",8)
# emp3 = Employee("zak",1)

# emp1.getSal()
# emp2.getSal()
# emp3.getSal()
# print "Total Employee count is %d" % Employee.empcount





###  Create a class VEHICLE. Vehicle can have functions such as it can move, it can refuel itself. Refueling happens based on what kind of fuel it uses. Also find the mileage based on movement.
### 2 functions  - Fuel Indicator , Type of Fuel 

# class vehicle:

# 	def __init__(self,name,fuel):
# 		self.name = name
# 		self.fuel = fuel

# 	def fuel_ind(self,distance):
# 		if distance <= 100:
# 			print "3/4th tank of",self.fuel,"available for",self.name
# 		elif distance > 100 and distance <= 200 :
# 			print "Half tank",self.fuel,"available for",self.name
# 		elif distance > 200 and distance <= 300 :
# 			print "1/4th tank of",self.fuel,"available for",self.name
# 		elif distance > 300 and distance <= 400 :
# 			print self.fuel,"refill required for",self.name
# 		else:
# 			print "Fill whatever you get, else walk up to your place"

# ride1 = vehicle("INNOVA","DIESEL")
# ride2 = vehicle("SWIFT","PETROL")

# ride1.fuel_ind(320)
# ride2.fuel_ind(450)