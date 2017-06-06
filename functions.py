#williamfiset 17 Functions 1 of 6 Intro, 18 Functions 2 of 6 Global, 18 Functions 2 of 6 Global, 19 Functions 3 of 6 args, kwargs, and variadic parameters, 20 Functions 4 of 6 recursion, 21 Functions 5 of 6 embedding function calls, 22 Functions 6 of 6 embedding functions

#functions are repetable code, makes code clearer, executes an operation.  Just call the function.
#math.sin() is a function

def printhelloworld():
	for x in range(6):
		print("Hello world")
printhelloworld() #returns Hello world six times

def printhelloworldparameter(amount):
	for x in range(amount):
		print("Hello world parameter")
printhelloworldparameter(2) #returns Hello world amount times

from math import pi

def circlearea(radius): #variable "radius" is a local varable to the circle_area function only. Also "radius" variable takes the 4 from r=4
	return pi * (radius ** 2) #returns the value, stores the value in function
r = 4
area = circlearea(r) #call function circle_area() with r=4, save in variable "area"
print(area) #print 50.26548245743669 if r=4
while True:	
	user_radius = int(input("Enter a radius.  Enter 0 to quit: "))
	if user_radius == 0:
		break
	print(circlearea(user_radius))
# #idiot.  User input must be in a number.  In this case, float.
# user_radius = 1
# while float(user_radius) > 0:
# 	user_radius = input("Enter a radius: ")
# 	print(circlearea(float(user_radius)))

def removevowels(string):
	vowels = "aeiou"
	new_string = ""
	for character in string: #for loop automatically loops over elements in sequences or lists.  Iterate over a sequence.  In this case, string.
		if character not in vowels: #don't print the vowels
			new_string = new_string + character #like x = x + 1 and initialize new_string as nothing.  Saves I in character which is new_string "I".  Saves space in character which is new_string "I ".  Saves l in character which is new string"I l".  No saves o in character.  Saves v in character which is new string "I lv" etc.
	return new_string
text = "I love eating apple pies"
text_without_vowels = removevowels(text)
print(text_without_vowels) #print I lv tng ppl ps

def common_start_end_lists(list1, list2):
	starts_match = list1[0] == list2[0]
	ends_match = list1[-1] == list2[-1]
	return starts_match and ends_match
print(common_start_end_lists([1,4,6,3],[1,57,3])) #print True
print(common_start_end_lists([0,4,6,3],[1,57,3])) #print False

def make_html_tag(text, tag):
	return "<%s>%s</%s>" % (tag, text, tag)
print(make_html_tag("My title","title")) #print <title>My title</title>
print(make_html_tag("Bold","bold")) #print <bold>Bold</bold>

largest_number = 0 #global variable
def set_largest_number(list_):
	largest = 0
	for number in list_:
		if number > largest:
			largest = number
	largest_number = largest
	print(largest_number)
set_largest_number([45,3,67,357,33]) #return 357
print(largest_number) #print 0

largest_number = 0 #global variable
def set_largest_number(list_):
	global largest_number #global variable largest_number recognized in function
	largest = 0
	for number in list_:
		if number > largest:
			largest = number
	largest_number = largest
	print(largest_number)
set_largest_number([45,3,67,357,33]) #return 357
print(largest_number) #print 357

a_global = "GLOBAL" #global variable
def change_global():
	a_global = "LOCAL" #local variable
change_global()
print(a_global) #print GLOBAL

a_global = "GLOBAL" #global variable
def change_global():
	global a_global #global variable a_global recognized in function
	a_global = "LOCAL" #local variable	
change_global()
print(a_global) #print LOCAL
#instructor said global keyword available.  Not often needed.  Should not be abused.

def add_numbers(n0, n1, n2):
	return n0 + n1 + n2
print(add_numbers(1,2,3))  #print 6

#infinite number of parameters passed
def add_numbersstar(a_string, *numbers):  #starred parameter is placed at the end or furthest right.  Its arguments are stored in a tuple.
	print(a_string)
	total = 0
	for number in numbers:
		total += number
	return total
print(add_numbersstar("I'm about to add some numbers",1,2,3,4,5)) #print I'm about to add some numbers /n 15

#pass a dictionary to a function.  Need double stars to the parameter.
def people_information(**people_ages):
	print(people_ages) #print {'ryan': 345, 'roxanne': 45, 'susan': 88}
	average_age = 0
	for age in people_ages.values():
		average_age += age
	average_age /= len(people_ages)
	return average_age
print(people_information(ryan=345, roxanne = 45, susan = 88))  #print 159.33333333333334

