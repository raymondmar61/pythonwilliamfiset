#williamfiset 16 A Module Overview

import math
import string
import random
#import time # don't need "import time" when I import using "from time import . . . "

words = "Hello World how are you?"
print(words.split()) #print ['Hello', 'World', 'how', 'are', 'you?']

print(dir(random)) #print random constants and functions 
print("Functions that begin with one understore they exist in standard library, but I prefer you don't touch them.")
print("Functions that begin and end with two understores are defined by Python.  For example, print(random.__all__) means all functions in the module random to use.")
print(random.__all__)
print("\n")
print(random.random()) #print a number between 0 and 1
print(random.randint(1, 10)) #print a number between 1 and 10

from time import timezone as dontcarenow
print(dontcarenow)

from sys import *
print(argv) #didn't need to type "sys.argv" because I used "from sys import *" instead of "import sys"