# WAP to take input array from user and then print array and the sorted array (using selection sort)

arr=[]
n=int(input("Enter"))
for i in range(n):
    arr.append(int(input()))

print("Original list:",arr)

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp

print("Sorted array:",arr)