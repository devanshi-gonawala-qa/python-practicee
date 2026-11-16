import sys 
encoding = sys.getdefaultencoding()
print(encoding)

# File read

# file = open("sample2.txt" , "r") #it can only read its allows only read so it cannot make file

# Write - it can not create file
file = open('sample2.txt', "w")
file.write('This is\n multiple\n line')
file.close()

# w+
# file = open('sample.txt', "w+")
# file.writelines(["1.\n" , "2.\n", "3."])
# file.close()

# r+
# file = open("sample.txt" , "r+")
# content = file.read()
# print(content)
# file.close()

# 16/11/2026 - after diwali
# readline - only read one line
# file = open("sample.txt", "r+")
# content= file.readline()
# print(content)
# file.close()

# readlines
# file = open("sample.txt", "r+")
# content= file.readlines()
# print(content)
# file.close()

file = open("sample2.txt", "r+")
while True:
    chunk = file.read(5)
    if not chunk:
        break
    print(chunk)
file.close() #this , space total 5 means this is 1 chunk

# Exception handling
try:
    file = open("shsbhbdsc.txt","r")
except FileNotFoundError:
    print("OOPS the file is not present")
print("this is the end of program")

# Multiple types of Exception

try:
    file = open("vshg.txt","r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("OOPS the file is not present")
except PermissionError:
    print("You do not have permission to access this file")
except Exception as e:
    print("An error occured:", str(e))
except:
    print("Unknown errror occured")
finally:
    print("this is the end of program")

# Write error permission if files directly not allow to write that time this error occured 
try:
    file = open("notes.txt", "w")
    file.write("This is is the file")
    file.close()
    print("Write opreation successfull")
except PermissionError:
    print("You do not have permission to write to this file")
except:
    print("An error occured while writting to this file")

file = open("demo.txt" , 'w')
file.write("This is a demo file")
file.close() 

# File = open("demo.txt", "r")
# print(file.read())
# file.close()
# with open
with open("demo.txt", "r") as file1:
    print(file1.read())
# File1.write("This is a new line in the demo file")

with open("input.txt", "w") as file1:
    file1.write("This is line 1.\n")
    file1.write("Room 202 has 4 Acs.\n")
    file1.write("There are 3 dogs and 4 cats.\n")
    file1.write("ID:007, code:123456")
max_digit = -1
result = ""
with open("input.txt", "r") as file:
    for line in file:
        digit_count = 0
        for char in line:
            if char.isdigit():
                digit_count+=1
                if digit_count > max_digit:
                    max_digit = digit_count
                    result = line
    print(result)



