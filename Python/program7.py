# Write a program to read two strings from console str1 and str2 .Write a logic to check if str1 and str2 is
# anagram,print "{str1}=={str2} is true " .If strings are not anagram then print "{str1} =={str2} is false" .An 
# anagram is a word or phrase formed by rearranging the letters of a different word or phrase formed by rearranging
# the letters  of different words and phrases ,typically using all original letters exactly once.


str1=input()
str2=input()

if "".join(sorted(str1))=="".join(sorted(str2)):
    print(f"{str1}=={str2} is true")
else:
    print(f"{str1}=={str2} is false")