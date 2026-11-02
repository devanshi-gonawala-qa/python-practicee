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