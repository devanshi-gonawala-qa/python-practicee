'''
oops:
class
object
inheritance
'''

'''class Car:
    pass #if you don't have any content to write you write pass 
# Object
car1 = Car()
car2 = Car()'''

# class Student:
#     def setData(self,name,age):
#         self.name = name
#         self.age = age
#     def getData(self):
#         print(f"Name is: {self.name}")
#         print(f"Age is: {self.age}")

# s1 = Student()
# s1.setData("Devanshi", 24)
# s1.getData()

# Constructor
# it is a special function which is invoked automatically when object is cretaed

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age=age
    def getData(self):
        print(f"Name is: {self.name}")
        print(f"Age is: {self.age}")

s1 =Student("Devanshi" , 24)
s1.getData()

# Normal function without parameter
class Tops:
    def __init__(self):
        print("This is a default consturctor")

t1 = Tops()

# inheritance
# Deriving the attribute of some other class
# single,multi level, multiple, hierarchical, hybrid
# Object will be made for last child only
# Single inheritance
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary =  salary
    def get_data(self):
        print(f'Employee name is {self.name}')
        print(f'Salary is {self.salary}')

class Developer(Employee):
    def write_code(self):
        print(f'{self.name} writes code')
d1 = Developer("Mansi", 45000)
d1.get_data()
d1.write_code()

# Multi level inheritance
class Employee:
    def __init__(self, dev_name, salary, tester_name):
        self.dev_name = dev_name
        self.salary =  salary
        self.tester_name = tester_name

    def get_data(self):
        print(f'Employee name is {self.dev_name}')
        print(f'Salary is {self.salary}')
        print(f'tester name is {self.tester_name}')

class Developer(Employee):
    def write_code(self):
        print(f'{self.dev_name} writes code')

class Tester(Developer):
    def test_build(self):
        print(f'{self.tester_name} Test the build')
t1 = Tester("Mansi", 45000, "Devanshi")
t1.get_data()
t1.write_code()
t1.test_build()

# 27/11/2026
# multiinheritance 
class Browser:
    def open_browser(self):
        print("Open Browser")
class ApiActivity:
    def call_api(self):
        print("Api called")
class Login(Browser, ApiActivity):
    def login(self):
        print("Login called")
l1 = Login()
l1.open_browser()
l1.call_api()
l1.login()

# Hierarchical inheritance
class Browser:
    def open_browser(self):
        print("Open browser")
class Login(Browser):
    def login(self):
        print("login called")
class SignUp(Browser):
    def sign_up(self):
        print("sign up")
l2 = Login()
l2.open_browser()
l2.login()

s2 = SignUp()
s2.open_browser()
s2.sign_up()

# Hybrid inheritance
class BaseTest:
    def base(self):
        print("This is base class")
class ApiTest(BaseTest):
    def api_test(self):
        print("Api testing")
class WebTest(BaseTest):
    def web_test(self):
        print("Web test")
class Login(WebTest, ApiTest):
    def login(self):
        print("Login called")
l3 = Login()
l3.base()
l3.api_test()
l3.web_test()
l3.login()


        