def add_ten(num):
	return num + 10

def double(num):
	return num * 2

def triple(num):
	return num * 3

number = 3

# tripled = triple(number)
# doubled = double(tripled)
# result = add_ten(doubled)

#embed calling a function combine the three variables into one
#sometimes embed can be confusing.  Instructor says it's the programmer's call to embed or not embed.
result = add_ten(double(triple(number)))
print(result)
