# apples = 10
#example of two independent if statements.  Both are true.  Both printed.
# if apples > 3:
# 	print("I have more than three apples!")
# if apples > 5:
# 	print("I have more than five apples!")

apples = 10
if apples > 6:
	print("I have more than six apples!")
elif apples <= 0:
 	print("You have less than zero apples!")
else:
	print("You have another amount of apples")

fruits = 12
if fruits == 12: #single = is assigning a variable; double == is comparsion
	print(12 * "12 ")

dollars = 139
#one way
if dollars >= 100 and dollars <= 200:
	print("Right amount of money")
#second way
if dollars >= 100:
	if dollars <= 200:
		print("Right amount of money")
#third way
if 100 <= dollars <=200:
	print("Right amount of money")

location = "home"
if location =="vegas" or location == "home":
	print("Somewhere nice")

a = 33
t = 22
if a == 33 and not (t == 22):
	print("...")
else:
	print("Not equal")
if (a == 33 and not (t == 22)) or ("baby" == "baby"):
	print("...")
else:
	print("Not equal")