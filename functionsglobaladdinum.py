largest_number = 0

def set_largest_number_multiplelists(list_):

	global largest_number

	largest = 0 #initialize "largest" variable
	for number in list_:
		if number > largest:
			largest = number

	largest_number = largest
	print(largest_number) #return 357, 10000000, 9357

set_largest_number_multiplelists([45, 3, 67, 357, 33])
set_largest_number_multiplelists([45, 2, 3, 7, 8, 10000000])
set_largest_number_multiplelists([45, 453, 6777, 33])
print(largest_number) #return 6777, the last largest_number variable value.  If we removed "global largest_number" in function, print(largest_number) returns 0.