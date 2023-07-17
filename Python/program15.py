#find min ,max and sum of digits

num=int(input())

min=9
max=0
sum=0
temp=str(num)
while(num>0):
    rem=num%10
    sum+=rem

    if(rem<min):
        min=rem
    if(rem>max):
        max=rem

    num//=10

l=len(temp)
avg=sum/l
print(f"Average of a number:{avg}")
print(f"Minimum digit:{min} , Maximum digit:{max} and Sum of digits:{sum}")