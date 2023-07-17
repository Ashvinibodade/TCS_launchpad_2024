# A faculty program stores values from the username and password field as a continuous sequence of characters.When 
# trying to fetch either the username or password,the entire string is displyed.Given the string str ,the task here 
# is to find and extract only the letters and special characters from the whole string stored.

# Note:
# The letters and the special character should be displayed saparately 
# The output should consist of all letters ,followed by all the special characters present in the input string

data=input()
str=[i for i in data if i.isdigit()==False]
special=[i for i in str if i.isalpha()==False ]
str=[i for i in str if i.isalpha()==True ]

p="".join(str)+"".join(special)
print(p)