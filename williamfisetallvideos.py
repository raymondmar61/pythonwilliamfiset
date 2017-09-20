apples = 20
if apples > 3:
	print("First if statement independent greater than three apples.")
if apples > 5:
	print("Second if statement independent greater than five apples.")
else:
	print("else: is like elif True:")
if 10 <= apples <= 20:
	print("Third if statement independent between 10 and 20 apples inclusive.")
location = "home"
if location is "home" or location is "vegas":
	print("I'm "+location)

listl = [1,2,3,4,5,6]
print(listl) #print [1, 2, 3, 4, 5, 6]
print(len(listl)) #print 6
items = ["cat","dog","moon","shoe"]
print(items[1]) #print dog
print(items.index("cat")) #print 0
items[1] = "parrot"
print(items) #print ['cat', 'parrot', 'moon', 'shoe']
items.append("door")
print(items) #print ['cat', 'parrot', 'moon', 'shoe', 'door']
items.insert(0,"door beginning")
print(items) #print ['door beginning', 'cat', 'parrot', 'moon', 'shoe', 'door']
items.remove("door beginning")
print(items) #print ['cat', 'parrot', 'moon', 'shoe', 'door']
items.pop()
print(items) #print ['cat', 'parrot', 'moon', 'shoe']
lastelement = items.pop()
print(lastelement) #print shoe
print(items) #print ['cat', 'parrot', 'moon']
items.pop(1)
print(items) #print ['cat', moon']
items = ["cat","dog","moon","shoe","cat","dog","cat"]
print(items.count("cat")) #print 3
print(items.count("dog")) #print 2
items.sort()
print(items) #print ['cat', 'cat', 'cat', 'dog', 'dog', 'moon', 'shoe']
items.reverse()
print(items) #print ['shoe', 'moon', 'dog', 'dog', 'cat', 'cat', 'cat']
items = ["mop","hop","cat","dog","moon","shoe","cat","dog","cat"]
items.reverse()
print(items) #print ['cat', 'dog', 'cat', 'shoe', 'moon', 'dog', 'cat', 'hop', 'mop']
alist = [11,22,33,44,55,66,77,88]
blist = ["|||"]
bars = blist * 4
print(bars) #print ['|||', '|||', '|||', '|||']
barsoutoflist = "".join(bars)
print(barsoutoflist) #print ||||||||||||
print(alist[2:5]) #print [33, 44, 55]
print(alist[-1]) #print 88
print(alist[0::2]) #print [11, 33, 55, 77]
print(alist[-1::-2]) #print [88, 66, 44, 22]
ctuple = ("a","b","c")
print(ctuple[2]) #print c
ctuple = (1,2,3,4,5,6,7,8)
print(ctuple[1:5]) #print (2, 3, 4, 5)
listfromdictionaryvideo = [1,2,3,457,75,5,3]
del listfromdictionaryvideo[3]
print(listfromdictionaryvideo) #print [1, 2, 3, 75, 5, 3]
listfromdictionaryvideo = []
#del listfromdictionaryvideo[0:] #same as listfromdictionaryvideo = [] empties list
print(listfromdictionaryvideo) #print []
print("\n")

helloworld = "Hello world!"
print(helloworld[0:5]) #print Hello
print("Hello world!"[0:5]) #print Hello
print("Hello world!"[::-1]) #print !dlrow olleH
sstring = "do goat sheep boat"
print(sstring.split()) #print ['do', 'goat', 'sheep', 'boat']
print(list(sstring)) #print ['d', 'o', ' ', 'g', 'o', 'a', 't', ' ', 's', 'h', 'e', 'e', 'p', ' ', 'b', 'o', 'a', 't']
sstring = "do/goat/sheep/boat/boat"
print(sstring.split("/")) #print ['do', 'goat', 'sheep', 'boat', 'goat']
print(sstring.replace("boat","yoga")) #print do/goat/sheep/yoga/yoga
print(sstring.find("goat")) #print 3 which is the starting index for goat
print(sstring.startswith("do")) #print True
print(sstring.endswith("boat/boat")) #print True
wordis = "ABCiop"
print(wordis.upper()) #print ABCIOP
print(wordis.lower()) #print abciop
llist = ["1","2","3","4"]
print("-".join(llist)) #print 1-2-3-4
print("".join(llist)) #print 1234
number = 345436
hex_ = 0X33
print(hex_) #print 51
exp = 2.5e6
print(exp) #print 2500000.0
astring = "The String"
anumber = 457
print("My number is %f.  My string is %s." % (anumber, astring)) #print My number is 457.000000.  My string is The String.
print("My number is %d.  My string is %s." % (anumber, astring)) #print My number is 457.  My string is The String.
astring = "The String2"
anumber = 457.56789
print("My number is %.2f.  My string is %s." % (anumber, astring)) #print My number is 457.57.  My string is The String2.
print("My number is %d.  My string is %s." % (anumber, astring)) #print My number is 457.  My string is The String2.
print("My number is {0}.  My string is {1}.".format(anumber, astring)) #print My number is 457.56789.  My string is The String2.
print("My number is "+str(int(anumber))+".  My string is "+astring+".") #print My number is 457.  My string is The String2.
escapecharacters = list("Hello World!")
print(escapecharacters) #print ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']
print("\v".join(escapecharacters))
"""
H
 e
  l
   l
    o
      
      W
       o
        r
         l
          d
           !
"""
print(list(range(1,11))) #print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(10,101,10))) #print [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("\n")

