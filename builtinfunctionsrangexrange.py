#williamfiset 28 Builtins 3 of 6 range vs xrange

# len, sorted, range, xrange (lazy range says instructor)

unordered_numbers = [1,7,3,7,2,4,0,2,-2,5,3]
unordered_characters = ["r","t","©","v","s","b"]
unordered_strings = ["cat","dog","mice"]
unordered_dictionary = [{2:"two",1:"one",4:"four"}]
print(sorted(unordered_numbers)) #print [-2, 0, 1, 2, 2, 3, 3, 4, 5, 7, 7]
print(sorted(unordered_characters)) #print ['b', 'r', 's', 't', 'v', '©']
print(sorted(unordered_strings))  #print ['cat', 'dog', 'mice']
print(sorted(unordered_dictionary)) #print [{1: 'one', 2: 'two', 4: 'four'}]
print(sorted("hello world!")) #print [' ', '!', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']; broke string into a list, then sort characters in the list individually

#reverse is originally set to False; i.e. reverse = False is default
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

for num in range(100):
	print(num) #prints 0 to 99 for each number in each individual line.  Range returns a list.

# xrange() no longer exists in python 3.5.  Gives you the numbers as you need them.  You can break a for loop below at, say 50, and it gives you the 50.
# for num2 in xrange(100):
# 	print(num2)