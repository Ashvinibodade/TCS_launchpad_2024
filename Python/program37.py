# WAP to take input from user (irrespective of datatype) and store it in the list and print sorted list first in
# asending order than in desending order

yt=input("Enter comma separated elements in the list:")

yt=list(yt.split(","))

# specially for integer type of data
# yt=list(map(int,yt.split(",")))

a=sorted(yt)
b=sorted(yt ,reverse=True)

print(f"Ascending order:{a}")
print(f"Desending order:{b}")