#WAp to get the number of occurences of a specified element in the array . Create a array by taking input from user

arr=[]
count=0
n=int(input("Enter"))
for i in range(n):
    arr.append(int(input()))

ele=int(input("Enter the element to check occurence:"))

for i in range(len(arr)):
    if ele==arr[i]:
        count+=1

print(f"Original array:{arr}")
print(f"Number of occurence of the number {ele} in the array :{count}")