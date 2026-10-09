# array - list in Python
# Mutable = means list is changeble
# list data type always be list type

#  range pending
a = [1,2,3]
print(a)
print(type(a))

a = ([1,2,3])
print(a)

a = ['a', 'b', 'c']
print(a)

a = [1,True,3.5,'piyush',None]
print(a)

# Indexing in a list
students = ['Kusum', 'Shubham', 'Pooja']
print(students)
# Indexing
print(students[1])
print(len(students))

# Reverse indexing
print(students[-1]) # -1 ,means last
print(len(students))
print(students[len(students)-2]) #total of len 3 - 2 = 1 on 1 prints shubham

# Updating an index in a list
students = ['Kusum', 'Shubham', "Pooja"]
print(students)

students[1] = "Navven"
print(students) #now its prints kusum, navven and pooja

# students[10] = "Piyush"
# print(students) give error because 10 is not in the list index

students[-1]= "Devanshi"
print(students)

students = ["Kusum", "Shubham", "Pooja", "Ruben", "Aarushi", "Vinoth", "Veerendra"]

for i in range(len(students)): #you can not write 7 because list may be change so don't hard coding thats why len(students) and if in future list increase or decrease this print properly
    print(students[i], end = "  ")