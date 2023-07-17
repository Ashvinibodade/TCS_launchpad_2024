#Read the word and letter from console and then print the word after deleting all the occurences of the letter

word=input()
letter=input()
t=[]

for i in range(len(word)):
    if(word[i]==letter):
        continue
    else:
        t.append(word[i])

y="".join(t)
print(y)