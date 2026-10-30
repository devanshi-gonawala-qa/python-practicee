# 21/10/2026
# Tuples - store in () AND tupls are imutable
# normal list
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupitar", "Saturn", "Uranus", "Neptune"]
planets.append('Sun')
print(planets)

# Tuples of number
num = (1,2,3)
print(type(num))
print(num)
# try to change tuple index wise like we want to change 1 to 5
# num[0] = 5
# print(num) #gives error

# Create tuple of single digit
b =(1,)
print(type(b))
c = ('a',)
print(type(c))
a = () #-blank tuple
print(type(a))
# tuple of range 0 - 10
nums = tuple(range(11))
print(nums)

a = [] #first create in list and then convert in to tuple becase tuple is immutable we cannot change 
for i in range(11):
    a.append(i)
a = tuple(a) #list to tuple
print(a)

# Tuples in functions
def swap(a,b):
    return(b,a)
print(type(swap(12,34))) #only know to type that's why set argumnet , not impect

a,b = swap(5,6)
print(a)
print(b)

def name(): # take input from user
    first_name=input("enter first name: ")
    last_name = input("enter last name: ")
    return (first_name,last_name)
# name() #only call
first_name,last_name =name()
print(first_name,last_name)

# Partially mutable tuples
a = (1,2,3,[4,5,6]) # in 0 index 1 in 1 index 2, in 2 inderx 3 in 3 index [4,5,6] 
print(a)
print(a[0])

print(a[-3]) #in -1 index last means [4,5,6] then -2 = 3, and so on..
print(a[3])
a[3].append (20) #we can add the value in list in tuple
print(a)

# # Quiz question
# t = (1,2,3)
# t[0] = 4
# print(t) #immutable we can not change tuple\

a = 23
t = (a)
print(type(t)) #give int because int is not converted in tuple and if you convert string to tuple so write tuple keyword

# ittration use to value print in one by one
a = (1,2,3,4,5)
for n in a:
    print(n)

# Using range function its store as a index
for i in range(len(a)):
    print(a[i]) #a[0] = 1 a[1] = 2

# String
# String is immutable
a = 'Piyush'
b = "singh"
print(type(a))
# a[0] = "S"
# print(a)

# Convert char to ascii use "ord" every character, number and special characters has ascii number
print(ord('a')) #97
print(ord('m'))
print(ord('z'))
print(ord('9'))
# Convert Ascii to char use "chr" every character
print(chr(97)) #a
print(chr(109))

# Properties of string
# String are imutable
# a = 'Piyush
# a[0] = 'a'

# We are replacing and not modifying
# Homogeneity
a = ["Naveen", "Kumar"]
a[0] = "Naveenkumar" #this is change because we can change in list
print(a)
# a = a+42 ?in list we can not add str or in 
# print(a)
a = "piyush" #we can add string 
a = a + 'd'
print(a)

# Iterability
a = 'Piyush'
for each_chr in a:
    print(each_chr)

for i in range(len(a)):
    a[i] = 'c'
    print(a[i])

# 28/10/2026 - ma'am on leave
# 26/10/2026 - give test
# 30/10/2026 
# case sensitive 
a = 'Piyush'
b = 'piyush'
print(a == b)
s= 'Tops Tech'
print(s[0:5]) #ans is Tops

text = 'TopsTechnologies'
print(text[0:6])
print(text[-3:]) #ans is ies
print(text[6:11])
print(text[::-1]) #reverse string
print(text[::2]) #1 char skip and then print word
print(text[3:])

# Functions in strings
print("tops tech".capitalize()) #1st word capital
print("tops tech".title()) #every first word capital
print("tops tech".count(t)) #how many times t come
print('pooja makhija'.count('ja'))
deltr = 'ae'
print('piyush singh'.replace('iy',deltr)) #change iy to ae

# Replace 
a = 'piyush'
b = a.replace('i','e')
print(a)
print(b)

# Split(Seperator)
print('abc_bncd_def'.split('_'))
print('abc+_bncd+_def'.split('+_'))

# Join()
a = ['abc','bncd','def']
print('_+'.join(a))

#upper and lower
print('tops'.upper())
print('TOPS'.lower())

# Quiz
a = 'abcd'
a+='e'
print(a)
print(len(a)) #ans is abcde and length is 5
