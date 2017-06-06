#williamfiset 29 Builtins 4 of 6 rBuiltins Functional Tools

#filter, reduce, map tools

#filter filters out a list.  Goes through every element in a list.  Tests against a boolean expression True or False.  Keep True elements.
def greater_than_10(num):
	return num > 10
list_ = [5,7,345,78,34,5]
#print(filter(greater_than_10, list_)) #works in python2.7
print(list(filter(greater_than_10, list_))) #works in python3.5 #print [345, 78, 34]

def beginswithe(text, prefix = "e"):
	return text.startswith(prefix)
words = ["earth","unicycle","moose","beef","eradicate"]
print(list(filter(beginswithe, words)))  #print ['earth', 'eradicate']
print("\n")

#map is a built-in function which applies a function to an entire list, each elements to the function you give it.  Feed each element to the function you give it and transform the list resulting in a new list.
numbers = range(11)
print(list(numbers)) #print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def square(num):
	return pow(num,2)
for n in numbers:
	print(square(n)) #print numbers list squared each individual line

#using for loop another way
list2 = []
numbersforloop = range(11)
for n in numbersforloop:
	list2.append(square(n))
print(list2) #print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

numbersmap = range(11)
print(list(numbersmap)) #print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] or the old list
def squaremap(num):
	return pow(num,2)
#print(map(squaremap, numbersmap)) #new list using map() works in python2.7
print(list(map(squaremap, numbersmap))) #works in python3.5 #print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100] or the new list
print("\n")

numbersmap2 = range(11)
print(list(numbersmap2)) #print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] or the old list
print(list(map(str,numbersmap2))) #print ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] converting numbers to string the new list using list(map()) works in python3.5
print([str(num) for num in numbersmap2 ]) #just another way to convert num to string in numbers list
print(list(map(int,map(str,numbersmap2)))) #convert string back to numbers or integers new list using list(map()) works in python3.5
print("\n")

numbers = range(11)
def add_two(x):
	return x + 2
print(list(map(add_two, numbers)))  #print [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print([add_two(n) for n in numbers]) #print [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12].  just another way

#reduce takes a list and shrink to one element
#reduce is python2.7
def add(a, b):
	return a + b
#print(reduce(add, xrange(1,6))) #python2.7 xrange-->[1,2,3,4,5], a=1 b=2 [3 (1+2), 3, 4, 5], a=3 b=3 [6 (3+3), 4, 5], a=6 b=4 [10 (6+4), 5], a=10 b=5 [15 (10+5)]-->15