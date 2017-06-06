#williamfiset 6 Lists 1 of 2, 7 Lists 2 of 2, 18 Functions 2 of 6 Global

#lists are collections of elements, data, or information

listsl = [1,2,3,4,5,6]
print(listsl) #print [1, 2, 3, 4, 5, 6]
print("The length of the list is", len(listsl)) #print The length of the list is 6
listsl.insert(0,100) #insert at position 0 number 100
print(listsl) #print [100, 1, 2, 3, 4, 5, 6]
listsl.remove(5) #remove the list item number 5
print(listsl) #print [100, 1, 2, 3, 4, 6]
cansaveinvariable = listsl.pop() #removes an item in a list, default is the last element
print(listsl) #print [100, 1, 2, 3, 4]
print(cansaveinvariable) #print 6
cansaveinvariable = listsl.pop(0) #removes first item in a list
print(listsl) #print [1, 2, 3, 4]
print(cansaveinvariable) #print 100

items = ["cat","dog","moon","shoe"]
print(items[0]) #print cat
print(items.index("cat")) #print 0
items[1] = "parrot" #replace first element dog with parrot
print(items) #['cat', 'parrot', 'moon', 'shoe']
items.append("door") #add to the items' list
print(items) #['cat', 'parrot', 'moon', 'shoe', 'door']

items = ["cat","dog","moon","shoe","cat"]
print("Cat appeared",items.count("cat"),"times.") #print Cat appeared 2 times.  Count number of times an element appears.
items.sort()
print(items) #print ['cat', 'cat', 'dog', 'moon', 'shoe]

#print["key"] + items #python2.7 square brackets to add to front of items' list
#print(items)

#slicing, take a list and cut it.  Extract a subset of a list.
print("-----slicing-----")
a = [11,22,33,44,55,66,77,88]
b = ["|||"]
c = ("a","b","c") #tuple, a immuterable list, doesn't change, no assigning
bars = b * 4
print(bars) #print ['|||', '|||', '|||', '|||']
print(''.join(bars)) #print ||||||||||||  String concatenation tip
print(a[3]) #print 44
print(a[2:5]) #print [33, 44, 55]
print(a[0:len(a)]) #print [11,22,33,44,55,66,77,88] another way to print the entire list
print(a[-1]) #print 88
print(a[-8]) #print 11
print(a[1::2]) #print [22, 44, 66, 88] start index:end index:step up or step down.  Blank is default
print(a[::-1]) #print [88, 77, 66, 55, 44, 33, 22, 11] start index:end index:step up or step down.  Blank is default
print(c[2]) #print c

# print[1,2,3,4,5,6,7,8][2:7] #only works for Python2.7 [3, 4, 5, 6, 7]
# print(1,2,3,4,5,6,7,8)[1:5] #only works for Python2.7 (2, 3, 4, 5)

def common_start_end_lists(list1, list2):
	starts_match = list1[0] == list2[0]
	ends_match = list1[-1] == list2[-1]
	return starts_match and ends_match
print(common_start_end_lists([1,4,6,3],[1,57,3])) #print True
print(common_start_end_lists([0,4,6,3],[1,57,3])) #print False