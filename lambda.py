#williamfiset 32 lambda

#lambda is another way to make a function.  A quick and dirty way.  One line to do everything we want.  Consist of highly of functional programming tools.

def square(x):
	return (x*x)
print(square(99)) #print 9801
#square2 is not a variable.  It acts as a function.  Lambda always return a value.  Can't return None.
square2 = lambda x: x*x
print(square2(99)) #print 9801

def sumRGB(r, g, b):
	return (r + g + b)
print(sumRGB(255,255,255)) #print 765
#sumRGB2 is not a variable.  It acts as a function.  Lambda always return a value.  Can't return None.
sumRGB2 = lambda r, g, b: r + g + b
print(sumRGB2(255,255,255)) #print 765

remove_duplicates = lambda iterable: set(iterable)
print(remove_duplicates("roooot")) #print {'r', 't', 'o'}
print(remove_duplicates([1,1,1,2,3,4])) #print {1, 2, 3, 4}
remove_duplicateslist = lambda iterable: list(set(iterable))
print(remove_duplicateslist("roooot")) #print ['r', 't', 'o']
print(remove_duplicateslist([1,1,1,2,3,4])) #print [1, 2, 3, 4]

convert_list_to_int = lambda iterable: map(int, iterable)
print(convert_list_to_int(["123","456","34"])) #print <map object at 0x7f1f6c877400>
convert_list_to_int = lambda iterable: list(map(int, iterable))
print(convert_list_to_int(["123","456","34"])) #print [123, 456, 34]
print("\n")

def evens(list_):
	even = []
	for num in list_:
		if num % 2 == 0: #number is even
			even.append(num)
	return even
print(evens(range(100))) #print [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

def evens2(list_):
	#add a lambda
	is_even = lambda num: num % 2 == 0
	even = []
	for num in list_:
		if is_even(num):
			even.append(num)
	return even
print(evens2(range(100)))

is_even = lambda num: num % 2 == 0
evens3 = lambda lst_: list(filter(is_even, lst_))
print(evens3(range(100)))
