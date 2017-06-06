#oop Object Orientated Programming.  A class is a template or a blueprint, a receipe which defines the object.  A class is like a mother which has the characteristics of her children.  The children is the instances of the mother class.
#Classes begin with an uppercase letter.
#two leading and two trailing underscores has a meaning.  
#__init__.  Give an object instances variables when created.
#self.  Self represents the object itself.  The object itself is the variable assigned to.  In the first example, "self" is assiged the variable "will":  will's name is "William" and will's gender is "Male".  Self much be the first in the parenthesis __init__().
#methods vs functions

class Human():

	def __init__(self, name, gender):
		self.name = name
		self.gender = gender

	def speak_name(self):
		print("My name is " +self.name)

	def speak(self, text):
		print(text)

	def perform_math_task(self, math_operation, *args):
		print(self.name+ " performed a math operation and the result was" ,math_operation(*args))
		

will = Human("William","Male")
print(will.name)
print(will.gender)
will.speak_name()
#print(will.speak_name()) #no need for print() to show a print statement from a function in a class
will.speak("I love python programming")

def add(a, b):
	return(a + b)

ryan = Human("Ryan Stevens", "Male")
ryan.perform_math_task(add, 34, 67) #this is a method
print(add(99, 234)) #this is a function