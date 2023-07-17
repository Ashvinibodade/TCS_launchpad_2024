#WAP to search how many numbers in given array are divisible by input value .Also display those numbers

arr=[]
count=0
n=int(input("Enter"))
for i in range(n):
    arr.append(int(input()))

print("Array is:",arr)

value=int(input("Enter element for divisibility:"))
l=[]
for i in range(len(arr)):
    if arr[i]%value==0:
        count+=1
        l.append(arr[i])

print(f"{count} elements in array are divisible by {value} which are {l}")