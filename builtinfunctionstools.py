#filter, reduce, map tools

#filter filters out a list.  goes through every element in a list tests against a boolean expression True or False.  Keep True elements.
def greater_than_10(num):
	return num > 10

list_ = [5,7,345,78,34,5]

print(filter(greater_than_10, list_)) #works in python2.7
print(list(filter(greater_than_10, list_))) #works in python3.5

def beginswithe(text, prefix = "e"):
	return text.startswith(prefix)

words = ["earth","unicycle","moose","beef","eradicate"]

print(list(filter(beginswithe, words)))

#map is a built-in function which applies a function to an entire list, each elements to the function you give it.  Feed each element to the function you give it and transform the list resulting in a new list.

numbers = range(11) #range 0 to 10
print(list(numbers)) #old list

def square(num):
	return pow(num,2)

#using for loop
for n in numbers:
	print(square(n))

#using for loop another way
list2 = []
for n in numbers:
	list2.append(square(n))
print(list2)

print(map(square, numbers)) #new list using map() works in python2.7
print(list(map(square, numbers))) #new list using map() works in python3.5

print(list(numbers)) #old list
print(list(map(str,numbers))) #convert numbers to string new list using map() works in python3.5
print([str(num) for num in numbers ]) #just another way to convert num to string in numbers list
print(list(map(int,map(str,numbers)))) #convert string back to numbers or integers new list using map() works in python3.5

def add_two(x):
	return x + 2

print(list(map(add_two, numbers)))
print([add_two(n) for n in numbers])

#reduce takes a list and shrink to one element
#reduce is python2.7
def add(a, b):
	return a + b

#print(reduce(add, xrange(1,6))) #python2.7 xrange-->[1,2,3,4,5], a=1 b=2 [3, 3, 4, 5], a=3 b=3 [6, 4, 5], a=6 b=4 [10, 5], a=10 b=5 [15]-->15