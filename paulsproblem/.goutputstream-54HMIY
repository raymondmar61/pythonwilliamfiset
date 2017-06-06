#paul's problem is lines with "nlu" must be deleted
import os

def remove_text(file_name, text):
	lines = []  #initialize lines stored in a list or an array both same things
	new_lines = [] #initialize new_lines stored in a list or an array both same things

	with open(file_name, "r") as text_file:
		lines = text_file.readlines()
	print(lines) #each text file stores in a list or an array.  "\n" means new line

	for line in lines:
		if text not in line:  #remember text is nlu defined in remove_text()
			new_lines.append(line)

	with open(file_name, "w") as text_file: #remember writes deletes old content and writes new content
		for line in new_lines:
			text_file.write(line)
	print(lines)


#print(os.listdir("./")) #print all files and folders in current directory.
print(__file__) #prints the file name; in my case and maybe python3.5 prints .py file
file_name = __file__ #saves __file__ in variable file_name
files_in_dir = os.listdir("./") #saves in variable files_in_dir
files_in_dir.remove(file_name) #remove paulsproblemdeletelines.py file to not be run in function remove_text()

#for statement opens all files in current directory and runs all files in function remove_text()
for file_ in files_in_dir:
	remove_text(file_, "nlu")