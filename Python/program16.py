# sum of series
# WAP  to find sum of series: 1/1! + 2/2! +.........+ n/n!

# note-Limit the decimal place upto 5

num=int(input())
sum=0
n=1

while n<=num:
    fact=1

    for i in range(1,n+1):
        fact*=i
        i=i+1

    sum+=(n/fact)
    n=n+1

print("Sum of the series is:",round(sum,5))

