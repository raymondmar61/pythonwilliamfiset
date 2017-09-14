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
