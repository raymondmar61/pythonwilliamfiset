#for loop simpiler and more powerful says instructor

list_ = [1,2,3,4,5,6,7,8,9,10]
print (list_)
print ("The length of list_ is", len(list_),"and the highest index is 9.")

#range(start, stop-1, increment) Python 2.7; however, documentation shows it works for Python 3.5 yet print(range()) specifically doesn't work
listrange = range(1,11,2)
print(listrange)
#print(list(range())) works according to Python documentation
print(list(range(1,11,2)))

#while loop multiple list_ by two
index = 0
while index < len(list_):
	print(int(list_[index]) * 2)
	index += 1

#for loop multiple list_ by two
#instructor says for loops better looping over elements in sequences or lists.  Iterate over a sequence.
for element in list_:
	print (element * 2)
	pass

#for loop in detailed:
for elementdetailed in [1,2,3,4,5,6,7,8,9,10]: #elementdetailed variable takes one at a time each data in the list in order:  starts with 1, then 2, then 3, then 4, . . . .	
	print(elementdetailed)

#simple examples
for char in "String":
	print(char)

for letter in "String":
	print(letter)

for data in range(0,10,2):
	print(data)

for nameyourvariablehere in "Raymond":
	print(nameyourvariablehere)

pi = 3.141592
for digit in str(pi):
	if digit != ".": #don't print the decimal
		print(digit)