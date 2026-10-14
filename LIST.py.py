# 09/10/2026
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

# 12/10/2026
# Square all the eleements inside the array [method 2]
a = [1 , 2, 3, 4]
for index in a : #becasue we not print whole array square sonits should be seperate that's why we use the index variable
    print(index**2)

# Square all the elemnets inside the array [method 1]
a = [1, 2, 3, 4]
for i in range(len(a)):
    a[i] = a[i] ** 2
print(a)

# Function in a list
# len()
a = [1, 5, 6, 10, 15, 20]
print(len(a)) # 6

# append() - add value at the last
a = []
print(a) # blank prints
a.append(10) # 10
print(a)
a.append(True)
print(a)
a.append (True)
print(a)
a.append("Devanshi")
print(a)
a.append("Devanshi")
print(a) #also prints the duplicate value in the list
a.append([1,2,3])
print(a) #also prints list in list

# insert() - give number and put that value on that index number
a = [1, 2, 3, 4]
a.insert(1, "Devanshi")
print(a)
a.insert(0, "Fenil")
print(a)
a.insert(-1, "abc")
print(a)
a.insert(8, 'shdv')
print(a) # if index number is not there so its add at the last
a.insert(110, 'last')
print(a)

# pop() - removes the item at last and delete which index mention
a = [1, 2, 3, 4, 5, 6]
print(a.pop())
print(a)
print(a.pop(0))
print(a)
print(a.pop(2))
print(a)
# 2, 3, 5 - final
# print(a.pop(10)) #gives error becuase 10th index not in a list

# remove() - if duplicate value there at one time only remove he first number or value
students = ['Kusum', "Devanshi", "Keyuri", "Sweety", "Khushi", "Aishwarya"]
students.remove("Khushi")
print(students)
a = [1, 2, 3, 4, 5, 2]
a.remove(2)
print(a)

# 14/10/2026
# + opreator
a = [1,2, 'a']
b = [4, 5, 6]
c = a+b
print(c)
# extend - list value add in list
a = [2, 3 , 4, 7]
a.extend([12, 13, 15, 20])
a.extend(range(5)) # range 0 to 4 aslo add in list
print(a)

# Check value in list use in
a = ['a', 'c', 'd', 'g']
print('x' in a)
if 'd' in a:
    a.remove('d')
print(a)

n = int(input("How many colors: "))
colors = []  #to make blank list of colors because this value add in the blank list when user enter color
for _ in range(n):
    color = input("Enter color: ")
    colors.append(color) #user enter color so add in list that's why use append
print(colors)

# range len
a = ['Piyush', 'Shekhar']
for i in range(len(a)):
    if a[i] == "Shekhar":
        print(i)

a = ['a', 'b', 'c']
for i in range(len(a)):
    print(i , ' ', a[i])

# 2D list [Nested list]
students = [
    [1, "Pooja"],
    [2, "Devanhsi"],
    [3, "Keyuri"]
]
print(students)

# Indexing in 2d list
a = [
    [10,20,30], #0
    [40,50,60], #1
    [70, 80,90] #2
]
print(a[0][1]) #20 
print(a[1][1]) #50
print(a[2][0]) #70

# Itreation in list
numbers = [
    [1,2],
    [3,4]
]
for row in numbers: #row[0]
    for item in row:
        print(item*2, end = " ")
    print()