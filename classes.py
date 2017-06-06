#williamfiset 33 Classes [1_11] introduction, 34 [2_11] self init, 35 [3_11] class variables, 39 Encapsulation, 40 Inheritance, 41 Interfaces Abstract Methods

#oop Object Orientated Programming.  A class is a template or a blueprint, a receipe which defines the object.  A class is like a mother which has the characteristics of her children.  The children is the instances of the mother class.
#Classes begin with an uppercase letter.
#Each class has a unique hexadecimal number which is the address in memory.  Can call a class more than once with each called calss its own unique hexadecimal number.  Call a class by setting the class equal to a variable; for example, myboat = Boat(), myboat2 = Boat().

class Boat():
	pass

my_boat = Boat()
print(my_boat) #print an unique hexadecimal number
my_boat2 = Boat()
print(my_boat2) #print an unique hexadecimal number
# my_boat2 = my_boat
# if my_boat is my_boat2:
# 	print("They point to the same address in memory")
# if my_boat == my_boat2:
# 	print("They point to the same address in memory")
print(id(my_boat)) #print the integer representation of the class unique hexadecimal number
print(id(my_boat2)) #print the integer representation of the class unique hexadecimal number

x = 56
def change_value(num):
	num = 90
print(x) #print 56
change_value(x)
print(x) #print 56

class Boat():
	def __init__(self):
		self.cargo_weight = 23
def change_cargo_weight(ship):
	ship.cargo_weight = 45
boat = Boat()
print(boat.cargo_weight) #print 23
change_cargo_weight(boat)
print(boat.cargo_weight) #print 45
print("\n")

#__init__.  Give an object, in this case class, instances variables when created.
#self.  Self represents the object itself.  The object itself is the variable assigned to.  In the first example, "self" is assiged the variable "will":  will's name is "William" and will's gender is "Male".  Self much be the first in the parenthesis __init__().
# class Human():
# 	def __init__(will, name, gender):
# 		will.name = name
# 		will.gender = gender
# 	def speak_name(will):
# 		print("My name is %s" % will.name)
#		print("My name is " +will.name)
# will = Human("William","Male")
# print(will.name) #print William
# print(will.gender) #print Male
# will.speak_name() #return My name is William

class Human():
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender
	def speak_name(self):
		print("My name is %s" % self.name)
		print("My name is " +self.name)
	def speak(self, text):		
		print(text)
	def perform_math_task(self, math_operation, *args):
		print(self.name+ " performed a math_operation and the result was" ,math_operation(*args))
will = Human("William","Male")
print(will.name) #print William
print(will.gender) #print Male
will.speak_name() #return My name is William
will.speak("I love Python programming!") #return I love Python programming!
raymondisself = Human("raymondname","raymondgender")
print(raymondisself.name) #print raymondname
print(raymondisself.gender) #print raymondgender
raymondisself.speak_name() #return My name is raymondname
raymondisself.speak("speaktext") #return speaktext
def add(a, b):
	return(a + b)
def subtract(a, b):
	return(a - b)
ryan = Human("Ryan Stevens","Male")
ryan.perform_math_task(add,34, 67) #return Ryan Stevens performed a math operation and the result was 101
ryan.perform_math_task(subtract,34, 67) #return Ryan Stevens performed a math operation and the result was -33
print("\n")

#car class - number of wheels on the car.  Class or static variable.  All cars have four wheels.
#house class - house address.  Instance variable.
#house class - purchase price.  Instance variable.
#character class - maximum health.  Class or static variable.
#grid class - width and height of grid.  Instance variable.
#polygon class - the number of vertices  Instance variable.
#triangle class - right triangle, scalene, equalaterial  Class or static variable.
#math class - golden ratio constant.  Class or static variable.
#class name must be before the class variable; e.g. Character.max_health.  Classname.classvariable

class Character():
	total_number_of_characters = 0  #class variable
	max_health = 100 #class variable
	def __init__(self, name):
		self.name = name #instance variable
		self.health = Character.max_health #instance variable
		Character.total_number_of_characters +=1
