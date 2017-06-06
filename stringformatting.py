number = 345436
hex_ = 0x33 #51
exp = 1e6

print(hex_)
print(exp)
print(int(exp))

astring = "The String"
anumber = 457.75

print(astring,anumber)
print("My number is",anumber,". My string is " +astring)
print("My number is %d. My string is %s." % (anumber,astring)) #%d decimal base 10 or integer, %s string, %f float
print("My number is {0}. My string is {1}.".format(anumber, astring))
print("My number is {0}. My string is {1}. {2}".format(int(anumber), astring, anumber))

