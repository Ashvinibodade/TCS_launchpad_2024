#WAp to remove all duplicates from the array and return a new array

arr=[]
count=0
n=int(input("Enter"))
for i in range(n):
    arr.append(int(input()))

ty=set(arr)
new_arr=list(ty)

print(f"New Array {new_arr}")