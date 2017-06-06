#Recursion is a function calling itself, returing its own call.  Then downgrades getting simpler everytime to it gets a basecase for which it's done.  Sum up all function calls.

def doublenumber(x):
	return x * 2
print(doublenumber(4))

def doublenumberrecursion(x):
	
	#if statement is the basecase.  Tells when it's done, too.
	if x == 0:
		return 0

	return doublenumberrecursion(x - 1) + 2 #calling itself.  Downgrading, going down.  Keep looping through until it hits zero.  The if statement basecase ends the function and returns the answer.  Sum up all function calls.

"""  x is function counter, +2 is the summing in the function
	x=4:  +2
	x=4-1:  +2
	x=3-1:  +2
	x=2-1:  +2
	x=1-1:  +0
"""

print(doublenumberrecursion(4))

#Triangle Numbers
#(no)  n = 0 Sum 0
# n = 1  Sum 1
## n = 2  Sum 3
### n = 3  Sum 6
#### n = 4  Sum 10

def triangle_numbers(n):
	#if statement is the basecase.  Tells when it's done, too.
	if n == 0:
		return 0

	return triangle_numbers(n - 1) + n #calling itself.  Downgrading, going down.  Keep looping through until it hits zero.  The if statement basecase ends the function and returns the answer.  Sum up all function calls.

for n in range(20):
	print(triangle_numbers(n))

# 343 --> 10 add 3+4+3
# 111222 --> 9 add 1+1+1+2+2+2
def sum_digits(num):
	if num == 0:
		return 0

	return sum_digits(num / 10) + int(num % 10) #it seems calling the function itself the paranthesis is the counter to tell the function to keep going or ready to stop at the base case.  The right is the summing up all function calls.

print(sum_digits(343))
print(sum_digits(111222))

#counter number of times "x" appears in a string
#yyyxxyy returns two x's
#yxxxyxy returns four x's

#for loop method
# str_ = "yyyxxyy"
# x_count = 0
# for char in str_:
# 	if char == "x":
# 		x_count += 1
# 	#return x_count #no return statement because it's not a function
# print("Number of x's:",x_count)

def count_x(str_):
	#basecase is no more string characters
	if str_ == "":
		return 0
	last_number = str_[-1]
	print(last_number)

	if last_number == "x":
		return count_x(str_[0:-1]) + 1 #zero is default, can leave blank
	return count_x(str_[0:-1]) + 0 #zero is default, can leave blank

print(count_x("yyyxxyy"))
print(count_x("yxxxyxy"))
print("Easier to use a for loop above count_x() function in this case")

#factorial
#0! = 1
#1! = 1
#2! = 1 * 2
#3! = 1 * 2 * 3
#4! = 1 * 2 * 3 * 4

# def factorial(x):
# 	if x == 0:
# 		return 1

# 	total = 1
# 	for n in range(1,x + 1):
# 		total *= n
# 	return total

# for x in range(10):
# 	print(factorial(x))

def factorial(x):
	#basecase
	if x in (0,1):  #same as x == 0 or x == 1?
		return 1

	return factorial(x - 1) * x  #calling itself.  Downgrading, going down.  Keep looping through until it hits zero.  The if statement basecase ends the function and returns the answer.  Multiple all function calls.


for x in range(10+1): #need to add +1 because of range() function being one less
	print(factorial(x))
#skip the for loop printing all factorials and want the answer
print(factorial(10))

