def common_start_end_lists(list1, list2):
	starts_match = list1[0] == list2[0] #returns True or False
	ends_match = list1[-1] == list2[-1] #negative number index in a list begins at the end of the list
	return starts_match and ends_match #returns True or False

gijoe = ["duke", "flint", "ladyjaye," "stormshadow"]
cobra = ["cobracommander", "destro", "baroness", "firefly", "stormshadow"]
print(common_start_end_lists( [1,4,6,3],[1,57,3]))
print(common_start_end_lists(gijoe,cobra))

def make_html_tag(text, tag):
	print("<"+tag+">"+text+"</"+tag+">")
	print("<%s>%s</%s>" % (tag, text, tag))

make_html_tag("hello","b")

#global variable can be used inside and outside a function.  Inside a function is read only.
largest_number = 0

def set_largest_number(list_):

	largest = 0 #initialize "largest" variable
	for number in list_:
		if number > largest:
			largest = number

	largest_number = largest
	print(largest_number) #return 357

set_largest_number([45, 3, 67, 357, 33])
print(largest_number) #return 0.  Now I know why the return statement in a function is important.  It returns the value from the function.  "print(largest_number)" outside the function prints 0 and inside the function prints 357.
print("-----")

#global variable can be used inside and outside a function.
#declare "largest_number" variable as global inside the function called "into scope"
largest_number = 0

def set_largest_number_globalvariable(list_):

	global largest_number

	largest = 0 #initialize "largest" variable
	for number in list_:
		if number > largest:
			largest = number

	largest_number = largest
	print(largest_number) #return 357

set_largest_number_globalvariable([45, 3, 67, 357, 33])
print(largest_number) #return 357
print("-----")
largest_number = 0

def set_largest_number_multiplelists(list_):

	global largest_number

	largest = 0 #initialize "largest" variable
	for number in list_:
		if number > largest:
			largest = number

	largest_number = largest
	print(largest_number) #return 357, 45, 9357

set_largest_number_multiplelists([45, 3, 67, 357, 33])
set_largest_number_multiplelists([45, 2, 3, 7, 8])
set_largest_number_multiplelists([45, 453, 6777, 9357, 33])
print(largest_number) #return 9357
print("-----")
largest_number = 0

def set_largest_number_oneresult(list_):

	global largest_number

	largest = 0 #initialize "largest" variable
	for number in list_:
		if number > largest:
			largest = number

	largest_number = largest
	
set_largest_number_oneresult([45, 3, 67, 357, 33])
set_largest_number_oneresult([45, 2, 3, 7, 8])
set_largest_number_oneresult([45, 453, 6777, 19357, 33])
print(largest_number) #return 19357

#global variable
a_global_variable = "GLOBAL"

def change_global():
	#to bring a_global_variable to the function, declare it with keyword "global"
	global a_global_variable
	#local variable
	a_global_variable = "LOCAL"
	return a_global_variable

change_global()
print(a_global_variable)