#In a game of scrabble,in order to avoid over-usage of the same letters in any word,Mario is trying to calculate 
# if a letter appers more than three times in any word and wants to discard such word .In order to asssit Mario,
# write a program to identify a number of times the most repeating letter would apper with any word.If the output 
# number is more than three ,Mario shall discard such words and choose another word for the game  

# using list comprehension
data=input()
freq=[data.count(i) for i in data]
print(max(freq))

# without list comprehension
data1=input()
freq1=[]
for i in data1:
    freq1.append(data1.count(i))
print(max(freq1))