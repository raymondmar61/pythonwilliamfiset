#williamfiset 4 Conditionals 1 of 2, 5 Conditionals 2 of 2

# apples = 10
#example of two independent if statements.  Both are true.  Both printed.
# if apples > 3:
# 	print("I have more than three apples!")
# if apples > 5:
# 	print("I have more than five apples!")

apples = 10
if apples > 6:
	print("I have more than six apples!") #print I have more than six apples!
elif apples <= 0:
 	print("You have less than zero apples!")
else:
	print("You have another amount of apples")

fruits = 12
if fruits == 12: #single = is assigning a variable; double == is comparsion
	print(12 * "12 ") #print 12 12 12 12 12 12 12 12 12 12 12 12

dollars = 139
#one way
if dollars >= 100 and dollars <= 200:
	print("Right amount of money")
#second way
if dollars >= 100:
	if dollars <= 200:
		print("Right amount of money")
#third way
if 100 <= dollars <= 200:
	print("Right amount of money")

if 12 != 13:
	print("yes 12 and 13 are different !=.  <> invalid not equal python 3.5")
# if 12 <> 13:
#  	print("yes 12 and 13 are different <>.  If statement works python2.7.")

location = "home"
if location =="vegas" or location == "home":
	print("Somewhere nice")

a = 33
t = 22
if a == 33 and not (t == 22):
	print("...")
else:
	print("Not equal") #print Not Equal
if (a == 33 and not (t == 22)) or ("baby" == "baby"):
	print("...")
else:
	print("Not equal") #print ...
if a == 33 or t == 11:
	print("True") #print True
else:
	print("False")