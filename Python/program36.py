#Create a dictionary to take three input from user .Take 3 inputs:
# 1.Number of key:value pair
# 2.keys
# 3.values
# Write a logic to print this dictionary .Now take another input as a value that needs to be searched in the dictionary.
# Then print if that value is present in the dictionary values or not and also convert it into uppercase 

kv=int(input("Enter number of key-value pair:"))
d={}
for i in range(kv):
    key=input("Enter key:")
    value=input("ENter value:")
    d[key]=value
sr=input("Enter the value to be searched:")

if sr in d.values():
    print(d)
    print(f"yes!,{sr.upper()} is present in the dictionary")
else:
    print(d)
    print(f"NO!,{sr.upper()} is not present in the dictionary")
