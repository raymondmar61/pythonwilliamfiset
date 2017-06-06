def add_numbers(n0, n1, n2): #the variables inside the function paranthesis are parameters
	return n0 + n1 + n2

print(add_numbers(1,2,3)) #the values inside the calling the funciton paranthesis are called arguments

def add_numbers_infinite_parameters(a_string, *numbers): #stores parameters in a list with asterik *.  Convention to add asterik parameters at the end.
	print(a_string)
	print(numbers)
	total = 0 #initialize for loop
	for number in numbers:
		total += number
	return total

print(add_numbers_infinite_parameters("I'm about to add numbers: ",1,2,3,4,5,6,7,8,9,10))

#dictionary.  Denote parameters with two asteriks
def people_information(**people_ages):
	print(people_ages)
	average_age = 0 #initialize for loop
	for age in people_ages.values(): #want the ages in people_ages use .values()
		average_age += age

	average_age /= len(people_ages)
	return average_age

print(people_information(ryan = 345, roxanne = 45, susan = 88)) #no quotes

#assign default value in function parameter
def teen_stat_calculator(gender, age, hours_of_exercise, weight, owns_phone = True, computer = True):
	pass

teen_stat_calculator("Female",15,6,135)
teen_stat_calculator("Male",15,6,135,False) #False applies to owns_phone, default computer True is correct
teen_stat_calculator("Female",18,13,135,computer=False) #must specific computer=False because it's false, owns_phone default is correct

# import string
# words = ["word","another","word","apple"]
# new_str = string.join(words) #valid for Python2.7
# print(new_str)