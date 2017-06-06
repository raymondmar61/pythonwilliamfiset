#oop Object Orientated Programming.  A class is a template or a blueprint, a receipe which defines the object.  A class is like a mother which has the characteristics of her children.  The children is the instances of the mother class.
#Classes begin with an uppercase letter.
#Each class has a unique hexadecimal number which is the address in memory.  Can call a class more than once with each called calss its own unique hexadecimal number.  Call a class by setting the class equal to a variable; for example, myboat = Boat(), myboat2 = Boat().

class Boat():
	pass

my_boat = Boat()
my_boat2 = Boat()
print(my_boat)
print(my_boat2)
#id() prints the integer representation of the class unique hexadecimal number
print(id(my_boat))
print(id(my_boat2))
hex_str_boat = str(my_boat)[-12:-1]
hex_str_boat2 = str(my_boat2)[-12:-1]
print(int(hex_str_boat, 16))
print(int(hex_str_boat2, 16))

x = 56
def change_value(num):
	num = 90

print(x)
change_value(x)
print(x)

class Boat():
	def __init__(self):
		self.cargo_weight = 23

def change_cargo_weight(ship):
	ship.cargo_weight = 45

boat = Boat()
print(boat.cargo_weight)
change_cargo_weight(boat)
print(boat.cargo_weight)