import sys 
encoding = sys.getdefaultencoding()
print(encoding)

# File read

# file = open("sample2.txt" , "r") #it can only read its allows only read so it cannot make file

# Write - it can not create file
file = open('sample2.txt', "w")
# file.close()

# w+
file = open('sample.txt', "w+")
file.writelines(["1.\n" , "2.\n", "3."])
file.close()

# r+
file = open("sample.txt" , "r+")
content = file.read()
print(content)
file.close()