bob = Character("Bob")
ryan = Character("Ryan Stevens")
print(Character.total_number_of_characters) #print 2
print(Character.max_health) #print 100
print(bob.name) #print Bob
print(ryan.name) #print Ryan Stevens
print("\n")

#Encapsulation is the art of data hiding

class ClassName():
	def __init__(self):
		self._privateVar = "Private"
		self.publicVar = "Public"
	def _privateMethod(self):
		pass
	def _privateMethod2(self):
		pass
	def publicMethod(self):
		return self._privateMethod2() + self._privateMethod()
	def publicMethod2(self):
		return 5
c = ClassName()
c2 = ClassName()
print(c._privateMethod()) #print None
print(c2.publicMethod2()) #print 5
print(c._privateVar) #print Private
print(c.publicVar) #print Public
print("\n")

#inheritance is the ability for one class to inherit the properties and methods of another class

#SuperClass Car
class Car(object):
	def __init__(self, car_type, color):
		self.car_type = car_type
		self.color = color
	def drive(self):
		print("Driving my %s %s" % (self.color, self.car_type))
	def park(self):
		print("Parked car")
mycar = Car("Toyota","Yellow")
mycar.drive() #return Driving my Yellow Toyota
mycar.park() #return Parked car

#inheritance.  No need to copy Car class and replace Car with Honda.  Let's have one class for both.  Uses same methods drive(self) and park(self).  Allows to take everything in SuperClass Car and apply to a subclass.
# class Honda(object):
# 	def __init__(self, color):
# 		self.car_type = "Honda"
# 		self.color = color
# 	def drive(self):
# 		print("Driving my %s %s" % (self.color, self.car_type))
# 	def park(self):
# 		print("Parked car")
# mycar = Car("Toyota","Yellow")

#Here is the subclass called Honda
class Honda(Car): #I believe the SuperClass Car is referenced here
	def __init__(self, color):
		super(Honda, self).__init__("Honda", color) #call __init__ method from class Car.  super is a keyword referring to the SuperClass methods and instances variables.  In this case, SuperClass is Car.  Car is referenced at the class Honda(Car).
		#Car.__init__(self, "Honda", color) #another way which is better says instructor
myhonda = Honda("Green")
myhonda.drive() #return Driving my Green Honda.  Use drive() method from SuperClass Car
print(myhonda.color) #print Green
print("\n")

#interface is a template which tells the class how to behave.  What properties and methods it must have.
#abstract method is related to interface.  It's a method which must be overriden.  The interface is the structure.
#interface and abstract methods works in python2.7.  nothing happened in python3.5.

from abc import ABCMeta, abstractmethod #Abstract Base Class instructor believes

class Shape(object): #interface
	__metaclass__ = ABCMeta
	@abstractmethod
	def area(self): #abstract method
		pass
	@abstractmethod
	def perimeter(self): #abstract method
		pass
#If I ran the class with the lines s = Shape() and print s.area(), then Python crashes.  Error is Can't instantiate abstract class Shape with abstract methods area, perimeter.  Instructor says Shape is an interface.  Can't create an instance.  Can only have it as a super class.
# s = Shape()
# print s.area()
class Rectange(Shape):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		super(Rectange, self).__init__()
	def area(self):
		return self.width * self.height
	def perimeter(self):
		return (self.width) * 2 + (self.height * 2)
rect = Rectange(5, 6)
print(rect.area())  #print 30
print(rect.perimeter())  #print 22
'''
hierarchy:
object
	Shape
		Rectangle
			Square
'''
class Square(Rectange):
	def __init__(self, side_length):
		self.side_length = side_length
		super(Square,self).__init__(side_length, side_length)
	#Override Rectangle(Shape) area method
	def area(self):
		print("Using Square area method")
		return self.side_length * self.side_length
s = Square(5)
print(s.area())  #print 25
print(s.perimeter())  #print 20
print("\n")

