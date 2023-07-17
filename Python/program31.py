#WAP to count the number of string  where the string length is 2 or more and the first and last charater are 
# same from the given list of string.

arr=input()
count=0

words=arr.split(" ")
print(arr)
print(words)

for i in words:
    if len(i)>=2 and i[0]==i[-1]:
        count+=1

print(count)

