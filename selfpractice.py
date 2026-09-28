# # a=""
# # print(type(a))
# # b=bool(a)
# # print(type(b))
# # print(b)
# # a=" "
# # print(type(a))
# # b=bool(a)
# # print(type(b))
# # print(b)

# # 1. Positive, Negative, or Zero
# # Problem Statement:
# # Given an integer, print whether it is positive, negative, or zero.

# # try:
# #   a = int(input("Enter number : "))

# #   if a > 0:
# #     print("This is the positive number")
# #   elif a < 0:
# #     print("This is the negative number")
# #   else:
# #     print("This is the zero")
# # except ValueError:
# #   print("Invalid input, please enter valid input")

# # 2. Maximum of Three Numbers
# # Problem Statement:
# # Given three integers, print the maximum number.
# # a = int(input("Enter the first number: "))
# # b = int(input("Enter the second number: "))
# # c = int(input("Enter the third number: "))
# # if a>b and a>c:
# #     print("Maximum number is: ",  a)
# # elif b>a and b>c :
# #     print("Maximum number is : ", b)
# # else:
# #     print("Maximum number is : ", c)


# # 3. Check Divisibility
# # Problem Statement:
# # Given an integer, check whether it is divisible by 5.
# # a = int(input("Enter the number : "))
# # if a%5 == 0:
# #     print("The number is divided by 5")
# # else:
# #     print("The number is not divided by 5, enter other number")

# #:::

# ### 🧠 One line to memorize

# # **`/` = division, `//` = quotient, `%` = remainder.**

# # And for **"is it divisible?"**, think:

# # **`number % divisor == 0`**.

# # # Take two numbers from the user
# # a = int(input("Enter the first number: "))
# # b = int(input("Enter the second number: "))

# # # Normal division
# # print("Normal division:", a / b)

# # # Quotient
# # print("Quotient:", a // b)

# # # Remainder
# # print("Remainder:", a % b)


# # 4. Voting Eligibility
# # Problem Statement:
# # Given a person's age, check whether they are eligible to vote.

# # If age is 18 or above → Eligible
# # # Otherwise → Not eligible
# # a = int(input("Please enter your age to valid you are eligible for vote or not : "))
# # if a >= 18:
# #     print("You can give vote")
# # else:
# #     print("You are not eligble for vote")


# # 5. Grade Calculator ⭐
# # Problem Statement:
# # Given a student's marks, print their grade:

# # 90–100 → A
# # 80–89 → B
# # 70–79 → C
# # 60–69 → D
# # # Below 60 → F
# # try:
# #     a = int(input("Please enter your marks: "))
# #     if a >=90 and a<=100:
# #         print("Your grade is A")
# #     elif a >=80 and a<=89:
# #         print("Your grade is B")
# #     elif a >=70 and a<=79:
# #         print("Your grade is C")
# #     elif a >=60 and a<=69:
# #         print("Your grade is D")
# #     elif a<60:
# #         print("Your grade is F")
# #     else:
# #         print("This marks is not valid")
# # except ValueError:
# #      print("Enter valid number")


# # OR 

# # if a >= 90:
# #     print("A")
# # elif a >= 80:
# #     print("B")
# # elif a >= 70:
# #     print("C")
# # elif a >= 60:
# #     print("D")
# # else:
# #     print("F")

# # Question 1 — Leap Year Checker ⭐⭐
# # Problem Statement:
# # Take a year from the user and check whether it is a leap year or not.

# # year = int(input("Enter a year: "))

# # if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
# #     print("Leap Year")
# # else:
# #     print("Not a Leap Year")

# for i in range(10):
#     print(i)

        
# for i in range(1, 101):
#     print(i)

# for i in list(range(0, 2)):
#     print("Hello my name is Devanshi")

N = input("Enter the number :")
flag = False

for i in N:
    if i == "5":
        flag = True
        break
if flag == True:
    print("This number contain 5")
else:
 print("This number not contain 5")




