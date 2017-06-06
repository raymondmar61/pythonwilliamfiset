#williamfiset 44 Generators

#generator is a way to output a sequence of values without actually having to hold those values in memory like an array.  You can't iterate backwards onto them or reset them.  If you want to iterate or rest, you create another generator.

for n in range(0,10):
	print(n) #print 0-9 in its own line

generator = iter(range(0,10))
print(generator) #print <range_iterator object at 0x7f9e4f216db0>
print(next(generator)) #print 0
print(next(generator)) #print 1
print(next(generator)) #print 2
print(next(generator)) #print 3
print(next(generator)) #print 4
print(next(generator)) #print 5

generatorreverse = iter(reversed(("abcde")))
print(next(generatorreverse)) #print e
print(next(generatorreverse)) #print d
print(next(generatorreverse)) #print c
print(next(generatorreverse)) #print b 
print(next(generatorreverse)) #print a

#a generator can have an ending:  runs out of elements or generate indefinitely	
#Type return keyword to exit out of the generator.  Another key word is needed to return generated elements.  Use yield keyword.
#Fibonacci series 1 1 2 3 5 8 13 21 . . .
def fibonacci_generator():
	a, b = 1, 1 #I think he meant a = 1 and b = 1
	print("yield a is" ,a) #prints yield a is 1; prints before 
	print("yield b is" ,b) #prints yield b is 1; prints before 
	yield a
	yield b
	while True:
		yield a + b #yield returns 2 or 1 + 1 during first while loop rotation
		a, b = b, a + b #I think he meant a = b and b = a + b		
g = fibonacci_generator()
print(next(g)) #prints yield a is 1\n yield b is 1\n 1\n
print(next(g)) #prints 1
print(next(g)) #prints 2
print(next(g)) #prints 3
print(next(g)) #prints 5
print(next(g)) #prints 8
print(next(g)) #prints 13

#Fibonacci series2 1 1 2 3 5 8 13 21 . . .
def fibonacci_generator2():
	a, b = 1, 1 #I think he meant a = 1 and b = 1
	print("yield a is" ,a) #prints yield a is 1; prints before 
	print("yield b is" ,b) #prints yield b is 1; prints before 
	yield a
	yield b
	while True:
		yield a + b #yield returns 2 or 1 + 1 during first while loop rotation
		a = b
		b = a + b #I think he meant a = b and b = a + b		
g2 = fibonacci_generator2()
print(next(g2)) #prints yield a is 1\n yield b is 1\n 1\n
print(next(g2)) #prints 1
print(next(g2)) #prints 2
print(next(g2)) #prints 3
print(next(g2)) #prints 6
print(next(g2)) #prints 12
print(next(g2)) #prints 24

squares = (x * x for x in range(10))
print(squares) #print <generator object <genexpr> at 0x7f6063d63af0> because we are generating instead of a list
squares = [x * x for x in range(10)]
print(squares) #print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
squares = (x * x for x in range(10))
print(next(squares)) #print 0
print(next(squares)) #print 1 
print(next(squares)) #print 4 
print(next(squares)) #print 9 
print(next(squares)) #print 16 
for elements in squares:
	print(elements) #prints the rest of squares 25, 36, 49, 64, 81 in its own line.  Interesting the for loops didn't begin printing from 0, 1, 4, . . . .  for loop is another way to access elements in a generator.  for loop tries to exhaust the generator until there are no more elements.


#method
def isprime(n):
	if n < 2: return False
	elif n in (2,3): return True
	elif n % 2 == 0 or n % 3 == 0: return False
	root = int(n**0.5) + 1
	for f in range(5, root, 6):
		if n % f == 0 or n % (f + 2) ==0:
			return False
	return True

def primenumber_generator():
	yield 2
	n = 3
	while True:
		if isprime(n):
			yield n
		n+=2 #all prime numbers are odd except 2.  Add two when a number is not prime.
# run primenumber_generator() in a for loop, it runs forever because there's an infinite number of prime numbers
# for p in primenumber_generator():
# 	pass
p = primenumber_generator()
print(next(p)) #print 2
print(next(p)) #print 3
print(next(p)) #print 5
print(next(p)) #print 7
print(next(p)) #print 11

#itertools module. Iterator.
from itertools import *
for perm in permutations('ABCDEF'):
 	print(perm)
print("\n")
for perm in combinations('ABCDEF',4):
 	print(perm)