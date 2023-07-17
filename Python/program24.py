#WAP to search input value in a list.Create a list by taking input from user.
# Also check if the search value is numeric and string

n=int(input("Enter"))
l=[]
flag=0
for i in range(n):
    l.append(int(input()))

search_ele=int(input("Enter the element to be searched:"))


if search_ele in l:
    flag+=1
if str(search_ele).isdigit():
    print(search_ele,"is Numeric")
else:
    print(search_ele,"is string")

if flag!=0:
    print("YES!",search_ele,"exists in list",l)
else:
    print("NO!",search_ele,"is no exists in list",l)