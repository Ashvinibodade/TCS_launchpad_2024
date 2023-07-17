#Given a word,create a function which returns whether or not its possible to create a palindrome by rearranging 
# the letters in the word


def checkPalindrome(st):
    l=[]

    for i in range(len(st)):
        if st[i] in l:
            l.remove(st[i]) 
        else:
            l.append(st[i])

    if len(st)%2==0 and len(l)==0:
        return True
    elif len(st)%2!=0 and len(l)==1:
        return True
    else:
        return False

inp_str=input()
print(checkPalindrome(inp_str))
