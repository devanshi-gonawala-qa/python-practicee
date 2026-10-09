#  Parameter and functions
def area_of_circle_5():
    return 3.14*5*5 #if in function no any parameter pass evry time write the code like multiply so for this solution we pass the parameters in the function and call time its give what is output we want
print(area_of_circle_5())

def area_of_circle(radius):
    return 3.14*radius*radius
print(area_of_circle(6))

def sum(a,b): # a and b is parameter
    return a+b
print(sum(10,20)) # 10, 20 argument

# What is parameter and argument
# If you want multiple parameters you can simply seprate them by comma, their types are not required.
# If the function is not returnning anything, then by default it will return None.
# In python, a paramter is a variable used in a function defination, while an argument is an actual value passed to the function during a call.
# In the above function, radius variable in the area circle() function is a parameter, whereas the 5 passed to it while calling, is an argument.

def sum(a,b):
    return a +b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def calculate_salary(base_monthly, bonus, equity):
    yearly_base= mul(base_monthly,12)
    yearly_base_bonus=sum(yearly_base,bonus)
    total_salary = sum(yearly_base_bonus,equity)
    return total_salary

a = calculate_salary(10000,5000,10000)
print(a + 10000)

# 05/10/2026
# Scope of variables

# a = 1 # Global scope
# def area_circle(radius):
#     area = 3.14 * (radius ** 2) #area is a local variable
#     return area
# b = area_circle(10) #Global variable
# print(a) # print 1
# print(b) #prints 314.0
# print(area) #error

a = 1 #global
def abc():
    a = 2 #local scope
    print(a) #2
abc() #2
print(a) #print 1

a = 1 #global
def abc():
    global a #now this a is global  
    a = 2 #local scope
    print(a) #2
abc() #2
print(a) #print 2

#Quiz
def foo(a): #0 prints 0 value thats is false
    if(a): #
        return 100
    a+=20 #0+20
    return a
print(foo(0)) #20

def solve(a,b):
    print('Function started')
    return 0
    c = a + b
    print('Function Ends')
c = solve(2,3) #0
print(c)

# Quiz 1
# foo() 1
# foo() 2
# for i in range(1,5):
#     foo()

# # And = 6 foo will be called

# Quiz 2
# def area_rectangle(l,b):
#     area = l * b
# area_circle1(3,4) # give error 
# print (area) #error because area is local variable and called outside the function

# Simple intrest
# Take principal, rate and time as input from user
# and create a function
# To calculate simple intrest # (p * r* t) /100
p =float(input("Enter principal: "))
r =float(input("Enter rate: "))
t =float(input("Enter time: "))

def simple_inetrest(p,r,t):
    return(p*r*t) /100
simple_inetrest_value = simple_inetrest(p,r,t)
print("simple_inetrest:" , simple_inetrest_value)

# Positional and keyword argument
def bio_data(name,age,gender):
    print("Name: ", name)
    print("Age: ", age)
    print("Gender", gender)
# bio_data(23,male, aakar) # give in 23 in name in age male and in gender aakar
bio_data(age=23,gender="Male", name = "Aakar")

# Default and undefined variables

def bio_data(name, age=0,gender=None):
    print("Name: ", name)
    print("Age: ", age)
    print("Gender:", gender)
bio_data(name="aakar")

# 07/10/2026  - ma'am on leave
# 09/10/2026

# Docstring
'''
hgghghbhbhb
bvghvgv bv
bvghvvgb
'''
print(round(3.45678,4)) # 3.4568
def abc(name,gender,age = 0):
    print(name,gender,age)
abc(name = "Devanshi", gender = "Female")

def abc(a,b,c=10):
    return a,b,c
print((abc(1,2)))


