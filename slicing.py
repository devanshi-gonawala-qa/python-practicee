def sub_list(li, start, end):
    new_list = []
    for i in range(start,end +1):
        new_list.append(li[i])
        # 49, 6 71
    return new_list
li = [2, 23, 49,6,71,55]
print(sub_list(li,2,4))

# 16/10/2026
# other way to write slicing
li = [2, 23, 49,6,71,55]
new_slicing_list = li[2:5] #stop at 4 becase its 5 index
print(new_slicing_list)

my_list = [0,1,2,3,4,5,6,7,8,9]
my_string = "Hello Python"
print(my_list[2:7])
print(my_string[0:5])

# Omitting start or end
print(my_list[:5]) #by default takes 0 index at start oint because only give end value
print(my_string[7:]) # by default end point takes end of string value ython

# Slicing with a step
print(my_list[0:10:2]) #takes value from 0 and 1 step skip and print the value
print(my_string[::-1]) #string value reverse from end 

#Creating a copy of sequence
new_list = my_list[:] #start and end value from 0 and end of the last index
print(new_list) # 0 to 9

a = [1,2,3] 
b = a 
a[2] = 4 #at the 2nd index change value 3 to 4
print(b) # 124

# Introduction to 2nd list(nested list)
math = [100,98,90]
science = [90,100,89]
hindi =[96,76,100]

subjects=[math,science,hindi]
print(subjects)

# Indexing in 2nd list , get the number of 2nd student for hindi, take out hindi number
# [[100, 98, 90], [90, 100, 89], [96, 76, 100]]
print(subjects[2][1]) # 76   

# Get the number of 3rd person for science subject
print(subjects[1][2]) #89 3 index means 2nd student

# Iterating a 2d list - for iteration takes for loop
subjects = [[100, 98, 90], [90, 100, 89], [96, 76, 100]]
for i in range(len(subjects)):
    for j in range(len(subjects[i])):
        print(subjects[i][j], end = " ") #100 98 90
    print() #new line after 1 index complete

# Input a 2nd list
user_inp_list =[] #make empty list
row = 4
col = 2

for i in range(row):
    temp = [] 
    for j in range (col):
        n = int(input()) #1 2
        temp.append(n) #not remove the value its adding that's why using append
    user_inp_list.append(temp)
    print(user_inp_list)

# Create a matrix of 5 (rows) * 4(column) and enter only even numbers from 0 -> 40 
# 0 2 4 6
# 8 10 12 14
# 16 18 20 22
# 24 26 28 30
# 32 34 36 38

row = 5
col = 4
count = 0 # start from 0
even_num = [] # create empty list becase fill the value in this list 
for i in range(row):
    temp = [] #create blank list because value which is come stor in this variable and temp is in the row means in i 
    for j in range(col):
        temp.append(count)
        count+=2 #increase 2 number check questioon
    even_num.append(temp)
print(even_num)

# Question 1
# Given a value and a list , find the element and print "found at : index" else "not found"

# a = [4, 5, 3 , 6, 10]
# n = 6
# ans = found at 3
# n = 11
# ans = not found

a = [4, 5, 3 , 6, 10]
n = 11 # change value in n and check in the list or not
for i in range(len(a)):
    if a[i] == n:
        print("Found at :" +str(i))
        break
else:
    print("Not found")

# 16/10/2026
# other method to check 
a = [4,5,3,6,10,6]
n = 60
if n in a:
    print("Found at :" + str(a.index(n)))
else :
    print("Not found")

# Given a list , you have to find the maximum element in this list

a = [2,10,2,12,60]
# ans = 60
max_ele = a[0] #60
for i in range(1, len(a)): #its startying at index 1 because we consider initially 0 index 2 is greater
    if a[i] > max_ele: #60 >12
        max_ele = a[i] #60
print(max_ele)

# Given a list , you have to find the minimum element in this list
a = [2,10,2,12,60]
# ans = 2
min_ele = a[0] #2
for i in range(1, len(a)): #its startying at index 1 because we consider initially 0 index 2 is greater
    if a[i] > min_ele: #2>10
        min_ele = a[i] #2
print(min_ele) 

# List comprehension, create a list of squeares till n-1
# normally print
n = 5 
square = []
for i in range(n):
    square.append(i*i)
print(square)
# List comprehension
new_square = [i*i for i in range(n)]
print(new_square)

# Create a list of all even elements
even_num = [i for i in range(0,n,2)] #0 2 4
print(even_num)
# 2nd method
even_num = [i for i in range(0,n) if i%2 ==0]
print(even_num)

# create a 2 array with initalization of 0 
row = 5
col = 4
array = [[1 for j in range(col)] for i in range(row)] # 1 because we want to print 1 you can change any number
print(array)

# Split function
a = input()
arr = a.split(" ") #if you want to split + then its split liek 12+67 so output is 12 67
arr = [int(i) for i in arr]
print(arr)

user_inp_list=[]
row = 5
col = 4
n = 0
for i in range(row):
    temp = []
    for j in range(col):
        n+=2
        temp.append(n)
    user_inp_list.append(temp)
print(user_inp_list)
# reverse list
a = [1, 2, 6, 4, 8, ' ']
print(a[::-1])

