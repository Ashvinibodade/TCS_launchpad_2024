# Problem Statement:
# ------------------------------------
# WAp to find the additive and multiplicative persistence of a number until the number is single digit and display 
# the number of iterations to reach a single-digit  number 
# + Take the number to be used for additive and multiplicative persistence as user input
# + Create 2 methods that take an integer as an argument  and-
#     Return its additive persistence
#     Return its multiplicative persistence 

# /////additive persistance
# Example=123496
# 1+2+3+4+9+6=15
# 1+5=6       ////////////it take 2 iteration

# /////multiplicative persistance
# Example=77
# 7*7=49
# 4*9=36
# 3*6=18
# 1*8=8    /////////it takes 4 iterations 


def additivePersistence(n,s):
    if s==1:
        print("Enter the number greater than 9")
        exit()
    else:
        c=0
        while(s>1):
            c+=1
            sum=0
            for ele in str(n):
                sum+=int(ele)
                s=len(str(sum))
                n=sum
        return c

def multiplicativePersistence(n,s):
    if s==1:
        print("Enter the number greater than 9")
        exit()
    else:
        c=0
        while(s>1):
            c+=1
            sum=1
            for ele in str(n):
                sum*=int(ele)
                s=len(str(sum))
                n=sum
        return c

a=input("Enter the number:")
size=len(a)
print("Additive persistence result:",additivePersistence(a,size))
print("Multiplicative persistence result",multiplicativePersistence(a,size))