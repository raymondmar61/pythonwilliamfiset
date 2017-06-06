#williamfiset 30 Builtins 5 of 6 Types

# tuple, list, str, bool, int, float
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
print("\n")

my_set = set()
my_set.add(5)
my_set.add(1)
my_set.add(2)
print(my_set) #print {1, 2, 5}
my_set.update([11,1,6,8])
print(my_set) #print {1, 2, 5, 6, 8, 11}
print(list(my_set)) #print [1, 2, 5, 6, 8, 11] as a list