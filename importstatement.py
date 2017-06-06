#williamfiset 15 Math Module, 16 A Module Overview

#the import statement get code that Python already provided us with.  In this case, we're using the math module.
#Google "Python Math" to find the Python documentation for math functions

# import math
# from math import sin, pi
# num = 5.6
# print(math.ceil(num)) #print 6
# print(math.floor(num)) #print 5
# print(math.factorial(math.floor(num))) #print 120.  Factorial() only accepts integral values.  Need to math.floor num.
# print(math.exp(2)) #print 7.38905609893065 which is e^2
# print(math.pow(2,4)) #print 16.0 which is 2^4
# print(math.log(16,2)) #print 4.0
# print(math.sin(math.pi * 2)) #print -2.4492935982947064e-16
# print(sin(math.pi * 2)) #print -2.4492935982947064e-16
# print(sin(pi * 2)) #print -2.4492935982947064e-16

# import math
# from math import pi as PIE
# print(math.pi) #print 3.141592653589793
# print(PIE) #print 3.141592653589793
# print(math.degrees(PIE*2)) #print 360.0

from math import pi as PIE
print(PIE) #print 3.141592653589793

import math
print(dir(math)) #print math constants and functions
print(math.__name__) #print math
print(math.__doc__) #print This module is always available.  It provides access to the mathematical functions defined by the C standard.
print(math.sqrt) #print <built-in function sqrt>