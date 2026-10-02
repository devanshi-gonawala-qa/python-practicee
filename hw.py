# HW
# Problem Statement: Maximum of two
# Given two integers, print the maximum of them.

# a = int(input("Enter the first number : "))
# b = int(input("Enter the second number : "))
# if a > b:
#     print("maximum number is : " ,a)
# else:
#     print("maximum number is : ", b)

# HW
# Problem Statement: Maximum of two and check equality also
# Given two integers, print the maximum of them or say both are equal.

# a= int(input("Enter the first number : "))
# b = int(input("Enter the second number : "))
# if a>b:
#     print(a)
# elif a < b:
#     print(b)
# else:
#     print("Both are equal")

#HW
# Problem Statement: Check even or odd
# Take an integer and print if it is even or odd
try:
    a = int(input("Enter number :"))
    if a%2 == 0:
          print("This is the even number")
    else:
          print("This is odd number")
except ValueError:
       print("Invalid number")

#  Increasing pattern
for i in range (1,6):
    print("*" * i)

#  Homework
for i in range(1,6):
    print(" "*(5-i)+"*"*i)