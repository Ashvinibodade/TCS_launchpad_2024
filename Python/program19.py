#Read the sentence and word from the console .Print the number of occurences of the word in the sentance in the 
# following sentence :The word 'x' appers 'y' times .Replace x with word and y with number of occurences.
# Comparison must be case sensitive 

sentence=input()
word_sen=sentence.split(" ")
word=input()
count=0

for i in range(len(word_sen)):
    if(word==word_sen[i]):
        count+=1

print(f"The word {word} appears {count} times")


