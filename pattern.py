# Pattern 5 star with 5 row and column
for _ in range(5):
    print("*"*5)
# hw
#  Increasing pattern
for i in range (1,6):
    print("*" * i)

#  Homework
for i in range(1,6):
    print(" "*(5-i)+"*"*i)

# Function 
# need of the function
# Banking system
# ********************
# Transaction complete
# Thank you for visiting
# ********************
print("*" * 20)
print("Transaction complete")
print("Thank you")
print("*" * 20)

# Syntax of defining functions
# defining a funtion
# def function_name():
    # actions
# To call the function
# Function_name()


# 02/10/2026
# Naming convention
# The naming convention for a function is the same as variables.
# It should be composed of alphabet, number, and underscorer should start with an alphabet or underscore.
# It should not be a keyword.
# In python we use snake case(there are two cases camel case and snake case)
# snake_case, camelCase, TitleCase

def area_of_circle():
    print(3.14*5*5)
area_of_circle()

# Return statement
# Above is how we define a function and call it. Now we want to add 1 to it or 2 to it. Can't we take it to a variable?
# This is what return statemnets are for. It is like a black box where you want some task to be done. But after the task is done you want it to return some value as well.

def abc():
    return 5 
abc() #if only return the function , its not verify what is return so what is return we used to print
print(abc()) #this return 5

a = abc() #function save in variable
print(a)

def area_of_circle():
    return 3.14*5*5
print(area_of_circle())
print(area_of_circle()+10)

#  Note : Functions excution ends at return. Once a return staement is found rest of the code will not be excuted.It is just like a break loops.
#  If you do return without any value, It will return None.

def abc():
    print("Hello")
    return  #after return statemnet nothing to return so only print before statemnet hello prints and none retrun because nothing write in return
    print("world")
    print("Tops")
print(abc())

def even_odd():
    a = 20
    if a%2==0:
        return "Even"
    else:
        return "Odd"
print(even_odd())       