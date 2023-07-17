# WAP to take input array from user and find the second largest element in the array

arr=[]
n=int(input("Enter"))
for i in range(n):
    arr.append(int(input()))

if(len(arr)<2):
    print("Invalid input")
else:
    arr.sort()
    print(f"In array {arr} ,the second largest element is {arr[-2]} ")