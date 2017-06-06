#oop Object Orientated Programming.  A class is a template or a blueprint, a receipe which defines the object.  A class is like a mother which has the characteristics of her children.  The children is the instances of the mother class.
#Classes begin with an uppercase letter.
#two leading and two trailing underscores has a meaning.  
#__init__.  Give an object instances variables when created.
#self.  Self represents the object itself.  The object itself is the variable assigned to.

class Rectangle():

	#"self" is "my_rectangle".  Implied argument.
	def __init__(self, width, length):
		self.width = width
		self.length = length

	#these are methods below
	def area(self):
		return((self.width * self.length))

	def perimeter(self):
	 	return((self.width * 2) + (self.length) * 2)

my_rectangle = Rectangle(5, 6)
another_rectangle = Rectangle(2, 10)

my_rectangle.area()
my_rectangle.perimeter()
print(my_rectangle.area())  #need print() because area() and perimeter() methods don't have print()
print(my_rectangle.perimeter()) #need print() because area() and perimeter() methods don't have print()

another_rectangle.area()
another_rectangle.perimeter()
print(another_rectangle.area())  #need print() because area() and perimeter() methods don't have print()
print(another_rectangle.perimeter()) #need print() because area() and perimeter() methods don't have print()

#car class - number of wheels on the car.  Class or static variable.
#house class - house address.  Instance variable.
#house class - purchase price.  Instance variable.
#character class - maximum health.  Class or static variable.
#grid class - width and height of grid.  Instance variable.
#polygon class - the number of vertices  Instance variable.
#triangle class - right triangle, scalene, equalaterial  Class or static variable.
#math class - golden ratio constant.  Class or static variable.

class Character():
	#class or static variables below
	total_number_of_characters = 0
	max_health = 100

	def __init__(self, name):
		#instance variables
		self.name = name
		self.health = Character.max_health #class name must be mention for class variables classname.classvariable
		Character.total_number_of_characters += 1

bob = Character("Bob")
ryan = Character("Ryan Stevens")

print(Character.total_number_of_characters)
print(Character.max_health)
print(bob.name)
print(ryan.name)
