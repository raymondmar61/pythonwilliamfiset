#williamfiset 23 Assert Try Raise Except Finally

#ASSERT
age = 344
#check condition, if false then run whatever is on the right of comma as an AssertionError
assert age >= 0, "How is your age negative?\n"
print("Your age is", age) #print Your age is 344

#TRY EXCEPT
while True:
	try:  #try: the code below which may work or not work
		numerator = float(input("Enter a numerator: "))
		denominerator = float(input("Enter a denominerator: "))
		print("The fraction ratio is %f " % (numerator/denominerator))
	except ZeroDivisionError as theZeroError: #print statement at except: is executed when an error happened at try:.  In this case, user enters zero as denominator.  Python has a custom defined error.  Use ZeroDivisionError.  Other custom defined errors are BaseException and Exception.  Can have more than one except
		print("An error has happened")
		print("The error written at except: statement is printed here-->" ,theZeroError)

#FILES
#my_file = open("filename.txt", "w") #opens file.  If not there, it creates one.  Opens in write mode.  Other modes are read and read-write.

#FINALLY
# my_file = open("filename.txt", "w")
# try:
# 	my_file.write("I wrote in a new file!\n")
# except Exception as error:
# 	print(error)
# except ZeroDivisionError as error:
# 	print(error)
# finally: #always execute no matter try: successful or unsuccessful
# 	my_file.close()
# 	pass

#RAISE
#user creates own errors with error messages
age = 199
if age > 135:
	raise Exception("Your supposed to be dead!  You are older than 135 years of age!")