#interface is a template which tells the class how to behave.  What properties and methods it must have.
#abstract method is related to interface.  It's a method which must be overriden.  The interface is the structure.
#interface and abstract methods works in python2.7.  nothing happened in python3.5.

#abc abstract base class
from abc import ABCMeta, abstractmethod

#Shape is the interface
class Shape(object):

	__metaclass__ = ABCMeta

	@abstractmethod
	#a shape must have an area and a perimeter
	def area(self):
		pass

	@abstractmethod
	def perimeter(self):
		pass

class Rectangle(Shape):

	def __init__(self, width, height):
		self.width = width
		self.height = height

		super(Rectangle, self).__init__()

	#take a method already exists in superclass and instead make it obey what it obey in the Rectangle class.
	#area does nothing in Shape(object).  Create a new one.
	def area(self):
		return self.width * self.height

	def perimeter(self):
		return (self.width * 2) + (self.height * 2)

class Square(Rectangle):

	def __init__(self, side_length):
		self.side_length = side_length
		super(Square, self).__init__(side_length, side_length)

	#Override Rectangle area method
	def area(self):
		print("Using Square area method")

		return self.side_length * self.side_length

rect = Rectangle(5, 6)
print(rect.area())
print(rect.perimeter())

s = Square(5)
print(s.area())
print(s.perimeter())

# s = Shape()
# print(s)
# print(s.area())		