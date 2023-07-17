#WAP to read input from the console and the swap them from middle

import math

n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))

#even number of element
if n%2==0:
    ele_in_single_half=int(n/2)
    first_half=l[:ele_in_single_half]
    second_half=l[ele_in_single_half:]
    print(second_half+first_half)
#odd number of element
else:
    middle=int(math.floor(n/2))
    first_half=l[:middle]
    second_half=l[middle+1:]
    print(second_half+[l[middle]]+first_half)