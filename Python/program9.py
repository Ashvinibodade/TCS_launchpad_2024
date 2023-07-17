# write a program which take input from console and give the count of each vowel

sentence=input()

for char in ['a','e','i','o','u']:
    count=0

    for letter in sentence:
        if letter.lower()==char:
            count+=1
    
    print("{} - {}".format(char,count))