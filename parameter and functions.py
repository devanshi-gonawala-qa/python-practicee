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

    