#default parameter
def teen_stat_calculator(gender, age, hours_of_exercise, weight, owns_phone = True, has_computer = True):
	pass
teen_stat_calculator("Female",15,6,135)
teen_stat_calculator("Male",15,6,135,False) #False applies to owns_phone, default has_computer True is correct
teen_stat_calculator("Female",18,13,135,has_computer=False) #must specific has_computer=False because it's false, owns_phone default is correct

#Recursion is a function calling itself, returing its own call.  Then downgrades getting simpler everytime to it gets a basecase for which it's done.  Sum up all function calls.
def doublewithoutrecursion(x):
	return x * 2
print(doublewithoutrecursion(4))  #print 8

"""  x is function counter, +2 is the summing in the function
	x=4:  +2
	x=4-1:  +2
	x=3-1:  +2
	x=2-1:  +2
	x=1-1:  +0
"""
def double(x):
	#if statement is the basecase.  Tells when function is done.  Most cases basecase is equal to zero.
	if x == 0:
		return 0
	return double(x-1) + 2 #calling itself.  Downgrading, going down.  Keep looping through until it hits zero.  The if statement basecase ends the function and returns the answer.  Sum up all function calls.
print(double(4))  #print 8

#Triangle Numbers
#(no)  n = 0 Sum 0
# n = 1  Sum 1
## n = 2  Sum 3
### n = 3  Sum 6
#### n = 4  Sum 10
def triangle_numbers(n):
	#if statement is the basecase.  Tells when function is done.  Most cases basecase is equal to zero.
	if n == 0:  
		return 0
	return triangle_numbers(n-1) + n #+n because we want to add up the previous
for n in range(20):
	print(triangle_numbers(n))

#343-->10, 111-->3 111222-->9
def sum_digits(num):
	#if statement is the basecase.  Tells when function is done.  Most cases basecase is equal to zero.
	if num ==0:
		return 0
	return sum_digits(num/10) + int(num % 10) #sum_digits(num/10) is the counter or calculate how many times to loop the function.  Take the num, divide by 10 to chop off a digit of num.  Add the last digit which is the mod of num written as (num % 10).
print(sum_digits(111222)) #return 9
print(sum_digits(989)) #return 26
print(sum_digits(343)) #return 10

#yyyxxyy count the number of x's which is 2. yxxxyxy is 4.
str_ = "yyyxxyy"
x_count = 0
for char in str_:
	if char == "x":
		x_count +=1
print(x_count) #print 2

def count_x(str_):
	if str_ == "":  #basecase
		return 0
	last_number = str_[-1]
	if last_number == "x":
		return count_x(str_[0:-1]) + 1
	return count_x(str_[0:-1]) + 0
print(count_x("yyyxxyy"))  #print 2
print(count_x("yxxxyxy"))  #print 4
""" words = "abcdefg"
 	print(words[-1]) #print g
 	print(words[0:-1]) #print abcdef
 	print(words[0:-2]) #print abcde
"""
#instructor says for loop easier than recursion

#factorial
#0! = 1
#1! = 1
#2! = 1 * 2
#3! = 1 * 2 * 3
#4! = 1 * 2 * 3 * 4
def factorial(x):
	if x == 0:
		return 1
	total = 1
	for n in range(1,x+1):
		total *= n
	return total
for x in range(10):
	print(factorial(x))

def factorialrecursion(x):
	if x in (0,1):  #basecase
		return 1
	return factorialrecursion(x-1) * x
for x in range(10):
	print(factorialrecursion(x))

def add_ten(num):
	return num + 10
def double(num):
	return num * 2
def triple(num):
	return num * 3
number = 3
tripled = triple(number)
doubled = double(tripled)
result = add_ten(doubled)
print(result) #print 28
result = add_ten(double(triple(number)))
print(result) #print 28
#instructor recommends not embedding functions.  Better to spread functions out.

def hw():
	print("Hello World!")
hw() #return Hello World!
helloworld = hw
helloworld() #return Hello World!

#embedded function
def get_adder():
	def add(a, b):
		return (a + b)
	return add
my_adder = get_adder()
print(my_adder(4,5)) #print 9

#embedded function within a function
def get_adder():
	def add(a, b):
		def double(n):
			return n * 2
		return (double(a) + double(b))
	return add
my_adder = get_adder()
print(my_adder(4,5)) #print 18

def combine_strings(*strings):
	return "".join(strings)
def print_combine_strings(function, *args):
	print(function(*args))
print_combine_strings(combine_strings,"123", "abs","tyef3") #return 123abstyef3