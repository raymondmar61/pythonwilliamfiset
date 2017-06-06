# valid for python2.7
# import __builtin__
# print(dir(__builtin__))
#BTW, True and False are a builtin

# valid for python3.5
import builtins
print(dir(builtins))
#BTW, True and False are a builtin

#min, max, pow, abs
from math import fabs

print(fabs(-4)) #float absolute? not a built in need to import math module
print(fabs(-4.6))
print(abs(-4))
print(abs(-4.6))

list_ = [1,77,33,55]
print(max(list_))
print(min(list_))

list_letters = ["a","y","f","h"]
print(min(list_letters))
print(max(list_letters))

print(6**78)
print(pow(6, 78))
