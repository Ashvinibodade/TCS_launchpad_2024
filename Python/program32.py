# WAP to test if list contain all the elements in range.Take list as input from user and range starting and 
# ending value.If elements in the list is present in the range the mention true otherwise false

n=int(input("Enter no of element in the list:"))
l=[]
for i in range(n):
    l.append(int(input()))

a=int(input("Enter the starting point:"))
b=int(input("Enter the ending range:"))
flag=True
for i in l:
    if i<=a and i>=b:
        flag=False
        break


print(f"The original list is:{l}")
print(f"Does list contain all elements in range : {flag}")
