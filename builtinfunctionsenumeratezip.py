#enumerate, zip

numbers = ["one","two","three","four"]
seasons = ["fall","winter","spring","summer"]

#assign a numerical value to elements in a list.  list() to make enumerate readable
print(enumerate(numbers, start=0)) #start=0 is default, no need to type
print(list(enumerate(numbers, start=0))) #start=0 is default, no need to type
print(enumerate(seasons, start=0)) #start=0 is default, no need to type
print(list(enumerate(seasons, start=0))) #start=0 is default, no need to type


#We know enumerate, we don't need the counter=0 initialization in the for loop
file_name = "example2.txt"
#characters are uppercase and lowercase sequentially
file_content = ""
with open(file_name,"r") as readable_file:
	file_content = readable_file.read()
	print(file_content)

new_content = [] #initialize new_content as an empty list--an array
for counter, character in enumerate(file_content): #counter is the number in enumerate, character is the letter in file_content; e.g. (0, 'H'), (1, 'A'), (2, 'P'), (3, 'P'), (4, 'Y'), . . . (counter, 'character')
	#Gets every other character
	if counter %2 == 0:
		new_content.append(character.upper())
	else:
		new_content.append(character.lower())
	print(new_content)
new_content = "".join(new_content) #take each character and join togehter instead of each character in its own line
print(new_content)

#zip combine two lists into one matching index list one to index list two
print(zip(numbers,seasons))
print("Combine two lists into one matching index list one to index list two")
print(list(zip(numbers,seasons)))
for numbers, season in zip(numbers, seasons):
	print("The present " +season+ " is number in string format " +numbers)