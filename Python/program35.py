# WAP to combine two dictionaries by adding values for common keys

d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
d_final={}

for i in d1:
    for j in d2:
        if i==j:
            d_final[i]=d1[i]+d2[i]
            d1[i]=0
            d2[i]=0
for i in d1:
    if d1[i]!=0:
        d_final[i]=d1[i]
for i in d2:
    if d2[i]!=0:
        d_final[i]=d2[i]
        
print(d_final)