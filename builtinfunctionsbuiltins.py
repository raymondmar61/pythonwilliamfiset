#williamfiset 31 Builtins 6 of 6 Builtins

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
input_ = input("Enter a number: ")
print("Number is",input_)  #print Number is |input_|

#eval evalulates a string like a math equation
foo = 34
bar = 3
print(eval("foo * bar")) #print 102.  34*3=102