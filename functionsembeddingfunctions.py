def hw():
	print("Hello World!")

hw()
#rename calling a variable?  Then assign a variable to calling a function.  Assigning a varaiable also becomes calling a function.
helloworld = hw
helloworld()

def get_adder():

	def add(a, b):

		return(a + b)

	return add #get_adder() returns the add() function

#add(4,5) #error message because add() is defined inside the get_adder() function
#we can use the add() function by assigning get_adder to a variable
#Instructor's words:  if we have a variable that stores the get_adder() or add() function, we can use the add() function
my_adder = get_adder()
print(my_adder(4,5))

def get_adder():

	def add(a, b):

		def double(n):
			return n * 2

		return (double(a) + double(b)) #return statement for add() calling double()

	return add #get_adder() returns the add() function

#we can use the add() function by assigning get_adder to a variable
#Instructor's words:  if we have a variable that stores the get_adder() or add() function, we can use the add() function
my_adder = get_adder()
print(my_adder(6,7))

def combine_strings(*strings):
	return "".join(strings) #(str1, str2, str3) --> str1str2str3

def print_combined_strings(function, *args):
	print(function(*args)) #args --> (str1, str2, str3) removes paranthesis

print_combined_strings(combine_strings, "123", "abs", "tyef3")