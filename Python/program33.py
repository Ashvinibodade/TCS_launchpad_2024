# WAP to sort tuple by number of digits(in asending order)

yt=input("Enter comma separated elements in the list:")

yt=list(yt.split(","))
yt.sort(key=len)
print(yt)