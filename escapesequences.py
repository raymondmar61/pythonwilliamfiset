print("Hello World!")
print("Hello\nWorld!") #\n creates a new line
print("\"Hello World!\"")
print("Hello\\ \"World!\"")
#print(""Hello World!"") #syntax error
print("Hello\f World!") #\f foam feeder, creates a new line and new "column"
print("\b")

hw = list("Hello World") #create a list of collection, elements from a string
print(hw)
hwjoin = "\f".join(hw)
print(hwjoin)
hwtab = "\t".join(hw) #\t tab out
print(hwtab)

print("Hello\rWorld") #\r line feed.  I don't see the advantage.
print("Hello\rWorld Peace") #\r line feed.  I don't see the advantage.  It's like a don't print on the left of \r?
print("Hello\tWorld") #\t tab out