peopleages = {"Ryan": 89, "William": 23, "Catherine": 44}
print(peopleages) #print {'Ryan': 89, 'Catherine': 44, 'William': 23}
print(peopleages["Ryan"]) #print 89
print(peopleages.get("Ryan")) #print 89
for key, value in peopleages.items():
	print(key, value)
"""
William 23
Catherine 44
Ryan 89
"""
for eachvalues in peopleages.values():
	print(eachvalues) #print values 89\n 44\n 23
del(peopleages["Ryan"])
print(peopleages) #print {'Catherine': 44, 'William': 23}
peopleages.update({"Ryan":90})
print(peopleages) #print {'Ryan': 90, 'Catherine': 44, 'William': 23}
if "John" in peopleages:
	del peopleages["John"]
peopleages.clear()
print(peopleages)
print("\n")

import math
#print(dir(math)) #prints all functions in math module
number = 5.6
print(math.ceil(number)) #print 6
print(math.floor(number)) #print 5
print(math.factorial(4)) #print 24
print(math.exp(2)) #print 7.38905609893065
print(math.pow(2,4)) #print 16.0
print(math.log(16,2)) #print 4.0
print(math.pi) #print 3.141592653589793
from math import *
print(pi) #print 3.141592653589793
from math import ceil, floor
number2 = 7.4
print(ceil(number2)) #print 8
print(floor(number2)) #print 7
from math import factorial as fact
print(fact(6)) #print 720
print("\n")

def printhelloworld(amount):	
	for eachhello in range(0,amount):
		print("Hello World",end="")	
printhelloworld(2) #return HelloWorldHello World
print("")
from math import pi
def circlearea(radius):
	return pi * (radius ** 2)
r = 4
area = circlearea(r)
print(area) #print 50.26548245743669
def removevowels(string):
	vowels="aeiou"
	newstring = ""
	for character in string:
		if character not in vowels:
			newstring = newstring + character
	return newstring
print(removevowels("I love eating apples pies")) #print I lv tng ppls ps
def commonstartendlists(list1, list2):
	startsmatch = list1[0] == list2[0]
	endsmatch = list1[-1] == list2[-1]
	return startsmatch and endsmatch
print(commonstartendlists([1,4,6,3],[1,57,3])) #print True
print(commonstartendlists([1,4,6,3],[1,57,9])) #print False
def makehtmltag(text, tag):
	return "<%s>%s</%s>" % (tag, text, tag)
print(makehtmltag("My Title","title")) #print <title>My Title</title>
largestnumber = 0
def setlargestnumber(list_):
	largest = 0
	for number in list_:
		if number > largest:
			largest = number
	largestnumber = largest
	print(largestnumber)
setlargestnumber([45,3,67,357,33]) #return 357
print(largestnumber) #print 0
#inefficient way to print largestnumber global variable
largestnumber2 = 0
def setlargestnumber2(list_):
	largest = 0
	for number in list_:
		if number > largest:
			largest = number
	largestnumber = largest
	return largestnumber	
largestnumber2 = setlargestnumber2([45,3,67,357,33])
print(largestnumber2) #print 357
#efficient way to print largestnumber global variable
largestnumber3 = 0
def setlargestnumber3(list_):
	global largestnumber3
	largest = 0
	for number in list_:
		if number > largest:
			largest = number
	largestnumber3 = largest
	print(largestnumber3)
