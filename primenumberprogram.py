#add while loop assign true for user to continuously enter a number.  Instructor added while loop at the end.  I added number = 1 and number !=0 for user to end while loop.

number = 1
while number != 0:

	number = int(input("Please enter a number (0 to quit): "))

	#Boolean value is either True or False
	#Every if statement is translated into a boolean value

	#assigned is_prime is true
	is_prime = True
	for factor in range(2, number):
		print(factor)
		if number % factor == 0:
			is_prime = False

	if is_prime == True:
		print(number,"is a prime number!")
	else:
		print(number,"is not a prime number!")
print("Thank you for participating")