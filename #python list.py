#python list,tuple,set,dictionary
#list
listnum = [3,1,4,1,5]
print(listnum[0],listnum[4])
listcolor = ['red','blue','green']
print(len(listcolor))
#append in list
listcolor = ['red', 'blue']
print(listcolor.append('yellow'))
#insert in list
listfruit = ['apple','banana']
print(listfruit.insert(1,'orange'))
#remove in list
listfruit = ['apple','banana','grapes']
print(listfruit.remove('banana'))
#pop the element 
listitem = [20,30,40]
print(listitem.pop(2))
#check
listnum = [1,2,3,4]
present = 3 in listnum
print(present)
#slice in list
listnum = [0,1,2,3,4]
print(listnum[2:4])
#count the value
listnum = [1,2,2,3,2]
print(listnum.count(2))
#replace
listnum = [5,10,15]
listnum[1] = 12
print(listnum)

#tuple
t = (10,20,30)
print(t[1])
#lenght of tuple
t = ('a','b','c')
print(len(t))
#unpack
x,y = (4,5)
print(x)
print(y)
#check
t = ('a','b','c')
present = 'b' in  t
print(present)
#type
t = ()
print(type(t))
#Concatenate into a new tuple
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result) 
#Repeat (7,) three times
my_tuple = (7,)
repeated_tuple = my_tuple * 3

print(repeated_tuple)

#Find the index of 2 in (1, 2, 3, 2).
my_tuple = (1, 2, 3, 2)
result = my_tuple.index(2)
print(result) 

#Count how many times 2 appears in (1, 2, 3, 2)
numbers = (1, 2, 3, 2)
result = numbers.count(2)
print(result)

#Create a single‑element tuple containing the value 5
single_element_tuple = (5,)
print(single_element_tuple)

#Python sets
#Create a set from a list
my_list = [1, 2, 2, 3]
my_set = set(my_list)
print(my_set)

#Add an element to a set
s = {1, 2, 3}
s.add(4)
print(s)

#Remove an element from a set
s = {1, 2, 3}
s.remove(2)
print(s)

#Check membership in a set
s = {1, 3, 5}
is_present = 5 in s
print(is_present)

#Find the length of a set
s = {10, 20, 30}
print(len(s))

#Clear all elements from a set
s = {1, 2, 3}
s.clear()
print(s)

#Conditional addition to a set
s = {'a', 'b'}
if 'c' not in s:
    s.add('c')
print(s)

#Remove duplicates using set casting
char_list = ['a', 'a', 'b']
unique_set = set(char_list)
print(unique_set)

#Union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)

#Intersection of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 & set2)


# Python Dictionaries

# Create a dictionary and print the name
d = {'name': 'Ali', 'age': 25}
print(d['name'])

# Add the key 'city': 'Lahore'
d['city'] = 'Lahore'
print(d)

#Change 'age' to 30
d = {'name': 'Ali', 'age': 25}
d['age'] = 30
print(d)

#Delete Key 'age'
d = {'name': 'Ali', 'age': 30}
del d['age']
print(d)

#Check if Key 'salary' Exists
d = {'name': 'Ali', 'age': 30}
exists = 'salary' in d
print(exists)

#Print All Keys
d = {'a': 1, 'b': 2}
print(d.keys())

#Print All Values
d = {'a': 1, 'b': 2}
print(d.values())

#Iterate and Print Key-Value Pairs
d = {'x': 10, 'y': 20}
for k, v in d.items():
    print(f"Key: {k}, Value: {v}")

#Safely Read Key with get()
d = {}
score = d.get('score', 0)
print(score)

#Create a Dictionary from Two Lists
keys = ['a', 'b']
values = [1, 2]
d = dict(zip(keys, values))
print(d)