setlargestnumber3([45,3,67,3357,33]) #return 3357
aglobal = "global"
def changeglobalvariable():
	global aglobal
	aglobal = "local"
changeglobalvariable()
print(aglobal) #print local; however if global aglobal removed in def changeglobalvariable(), then print global
def addnumbers0(n0, n1, n2):
	return n0 + n1 + n2
print(addnumbers0(1,2,3)) #print 6
def addnumbers(astring, *numbers):
	print(astring) #print I am about to add some numbers star arguments *numbers at end:
	print(numbers) #print (1, 2, 3, 4, 5, 6)
	print(type(numbers)) #print <class 'tuple'>
	total = 0
	for eachnumber in numbers:
		total += eachnumber
	return total
print(addnumbers("I am about to add some numbers star arguments *numbers at end: ",1,2,3,4,5,6)) #print I am about to add some numbers star arguments *numbers at end:\n 21
#pass a dictionary to a function
def peopleinformation(**peopleages):
	print(peopleages) #print {'susan': 88, 'ryan': 345, 'roxanne': 45}
	averageage = 0
	for age in peopleages.values():
		averageage += age
	averageage /= len(peopleages)
	return (averageage)
print(peopleinformation(ryan=345, roxanne=45, susan=88)) #print 159.33333333333334
def teen_stat_calculator(gender, age, hours_of_exercise, weight, owns_phone = True, computer = True):
	pass
teen_stat_calculator("Female",15,6,135)
teen_stat_calculator("Male",15,6,135,False) #False applies to owns_phone, default computer True is correct
teen_stat_calculator("Female",18,13,135,computer=False) #must specific computer=False because it's false, owns_phone default is correct
#recursion
def double0(x):
	return x * 2
print(double0(4)) #print 8
def double(x):
	print(x)
	#base case is when x is zero, it's time to return.  exit function in lament terms.
	if x == 0:
		return 0
	return double(x-1) + 2 #It's like a counter starting a four going down by one.  double(x-1) is the counter--like a loop counter.  While counting down, add two for each counting down.  This is recursion.
"""
double(x-1)-->recursion
4-->2
3-->2
2-->2
1-->2
0-->0
"""
print(double(4)) #print 8
#recursion
def trianglenumbers(n):
	if n == 0: #base case
		return 0
	return (trianglenumbers(n-1) + n)
"""
trianglenumbers(n-1)-->recursion
1-->1
2-->3
3-->6
4-->10
5-->15
"""
for n in range(0,20):
	print(trianglenumbers(n))
#recursion
def sumdigits(num):
	#print(num)
	if num == 0: #base case
		return 0
	return (sumdigits(num/10)) + int((num % 10))
"""
343-->10 3+4+3
111222-->9 1+1+1+2+2+2
"""
print(sumdigits(343))
print(sumdigits(111222))
#recursion
stringx0 = "yyyxxyy"
xcount = 0
for char in stringx0:
	if char == "x":
		xcount += 1
print(xcount) #print 2
#for loop above as recursion
def countx(stringx):
	if stringx == "": #base case
		return 0
	lastnumber = stringx[-1]
	if lastnumber == "x":
		return countx(stringx[0:-1]) + 1
	else:
		return countx(stringx[0:-1]) + 0
"""
yyyxxyy-->2  2 x's
yxxxyxy-->4  4 x's
"""
print(countx("yyyxxyy")) #print 2
print(countx("yxxxyxy")) #print 4
#recursion factorial function
def factorial0(x):
	if x == 0:  #base case
		return 1
	total = 1
	for n in range(1,x+1):
		total *= n
	return total
for x in range(0,10):
	print(factorial0(x))
def factorial(x):
	if x in (0, 1): #base case
		return 1
	else:
		return factorial(x-1) * x
"""
0!-->1
1!-->1
2!-->2
3!-->6
4!-->24
"""
for x in range(0,10):
	print(factorial(x))
#embedding function calls
def addten(num):
	return num + 10
def double(num):
	return num * 2
def triple(num):
	return num * 3
number = 3
tripled = triple(number)
doubled = double(tripled)
result = addten(doubled)
print(result) #print 28  (2(3*3))+10
number = 3
result = addten(double(triple(number)))
print(result) #print 28
def hw():
	print("Hello World")
helloworld = hw()
helloworld #return Hello World
def getadder():
	def add(a, b):
		return a + b
	return add
myadder = getadder()
print(myadder(4,5)) #print 9
def getadder2():
	def add(a, b):
		def double(n):
			return n * 2		
		return double(a) + double(b)
	return add
