# WAp to read a word from console .Print the length of longest repeating character  streak

ty=input()
d={}
c=0
ans=""

for i in ty:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d:
    if c < d[i]:
        ans=i
        c=d[i]

print(ans)
