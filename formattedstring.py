# Formatted String
name = 'Devanshi'
gender = 'Female'
age = '24'
# Simple method
print('Name:-',name,"Gender:-",gender,"Age:-",age)
# Formatted method
print(f'Name:{name} Gender:-{gender} Age:- {age}')
temp = 'Name: {} , gender:-{} , Age:- {}'
print(temp.format("TOPS","Unspecified",13))

# List Comparrision
print([1,2,3,4,5] < [1,3]) #True 
print([1,3,0] > [1,3])
print([1,3] == [1,3])
print([1,4,5] > [1,6])

# String Comparrison
print('a' > 'A') #97 65 so true 97 is greater than 65
print('Aakar' > 'Sudip') #false 

# 02/11/2026
# Q1: You are given a list of strings, where each string represents a log entry from a system. 
# your task is find and print all log entries that contain the word "ERROR"

# logs = ["2024-07-18 10:00:01 INFO server started",
# 2024-07-18 10:01:17 ERROR failed to connect to database",
# "2024-07-18 10:02:45 WARNING High memory usage", 
# "2024-07-18 10:02:10 ERROR Disk full", 
# 2024-07-18 10:06:30 INFO Backup complete"]

logs = ["2024-07-18 10:00:01 INFO server started",
"2024-07-18 10:01:17 ERROR failed to connect to database",
"2024-07-18 10:02:45 WARNING High memory usage", 
"2024-07-18 10:02:10 ERROR Disk full", 
"2024-07-18 10:06:30 INFO Backup complete,error"]

for lines in logs:
    if "ERROR" in lines.upper(): #because error also in small letter
        print(lines)

# Q2: Print the longest line lines = [
# "Devops is awsome", ]
# "Error: Disk not found.",
# "Server started successfully at 10:05 AM."
# "OK"]
longest_line = ""
lines = ["Devops is awsome",
"Error: Disk not found.",
"Server started successfully at 10:05 AM."
"OK"]
for line in lines:
    if len(line) > len(longest_line):
        longest_line = line
    print(longest_line)

#  other this with python
print(max(lines))