myadder2 = getadder2()
print(myadder2(4,5)) #print 18
def combinestrings(*strings):
	return "".join(strings)
def printcombinedstrings(function, *args):
	print(function(*args))
printcombinedstrings(combinestrings, "123","abs","tyef3") #print 123abstyef3
print("\n")

age = 34
assert age >= 0, "If assert is false, the do the action:  AssertionError:  How is your age negative?  Python crashes.\n"
print("Your age is",age)
while True:
	try:
		#numer = float(input(("Enter a numerator: ")))
		#denom = float(input(("Enter a denominator: ")))
		numer = 5
		denom = 0
		print("The fraction ratio is %f " % (numer/denom))
		break
	except ZeroDivisionError:
		print("An error happened")
		break
myfile = open("fileondesktop.txt","w")
try:
	myfile.write("I wrote in a new file\n")
except BaseException:
	print("error")
finally: #finally always executes 
	myfile.close()
# age = 199
# if age > 135:
# 	#print("You're supposed to be dead!")
# 	raise Exception("You're supposed to be dead.  You're older than 135 years old.") #user created an custom error message using raise Exception().  error message appered because age = 199 is greater than age > 135.
filename = "example.txt"
examplefile = open(filename,"w")
try:
	examplefile.write("Blue goose on the loose\n")
	examplefile.write("Honeycomb cereal\n")
except Exception as error:
	print("Problem handling file, error was %s" % error)
finally:
	examplefile.close()
with open(filename,"w") as examplefile:
	lines = ["Happy whale on parade!\n","Red Bee dancing\n","The great git in the sky!\n"]
	examplefile.write(lines[0])
	examplefile.write(lines[1])
	examplefile.write(lines[2])
	examplefile.writelines(lines) #better than examplefile.write(lines[])
with open(filename,"r") as readingfile:
	for eachline in readingfile.readlines():
		print(eachline)
with open(filename,"r") as readingfile:
	readnoforloop = readingfile.read()
	print(readnoforloop)
filecontent = ""
with open(filename,"r") as readingfile:
	filecontent = readingfile.read()
newfilecontent = []
counter = 0
for character in filecontent:
	if counter % 2 == 0:
		newfilecontent.append(character.upper())
	else:
		newfilecontent.append(character.lower())
	counter += 1
newfilecontent = "".join(newfilecontent)
with open(filename,"w") as writeablefile:
	writeablefile.write(newfilecontent)
with open(filename,"a") as appendingfile:
	for eachnumber in range(1,21):
		appendingfile.write(str(eachnumber))
print("\n")

print(abs(-100)) #print 100
print(pow(4,2)) #print 16.0
print(int(pow(4,2))) #print 16.0
print(4**2) #print 16
numbers3 = [1, 77, 33, 55]
print(min(numbers3)) #print 1
print(max(numbers3)) #print 77
letters = ["za","y","f","h","a"]
print(min(letters)) #print a
print(max(letters)) #print za
numbers = ["one","two","three","four"]
seasons = ["fall","winter","spring","summer"]
print(enumerate(numbers)) #print <enumerate object at 0x7f2581f073f0>
print(list(enumerate(numbers))) #print [(0, 'one'), (1, 'two'), (2, 'three'), (3, 'four'
print(list(enumerate(seasons))) #print [(0, 'fall'), (1, 'winter'), (2, 'spring'), (3, 'summer')]
print(tuple(enumerate(seasons))) #print ((0, 'fall'), (1, 'winter'), (2, 'spring'), (3, 'summer'))
filename = "example.txt"
"""
filecontent = ""
with open(filename,"r") as readingfile:
	filecontent = readingfile.read()
newfilecontent = []
counter = 0
for character in filecontent:
	if counter % 2 == 0:
		newfilecontent.append(character.upper())
	else:
		newfilecontent.append(character.lower())
	counter += 1
newfilecontent = "".join(newfilecontent)
"""
filecontent = ""
with open(filename,"r") as readingfile:
	filecontent = readingfile.read()
newfilecontent = []
for index, character  in enumerate(filecontent):
	if index % 2 == 0:
		newfilecontent.append(character.upper())
	else:
		newfilecontent.append(character.lower())
