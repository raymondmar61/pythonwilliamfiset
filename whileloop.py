#while loop.  Repeat an operation.  Condition is true, go while loop.  Condition is false, stop while loop.

#basic loop below:  initialize, while loop with condition, body
# num = 0
# while num <= 10:
# 	print(num) 
# 	num +=1 #same as num = num + 1

#Infinite Loop
#Shortcut keys 0 = False, 1 = True
# while True:
# 	print("Will execute forever")

stars = ""
while len(stars) <=10:
	#pass #it means don't do anything, skip, ignore, don't make it crash
	print(stars)
	stars = stars + "*"

#even number of stars
stars = ""
while len(stars) <=10:
	if len(stars) % 2 == 0:
		print(stars)
	stars = stars + "*"

#odd number of stars
stars = ""
while len(stars) <=10:
	if len(stars) % 2 != 0:
		print(stars)
	stars = stars + "*"

while len(input("Enter name that has at least five characters: ")) <5:
	print("That name didn't have at least five characters?")
print("That name has at least five characters")
