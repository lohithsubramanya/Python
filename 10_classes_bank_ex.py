#### Classes  - Member Variables

# class ClassName:
# 	'this is an example class'   

# 	def __init__(self,name,age):  #### To declare and use a custom made constructor we need to define this function (def__init__())mandatorily
# 		self.name=name           ### Self is always a reference to the object. Need to declare 
# 		self.age=age

# 	def func(self): 
# 		print 'function 1'

# obj = ClassName()
# obj.func()



### bank Example

# class Bank:
# 	def __init__(self,bankBalance):
# 		self.bankBalance=bankBalance
# 		print "object created"
# 		print 'my current bank balance is :', self.bankBalance

# 	def deposit(self,amt):
# 		self.bankBalance+=amt
# 		print self.bankBalance

# 	def withdraw(self,amt):
# 		self.bankBalance-=amt
# 		print self.bankBalance

# man1 = Bank(10000)
# man1.deposit(2000)

###  Create a class VEHICLE. Vehicle can have functions such as it can move, it can refuel itself. Refueling happens based on what kind of fuel it uses. Also find the mileage based on movement.
### 2 functions  - Fuel Indicator , Type of Fuel 

### Create a class employee which will have a function to get salary and the salary calculation will be based on the experience. Also, find out how many employees are there.


#### This is over-riding example .

# class Bank:

# 	def __init__(self, bankBalance):
# 		self.bankBalance=bankBalance

# 	def deposit(self, amt):
# 		self.bankBalance += amt
# 		print self.bankBalance


# 	def withdraw(self, amt):
# 		self.bankBalance -= amt
# 		print self.bankBalance

# 	def interest(self):
# 		Int = 0.1*(self.bankBalance)
# 		self.bankBalance += Int
# 		print 'My current bank balance is :', self.bankBalance

# class hsbc(Bank):

# 	def interest(self):
# 		Int = 0.07*(self.bankBalance)
# 		self.bankBalance += Int
# 		print 'My hsbc bank balance is :', self.bankBalance


# man1= hsbc(10000)
# man1.interest()


#### Method Overloading - passing ARGUMENTS inside the function
