#williamfiset 42 Static Methods
#static methods belong to a class, not specific to an object

#old way.  I can't make it to work.
# class Math():
# 	def factorial(x):
# 		if x in (0, 1): return 1
# 		return factorial(x - 1) * x

# math_object = Math()
# math_object.factorial(4)

#static way
class Math():
	@staticmethod
	def factorial(x):
		if x in (0, 1):return 1
		return Math.factorial(x - 1) * x

#old way assigning an object to a class
math_object = Math()
print(math_object.factorial(4))

#quicker way calling the static way
print(Math.factorial(4))