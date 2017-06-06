#inheritance is the ability for one class to inherit the properties and methods of another class

#object
#   Car

#SuperClass Car

class Car(object):

	def __init__(self, car_type, color):

		self.car_type = car_type
		self.color = color

	#method
	def drive(self):
		print("Driving my " +self.color+ " and " +self.car_type)

	def park(self):
		print("Parked Car")
		
#instead of copying the class Car(object) for each car type, use inheritance
# class Honda(object):

# 	def __init__(self, color):

# 		self.car_type = "honda"
# 		self.color = color

# 	#method
# 	def drive(self):
# 		print("Driving my " +self.color+ " and " +self.car_type)

# 	#method
# 	def park(self):
# 		print("Parked Car")

#Subclass of Car called Honda

class Honda(Car):

	def __init__(self, color):
		#super is a keyword referring to the SuperClass methods and instances variables
		super(Honda, self).__init__("Honda", color)
		#Car.__init__(self, "Honda", color) #another way

mycar = Car("Toyota","Yellow")

mycar.drive()
mycar.park()

myhonda = Honda("Green")

myhonda.drive()
print(myhonda.color)
myhonda.park()