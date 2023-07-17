num=input()
temp=int(num)
length=len(num)
res=0
while(temp>0):
    rem=temp%10
    res=res+(rem**length)
    temp=temp//10

if(res==int(num)):
    print("Armstrong")
else:
    print("Not Armstrong")
    