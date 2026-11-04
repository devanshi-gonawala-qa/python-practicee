# 02/11/2026
d = {} #its[dictonary] store in {}
print(type(d))

# another way to write dict
d = dict()
print(type(d))

a = 'a'
d = {a : 1, 'b' : 2}
print(d)

# d = {[1,2,3,4] : '1'}
# print(d)

d = {(1,2,3,4) : '1'}
print(d)

d = {2: '1'}
print(d)

nicknames = {"Madhuri" : "Sweety",
             "Vinoth" : "Appu", 
             "Kusum" : "ku ku",
             "Aakar" : "Golu"}
# print(nicknames[0]) #its cannot indexing because indexing not support
print(nicknames["Madhuri"]) 
print(nicknames["Aakar"])

# print(nicknames['avd'])
print(nicknames.get("kusum"))

print(nicknames.get('abv', 'Not Present'))
# Intserting values in Dictionary
a = {True: 'a', 'a' : 1, 2:False, 3.14: 'pi'}
a[True] = 'b'
print(a)

a[False] = 12
print(a)

# Updating value from the dictionary using a key
nicknames['Kusum'] = 'New Value'
print(nicknames)
# Length of Dictionary
print(len(nicknames))

# Delete a key from a Dictionary
del nicknames['Aakar']
print(nicknames)
print(len(nicknames))

# pop function 
print(nicknames.pop('Vinoth'))
print(nicknames)
print(len(nicknames))

print(nicknames.pop('Vinoth', 'Default value'))
# Get keys and value of dictionary
nicknames = {"Madhuri" : "Sweety",
             "Vinoth" : "Appu", 
             "Shubham": "Zoo Zoo",
             "Kusum" : "ku ku",
             "Aakar" : "Golu"}
print(nicknames.keys())
print(nicknames.values())

# Iterating a dictionary
for key in nicknames:
    print(f'keys:{key},value:{nicknames[key]}')
for key,value in nicknames.items():
    print(f'keys:{key},value:{value}')
# Modifying multiple keys
d = {'a' : 1, 'b': 2, 'c' :3}
for key in d.keys():
    d[key] = d[key] **2
print(d)

# Present [04/11/2026]
input = "Aakar Sharma"
freq = {}
for ci in input:
    if ci not in freq:
        freq[ci] = 0
    freq[ci] +=1
print (freq)

# Sets
# Sets with default elements
s = set()
print(type(s))
s = {1,2,3,45,12,78,12,3,4,5,6,7,8,9} #set by default value give in order
print(s)
# print(s[1]) #indexing is not allow in set so its give error
s = {1,True,(1,2),'a'} # true is eual to 1 so 1 is in already in set that's why in output duplicate value remove and give as order wise
print(s)
# s = {True, [1,2,3]} 
# print(s)

s = {1, True, (1,2) , 'a'}
s.add(False) #its value 0 so its position first in putput
s.add(False) #its not taken becuase false is eual to 0 already has 
print(s)

# update an element
s = {'a', 'b', 'c'}
s.update(['d','e','f']) #direct set not allow the list but in update its allow list
print(s)

# Delete an element inside the set
s.remove('a')
print(s)
print(len(s))
# to fetch differnt character in line
for e in s:
    print(e)

# to check element in set
print('a' in s) #false because its remove
print('d' in s)#true

# intersection, union, differnce
food_that_you_like_to_eat = {'Pizza' , 'Noodles', 'Pasta' , 'Chocolates', 'Burger'}
food_that_are_expensive = {'Pizza', 'Croissant', 'Avocado'}
print(food_that_you_like_to_eat.intersection(food_that_are_expensive)) #common value give
print(food_that_you_like_to_eat.union(food_that_are_expensive))  #all value give
print(food_that_you_like_to_eat.difference(food_that_are_expensive))  #unique value of 1st list prior {'Burger', 'Pasta', 'Noodles', 'Chocolates'}
print(food_that_are_expensive-food_that_you_like_to_eat)

# Given a sentence count the number of unique words.
sentence = 'This is a sentence.This is not a paragraph.'
words = sentence.split(' ')
print(words)
print(len(words))

unique = set(words)
print(unique)
print(len(unique)) #common value not take in set