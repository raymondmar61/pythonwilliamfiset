#opens a file in a mode.  Read reads only "r".  Write erases contents and start from scratch "w".  Append adds lines content to the bottom "a".  Read & write.  Open in binary mode.  Instructor shows read, write, append, read+, and read write.
#instructor recommends using the with syntax which automatically close file

#create a file.  File extension can be created originally.
file_name = "example.txt"
#open a file
example_file = open(file_name, "w")
#write a file with try:
try:
	example_file.write("Blue Goose on the loose\n")
	example_file.write("Honeycomb cereal\n")
except Exception as error:
	print("Problem handling file, error was", error)
finally:
	example_file.close()

#files.py successfully ran.  example.txt file created in present directory.

#better way to create, open, and write using with
with open(file_name, 'w') as example_file2:
	lines = ["Happy whale on parade!\n", "Red Bee dancing\n","The great gig in the sky!\n"]
	# example_file2.write(lines[0])
	# example_file2.write(lines[1])
	# example_file2.write(lines[2])
	example_file2.writelines(lines) #faster than example_file2.write() statements
	#example_file2.close() #redundant.  with syntax closes file

#read a file
with open(file_name, "r") as reading_file:
	for line in reading_file.readlines():
		print(line)
#successfully ran.  Printed the lines in terminal.	

#read a file another way
with open(file_name, "r") as reading_file:
	text = reading_file.read()
	print(text)
#successfully ran.  Printed the lines in terminal.

#better way to create, open, and write using with
with open(file_name, 'w') as example_file2:
	lines = ["Happy whale on parade!\n", "Red Bee dancing\n","The great gig in the sky!\n"]
	example_file2.writelines(lines)

#characters are uppercase and lowercase sequentially
new_content = [] #initialize new_content as an empty list--an array
file_content = ""
with open(file_name,"r") as reading_file3:
	file_content = reading_file3.read()
	print(new_content)
counter = 0
for character in file_content:
	#Gets every other character
	if counter %2 == 0:
		new_content.append(character.upper())
	else:
		new_content.append(character.lower())
	counter +=1
	print(new_content)
new_content = "".join(new_content) #take each character and join togehter instead of each character in its own line
print(new_content)
#write new_content[] uppercase and lowercase into file_name = example.txt
with open(file_name,"w") as writeable_file:
	writeable_file.write(new_content)

#append mode
print(new_content) #using new_content above
with open(file_name, "a") as appending_file:
	for char in new_content:
		appending_file.write(char)