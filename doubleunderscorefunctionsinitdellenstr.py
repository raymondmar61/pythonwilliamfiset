#williamfiset 43 Double Underscore Functions

#instructor shows a sample of many double underscore functions.

class ShoppingList(object):
	def __init__(self, **items):
		self.items = items
	#__len__ returns the length of the object it is
	def __len__(self):
		total_items = 0
		for _ in self.items:
			total_items += 1
		return total_items
	#string representation of the object.  Must return string
	def __str__(self):
		return 'List contains items: ' + ', '.join(self.items.keys() )
	#delete object reference count is zero, object is about to get destroyed
	def __del__(self):
		print("Object is being destroyed")
	def __add__(self, obj):
		new_dict = {}
		for key, value in self.items.items():
			new_dict[key] = value
		for key, value in obj.items.items():
			if key in self.items:
				new_dict[key] = new_dict[key] + value
			else:
				new_dict[key] = value
		return new_dict

wills_items = ShoppingList(Apple = 4, Pear = 23, Pie = 4)
ryans_items = ShoppingList(Bannana = 89, Pear = 23, Carrot = 8)

print(wills_items + ryans_items) #print {'Pear': 46, 'Carrot': 8, 'Pie': 4, 'Bannana': 89, 'Apple': 4}.  python identified two lists adding using __add__
print(len(wills_items)) #print 3.  finds the function len in the class ShoppingList()
print(str(wills_items)) #print List contains items: Pie, Pear, Apple.  if there's not str function, returns hexidecimal and type