newfilecontent = "".join(newfilecontent)
numbers = ["one","two","three","four"]
seasons = ["fall","winter","spring","summer"]
print(zip(numbers, seasons)) #print <zip object at 0x7fc89fa54108>
print(list(zip(numbers, seasons))) #print [('one', 'fall'), ('two', 'winter'), ('three', 'spring'), ('four', 'summer')]
for eachnumber, eachseason in zip(numbers, seasons):
	print(eachnumber, eachseason) #print one fall\n two winter\n three spring\n four summer
unordered_numbers = [1,7,3,7,2,4,0,2,-2,5,3]
unordered_characters = ["r","t","©","v","s","b"]
unordered_strings = ["cat","dog","mice"]
unordered_dictionary = [{2:"two",1:"one",4:"four"}]
print(sorted(unordered_numbers)) #print [-2, 0, 1, 2, 2, 3, 3, 4, 5, 7, 7]
print(sorted(unordered_characters)) #print ['b', 'r', 's', 't', 'v', '©']
print(sorted(unordered_strings))  #print ['cat', 'dog', 'mice']
print(sorted(unordered_dictionary)) #print [{1: 'one', 2: 'two', 4: 'four'}]
print(sorted("hello world!")) #print [' ', '!', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']; broke string into a list, then sort characters in the list individually
print(sorted(unordered_numbers, reverse = True)) #print [7, 7, 5, 4, 3, 3, 2, 2, 1, 0, -2]
print(sorted(unordered_characters, reverse = True)) #print ['©', 'v', 't', 's', 'r', 'b']
print(sorted(unordered_strings, reverse = True)) #print ['mice', 'dog', 'cat']
print(sorted(unordered_dictionary, reverse = True)) #print [{1: 'one', 2: 'two', 4: 'four'}]
print(sorted("hello world!", reverse = True)) #print ['w', 'r', 'o', 'o', 'l', 'l', 'l', 'h', 'e', 'd', '!', ' ']; broke string into a list, then sort characters in the list individually
print(len([1,2,3,4,5])) #print 5
print(len({"two": 2, "key": "value", ("tuple", "str") : {"list":"inception"}})) # print 3
print(len("four"))  #print 4
#print(len((1), (2), (3), (4), (5, 6, (7, 8)))) #error message len takes one argument only.  len() takes exactly one argument (5 given)
#print(len((1), (2), (3), (4), (5, 6, 7, 8))) #error message len takes one argument only
def greaterthantenfilterlist(num):
	return num > 10
numberslist = [5, 7, 345, 78, 34, 5]
print(filter(greaterthantenfilterlist, numberslist)) #print <filter object at 0x7f3fa98dc278>
print(list(filter(greaterthantenfilterlist, numberslist))) #print [345, 78, 34]
def beginswithefilterlist(text, prefix="e"):
	return text.startswith(prefix)
words = ["earth","unicycle","moose","beed","eradicate"]
print(list(filter(beginswithefilterlist, words))) #print ['earth', 'eradicate']
numbers = list(range(0,11))
print(numbers) #print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def squaremaplist(num):
	return pow(num,2)
"""
numberssquared = []
for eachnumbers in numbers:
	print(squaremaplist(eachnumbers))
	numberssquared.append(squaremaplist(eachnumbers))
print(numberssquared) #print [0.0, 1.0, 4.0, 9.0, 16.0, 25.0, 36.0, 49.0, 64.0, 81.0, 100.0]
"""
print(list(map(squaremaplist, numbers))) #print [0.0, 1.0, 4.0, 9.0, 16.0, 25.0, 36.0, 49.0, 64.0, 81.0, 100.0].  No need for the for loop.
print(list(map(str, numbers))) #print ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'.  str is a function
print(list(map(int, numbers))) #print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10].  int is a function
# reduce is python2.7
# def addreducelist(a, b):
# 	return a + b
# print(reduce(addreducelist, range(1,6))) #print 15
from math import pi as PIE
print(tuple("My_Python")) #print ('M', 'y', '_', 'P', 'y', 't', 'h', 'o', 'n')
print(tuple((1,2,3))) #print (1, 2, 3)
print(tuple( ['G','N','U'] )) #print ('G', 'N', 'U'). List becomes a tuple
print(list(range(10))) #print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list("23456")) #print ['2', '3', '4', '5', '6'].  Separates each string character into a list with elements
print(list((1,2,3,4))) #print [1, 2, 3, 4].  Tuple becomes a list.
print(str(True)) #print True
print(str("1234567")) #print 1234567
print(str(PIE)) #print 3.141592653589793
print(bool(1>3)) #print False boolean returns True or False
print(bool('a' < 'v')) #print True boolean returns True or False
print(bool(1==1)) #print True boolean returns True or False
print(int(456)) #print 456
print(int("453")) #print 453 converts string to integer
#print(int( [567] )) #error message because can't convert a list to an integer
print(float(PIE)) #print 3.141592653589793
print(float("1.474")) #print 1.474
print(float(508)) #print 508.0
#set an unordered list of unique elements, final result is a list with no duplicates
list_ = [1,1,1,2,3,4,4,4]
print(set(list_)) #print {1, 2, 3, 4}
my_set = set()
my_set.add(5)
my_set.add(1)
my_set.add(2)
print(my_set) #print {1, 2, 5}
my_set.update([11,1,6,8])
print(my_set) #print {1, 2, 5, 6, 8, 11}
print(list(my_set)) #print [1, 2, 5, 6, 8, 11] as a list
#any, all take a list return True or False
print(any([True, False, 0, 1 < 0])) #print True
print(any([False])) #print False
print(any([])) #print False
print(all([True, True])) #print True
print(all([True, 34<5])) #print False
#dir
import os
#print(dir(os)) #uppercase are constants, underscores begin and end are Python built-in variables, leading underscores we shouldn't touch, rest are functions or classes
#print(os.__all__) #tells us what we should be using
print(dir(str))
#input get user input.  Try to get you a number.
#input_ = input("Enter a number: ")
#print("Number is",input_)  #print Number is |input_|
#eval evalulates a string like a math equation
foo = 34
bar = 3
print(eval("foo * bar")) #print 102.  34*3=102
print("\n")

