# List

# Q1. Create a list containing five of your favorite fruits.print the list.
fruits = ["Apple", "Banana", "Orange", "Kiwi", "Chiku"]
print (type(fruits)) #only for know the type
print (fruits)

# Q2. Create a list of five numbers.Print the first and last items.
numbers = [21,32,34,18,6]
print (numbers[0], numbers[-1])

# Q3. Create a list of numbers and append one new number to it. Print the updated list.
numbers1 = [18,6,31,15,25]
numbers1.append(30)
print(numbers1)

# Q4. Create a list of colors. Change the second item to "blue" and print the list.
colors = ["Purple", "Red", "White", "Black", "Yellow"]
colors[1] = "Blue"
print(colors)

# Q5. Create a list of numbers. Remove one item from list and print the result.
Numbers = [91, 87, 75, 64, 43]
Numbers.pop(0)
print(Numbers)

# Functions

# Q6. Write a function named greet() that prints "Hello, students!" . Call the function.
def greet():
    print("Hello, students!")
greet()

# Q7. Write a function named add(a,b) that returns the sum of two numbers. Print the result.
def add(a,b):
    return a + b
print("Total is: " , add(39,27))
    
# Q8. Write a function named square(n) that returns the square of number. Test it with 5.
def square(n):
    return n**2
print(square(5))

# Q9. Write a function named is_even(n) that returns True if a number is even and false otherwise.
def is_even(n):
    if (n%2 == 0):
        return True
    else:
        return False
print(is_even(67))

# Input

# Q10. Ask the user for their name and print a greeting using that name.
name = input("Enter your name: ")
print("Hello, " + name + "!")

# Q11: Ask the user for two numbers and print their sum. Convert the input to numbers.
num1 = int(input("Enter Your first number: "))
num2 = int(input("Enter Your Second number: "))
print("Sum is " , num1 + num2)

# Q12. Ask the user for their age and print how old they will be after 5 years.
age = int(input("Enter your age: "))
print("Your age after 5 years will be: ", age + 5)

# Slicing

# Q13. Given text = "Python", print the first three characters using slicing.
text = "Python"
print(text[0:3])

# Q14. Given text = "Programming", print the last four characters using slicing.
text1 = "Programming"
print(text1[-4:])

# Q15: Given numbers = [10, 20, 30, 40,50, 60] , print the first three items using slicing.

