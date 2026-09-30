N = int(input("Enter the number : "))
flag = False # in starting flag false

if N == 1:
    print("Not a prime number")
elif N == 2:
    print("Prime number")
else:
    for i in range(2, N):
        if N%i == 0:
            flag=True
            break
        else:
            flag = False
    if flag == False:
        print("prime number")
    else:
        print("Not a prime number")
print()
# 28/09/2026
# To extract last digit i will use %10
N = 235
print(N%10)
print()
# if last digit remove and print 1st 2 digit or 3 digit use floor division

N=123
print(N//10)
print()
# Question
# print the digits of number '459' in reverse order
# print 9 5 4
# steps 1. intput from user , then last digit remove so use mod and then after remove the last digit from N (this all in use in while loop)
N=int(input("Enter a value in positive integer :"))
while N>0:
    print(N%10, end = " ")
    N=N//10
print()

# print sum of digits of N. N> 0
# N = 6531
# 6+5+3+1 = 15. print(15)
# Steps : input from user , while N>0, N%10, ans = ans + N, N//10

N=int(input("Enter the number in positive integer to calculate : "))
ans = 0
while N>0:
    ans+=N%10
    N//=10
print(ans)
print()

# Add a given digit to the back of a given number N
# N > 0
# 0<=D<=9
F= int(input("Enter positive integer: "))
K = int(input("Enter value greater than 0 less than 10: "))
F = F*10+K
print(F)

# reverse in - value
N = - 4543
if N < 0:
    copy = N * -1 #this is the formula to hack for negative number
else:
    copy = N
rev = 0
while copy > 0:
    d = copy % 10 #last digit
    rev = rev*10 + d #append the last digit number
    copy = copy//10
if N< 0:
    rev = rev * -1
print(rev)

# 30/09/2026
# reverse task [multiple times number ask code]

T = int(input("Enter a single digit : "))
while T > 0:
    N=int(input("Enter the digit: "))
    if N < 0:
        copy=N*-1
    else:
        copy=N
    rev=0
    while copy>0:
        d=copy%10 #last digit
        rev=rev*10+d
        copy//=10
    if N <0:
        rev = rev*-1
    print(rev)
    T-=1