def square(x):
	return x*x
print(square(99)) #print 9801
squarelambda = lambda x: x*x
print(squarelambda(99)) #print 9801
def sumrgb(r, g, b):
	return r + g + b
print(sumrgb(45, 56, 87)) #print 188
sumrgb = lambda r, g, b: r + g + b
print(sumrgb(45, 56, 87))
def functionname(yes, no):
	return yes, no
print(functionname("hi","beering")) #print ('hi', 'beering')
functionname = lambda yes, no: print(yes, no)
functionname("hi","beering") #return hi beering
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
print("\n")

class Boat():
	def __init__(self):
		self.cargoweight = 23
	def printcargoweight(self):
		return self.cargoweight
myboat = Boat()
myboat2 = Boat()
print(myboat) #print <__main__.Boat object at 0x7f696b691160>
print(myboat2) #print <__main__.Boat object at 0x7f42f4f621d0>
print(myboat.printcargoweight()) #print 23
class Human():
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender	
	def printname(self):
		return self.name
	def speakname(self):
		print("My name is %s" % self.name)
	def speak(self, text):
		print(text)
	def performmathtask(self, mathoperations, *args):
		print("%s performed a math operation and the result was %f" % (self.name, mathoperations(*args))) #mathoperations is calling the functions outside class
def mathoperationsadd(a, b):
	return a + b
def mathoperationsmultiply(a, b):
	return a * b
will = Human("nameWilliam","gendermale")
print(will.name) #print nameWilliam
print(will.gender) #print gendermale
print(will.printname()) #print nameWilliam
will.speakname() #print My name is nameWilliam
will.speak("text is I love programming") #print text is I love programming
ryan = Human("nameRyanStevens","gendermale")
ryan.performmathtask(mathoperationsadd, 34, 67) #return nameRyanStevens performed a math operation and the result was 101.000000
ryan.performmathtask(mathoperationsmultiply, 34, 67) #return nameRyanStevens performed a math operation and the result was 2278.000000
class Rectange():
	def __init__(self, width, length):
		self.wnewvariable = width
		self.lnewvariable = length
	def area(self):
		return self.wnewvariable * self.lnewvariable
	def perimeter(self):
		return (self.wnewvariable * 2) + (self.lnewvariable * 2)
rectangle1 = Rectange(5, 6)
rectangle2 = Rectange(2, 10)
#print(rectangle1.width) #error message
print(rectangle1.wnewvariable) #print 5
print(rectangle1.area()) #print 30
print(rectangle2.perimeter()) #print 24
class Character():
	totalnumberofcharacters = 0 #class variable or static variable
	maximumhealth = 100
	def __init__(self,name):
		self.name = name
		self.health = Character.maximumhealth
		Character.totalnumberofcharacters += 1
bob = Character("Bob")
ryan = Character("Ryan")
print(bob.health) #print 100
print(Character.totalnumberofcharacters) #print 2
print(Character.maximumhealth) #print 100

