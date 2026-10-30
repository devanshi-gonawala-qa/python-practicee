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