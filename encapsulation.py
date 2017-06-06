#Encapsulation is the art of data hiding

class ClassName():

	def __init__(self):

		self._privateVar = "Private"
		self.publicVar = "public"

	def _privateMethod(self):  #start privateMethod with an underscore
		pass

	def _privateMethod2(self):  #start privateMethod with an underscore
		pass

	def publicMethod(self):
		
		return 5

c = ClassName()

print(c._privateMethod())	
print(c.publicMethod())
print(c._privateVar)
print(c.publicVar)