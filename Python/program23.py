#WAP to take input from console.find count of prime number

n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))

prime_count=0

for ele in l:
    if ele==1 or ele==0:
        continue
    else:
        prime=True
        for i in range(2,ele):
            if ele%i==0:
                prime=False
        if prime==True:
            prime_count+=1

print(f"There are {prime_count} prime in the list")