#Write a program ,in which take a string from console and print the count of vowel

word=input()
count=0

for i in word:
    if i.lower() in ['a','e','i','o','u']:
        count+=1
    
print(count)