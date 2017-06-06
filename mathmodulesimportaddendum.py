#the import statement get code that Python already provided us with.  In this case, we're using the math module.
#Google "Python Math" to find the Python documentation for math functions

# import math

# num = 5.6
# print(math.ceil(num))
# print(math.floor(num))

# print(math.factorial(4))
# print(math.pow(2,4))
# print(2**4)
# print(math.exp(2))
# print(math.log(16,2))

# print(math.sin(6.28))
# print(math.sin(math.pi*2))

# four = math.sqrt(4)
# print(four)

#tired of typing "math."?  Obviously these are math functions.
#type "from math import *" which means don't specify where functions came from; assumed already written "math."  import * means import all functions; in this case math functions readily accessable
# from math import *

# num = 5.6
# print(ceil(num))
# print(floor(num))

# print(factorial(4))
# print(pow(2,4))
# print(2**4)
# print(exp(2))
# print(log(16,2))

# print(sin(6.28))
# print(sin(pi*2))

# four = sqrt(4)
# print(four)

#imported all math functions from Python module
#in particular, we noted we imported sin.  No need for "math.sin.""  Just ".sin"
#however, we must note "math." for the rest of the math functions
#we can rename Python function; e.g. give "ceil" a new name "roundup"
import math
# from math import sin, pi, ceil as roundup

# num = 5.6
# print(math.ceil(num))
# print(roundup(num)) #renamed math.ceil as roundup or math.ceil=roundup
# print(math.floor(num))

# print(math.factorial(4))
# print(math.pow(2,4))
# print(2**4)
# print(math.exp(2))
# print(math.log(16,2))

# print(sin(6.28)) #no need for "math." for sin because we noted from import
# print(sin(pi*2)) #no need for "math." for pi because we noted from import

# four = math.sqrt(4)
# print(four)

# print(math.degrees(pi * 2)) #a circle 360.0 degrees

#we can find all the functions in a module
#in this case, math module
print(dir(math))
print(math.__name__)
print(math.__doc__)
print(math.__spec__)