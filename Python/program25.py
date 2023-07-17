#Search numeric values from array between given range of two input values 
# (define a func to set logic to count in a range)

def count(arr,n,x,y):
    count=0

    for i in range(n):
        if i>=x and i<=y:
            count+=1
    return count

arr=[]
n=int(input("Enter"))
for i in range(n):
    arr.append(int(input()))

arr_size=len(arr)
a=int(input("Enter start point:"))
b=int(input("Enter end point:"))

k=count(arr,arr_size,a,b)
if k!=0:
    print(f"Values between {a} and {b} are {k}")
else:
    print("No value found")