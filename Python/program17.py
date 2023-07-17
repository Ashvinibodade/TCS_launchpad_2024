# print prime if given number is prime otherwise print nonprime

num=int(input())
flag=False

if num==1:
    print("Not prime")
elif num>1:
    for i in range(2,num):
        if(num%i==0):
            flag=True
            break

if flag==False:
    print("prime")
else:
    print("Non prime")