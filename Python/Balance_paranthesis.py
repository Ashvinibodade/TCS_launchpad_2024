open_paranthesis=['[','{','(']
closed_paranthesis=[']','}',')']

def check(mystr):
    stack=[]
    for i in mystr:
        if i in open_paranthesis:
            stack.append(i)
        elif i in closed_paranthesis:
            pos=closed_paranthesis.index(i)
            if((len(stack)>0) and (open_paranthesis[pos]==stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
            
    if(len(stack)==0):
        return "Balanced"
    else:
        return "Unbalanced"

string=input()
print(string ,"-",check(string))