#williamfiset 29 Builtins 4 of 6 rBuiltins Functional Tools

#run the examples python2.7

#filter to filter out elements in a list, reduce to combine something, map to apply a function everywhere

def add(a,b):
	return a + b

def keepvowel(character):
	return character.lower() in ('a','e','i','o','u')

words = ['visions','of','Infinity','pythOn','squirrel']

print reduce(add, words) #print visionsofInfinitypythOnsquirrel.  Combine list "words" in one string no spaces
print list(reduce(add, words)) #print ['v', 'i', 's', 'i', 'o', 'n', 's', 'o', 'f', 'I', 'n', 'f', 'i', 'n', 'i', 't', 'y', 'p', 'y', 't', 'h', 'O', 'n', 's', 'q', 'u', 'i', 'r', 'r', 'e', 'l'].  Combine list "words" in one list, each letter its own individual element
print filter(keepvowel, list(reduce(add,words))) #print ['i', 'i', 'o', 'o', 'I', 'i', 'i', 'O', 'u', 'i', 'e'] #instructor didn't catch error upper vowels included
#print filter(keepvowel, list(reduce(add,words).lower())) #solution to error
print len (filter(keepvowel, list(reduce(add,words)))) #print 11