# Reverse a number

# case1:if number is in string formate
num=input()
print(num[::-1])

# case2:if number is integer
num=int(input())

while num>0:
    rem=num%10
    res=(res*10)+rem
    num//=10

print("Reversed string is :"+res)