#find sum of even and odd digits

num=int(input())
sum_even=0
sum_odd=0

while(num>0):
    rem=num%10
    if(rem%2==0):
        sum_even+=rem
    else:
        sum_odd+=rem
    num//=10

print(f"Sum of even numbers:{sum_even} and sum of odd numbers:{sum_odd}")

