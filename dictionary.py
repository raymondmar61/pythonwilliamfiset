#williamfiset 14 Dictionary

#dictionary or hash map in java.  Give it a key and its value or description.  Key can't be a list; must be unique.  Value or description can be duplicates.  Dictionary are unordered.

peopleages = {"Ryan": 89, "William": 23, "Catherine": 44}

print(peopleages) #print {'Catherine': 44, 'William': 23, 'Ryan': 89}
print(peopleages["Ryan"]) #print 89
print(peopleages.get("Catherine")) #print 44
del peopleages["William"]
print(peopleages) #print {'Ryan': 89, 'Catherine': 44}
peopleages.update({"William Is Back" : 25})
print(peopleages) #print in no particular order {'Catherine': 44, 'Ryan': 89, 'William Is Back': 25}
print("\n")
for key in peopleages:
	print(key) #print Ryan\n William Is Back\n Catherine\n no particular order
for key in peopleages.keys():
	print(key) #print Ryan\n William Is Back\n Catherine\n no particular order
for seven7 in peopleages.values():
	print(seven7) #print 44\n 25\n 89 no particular order
for key in peopleages:
	print(key, ":", peopleages[key]) #print both key and value separated by a colon
for k, v in peopleages.items():
	print(k, ":", v) #more detailed

#check dictionary has a key.  Error message appears
# if peopleages.has_key("john"):
# 	del peopleages["john"]
#or
if "john" in peopleages:
	del peopleages["john"]

# #delete dictionary
# peopleages.clear()
# #or
# peopleages = {}
