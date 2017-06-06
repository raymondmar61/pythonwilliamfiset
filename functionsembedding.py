def add_ten(num):
	return num + 10

def double(num):
	return num * 2

def triple(num):
	return num * 3

number = 3

tripled = triple(number)
doubled = double(tripled)
result = add_ten(doubled)

print(result)
