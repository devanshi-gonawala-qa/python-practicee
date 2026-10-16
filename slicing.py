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
    temp [] #create blank list because value which is come stor in this variable and temp is in the row means in i 
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
