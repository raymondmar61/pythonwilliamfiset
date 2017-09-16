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
