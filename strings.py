# print[1,2,3,4,5,6,7,8][2:7] #only works for Python2.7 [3, 4, 5, 6, 7]
# print(1,2,3,4,5,6,7,8)[1:5] #only works for Python2.7 (2, 3, 4, 5)
# we can slice a string like slice a list
# print("hello World!")[0:6] #only works for Python2.7 hello
# print("hello World!")[2] #only works for Python2.7 l
# print("hello World!")[::2] #only works for Python2.7 hloWrd
# print("hello World!")[::-1] #only works for Python2.7 !dlroW olleh

#INSTRUCTOR SAYS GO TO PYTHON DOCUMENTATION TO SEE PYTHON BUILT-IN FUNCTIONS
#DON'T REINVENT THE WHEEL

#williamfiset 8 Strings, 9 String Formatting, 10 Escape Sequences, 17 Functions 1 of 6 Intro, 18 Functions 2 of 6 Global, 

s = "do goat sheep boat"
print(s.split())  #print as a list ['do', 'goat', 'sheep','boat']
split_s = s.split()
print(split_s) #print as a list ['do', 'goat', 'sheep','boat'] from a variable
s = "do/goat/sheep/boat"
split_s = s.split("/")
print(split_s) #prints as a list ['do', 'goat', 'sheep','boat'] from a variable
replace_s = s.replace("boat","yoga")
print(replace_s) #print do/goat/sheep/yoga from a variable
upper_s = s.upper()
print(upper_s) #print DO/GOAT/SHEEP/BOAT from a variable
s = "DO GOAT SHEELP BOAT"
print(s.lower()) #print do goat sheelp boat
wheregoat = s.find("GOAT")
print("GOAT is at",wheregoat,"position") #print GOAT is at 3 position

hw = "hello world"
if hw.startswith("hello"):
	print("hw starts with hello")

user_input = input("Please enter a string: ") #raw_input() is python2.7?
if user_input.startswith("hello"):
	print("User enters \"hello\"")
elif user_input.endswith("!"):
	print("You ended with !")
else:
	print("Please type 'hello' next time")

joinstring = ["1","2","3","4"]
joinwithwhat = " "
joinstring = joinwithwhat.join(joinstring)
print(joinstring) #print 1 2 3 4
joinstring = ["1","2","3","4"]
print(joinstring) #print ['1', '2', '3', '4']
print("-".join(joinstring)) #print 1-2-3-4

capitalizefirstword = "general"
print(capitalizefirstword.capitalize()) #print General
capitalizefirstword2 = "colonel"
capitalizefirstword2 = capitalizefirstword2.capitalize()
print(capitalizefirstword2) #print Colonel

#Python documentation; e.g. string.capitalize() or mywords stringsavedasvariable.function()

number = 345436
hex_ = 0x33 #51
exp = 1e6
print(hex_) #print 51 
print(exp) #print 1000000.0
print(int(exp)) #print 1000000

a_Str = "The String"
a_num = 457
print("My number is",a_num,"my string is",a_Str) #print My number is 457 my string is The String
#print("My number is "+a_num+" my string is" +a_Str) #error message Can't convert 'int' object to str implicitly
print("My number is",a_num,"my string is "+a_Str) #print My number is 457 my string is The String
print("My number is %d my string is %s" %(a_num, a_Str)) #print My number is 457 my string is The String
#%d decimal base 10 or integer, %s string, %f float
print("My number is {0} my string is {1}".format(a_num, a_Str))
print("My number is {0} my string is {1} {2}".format(int(a_num), a_Str, a_num))

print("Hello\nWorld!") #print Hello\n World!
print("\"Hello World!\"") #print "Hello World!"
print("Hello\\World!") #print Hello\World!
print("Hello\fWorld!") #print Hello
								  #World!
#\f foam feeder, creates a new line and new "column"
stringvariable = list("Hello World")
print(stringvariable) #print ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
print("\f".join(stringvariable)) #print
#H
# e
#  l
#   l
#    o
#     
#      W
#       o
#        r
#         l
#          d
print("\t".join(stringvariable)) #print H	e	l	l	o	 	W	o	r	l	d
#\t tab out
print("Hello\rWorld") #print World.  \r line feed.  I don't see the advantage.
print("Hello\rWorld Peace") #print World Peace.  \r line feed.  I don't see the advantage.  It's like a don't print on the left of \r.  Carriage return.
print("Hello\tWorld") #print Hello	World  \t tab out

def removevowels(string):
	vowels = "aeiou"
	new_string = ""
	for character in string: #for loop automatically loops over elements in sequences or lists.  Iterate over a sequence.  In this case, string.
		if character not in vowels: #don't print the vowels
			new_string = new_string + character #like x = x + 1 and initialize new_string as nothing.  Saves I in character which is new_string "I".  Saves space in character which is new_string "I ".  Saves l in character which is new string"I l".  No saves o in character.  Saves v in character which is new string "I lv" etc.
	return new_string
text = "I love eating apple pies"
text_without_vowels = removevowels(text)
print(text_without_vowels) #print I lv tng ppl ps

def make_html_tag(text, tag):
	return "<%s>%s</%s>" % (tag, text, tag)
print(make_html_tag("My title","title")) #print <title>My title</title>
print(make_html_tag("Bold","bold")) #print <bold>Bold</bold>