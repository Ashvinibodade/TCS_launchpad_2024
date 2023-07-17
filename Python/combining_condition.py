# Check the given numberr is even natural or odd natural or if not then even or odd

num=int(input("Enter:"))

# if num>0:
#     if num%2==0:
#         print("Number is even natural")
#     else:
#         print("Number is odd natural")
# elif num==0:
#     print("Number is zero")
# else:
#     if num%2==0:
#         print("Number is even")
#     else:
#         print("Number is odd")

if num%2==0 and num>0:
    print("Number is even natural")
elif num%2!=0 and num>0:
    print("Number is odd natural")
elif num%2==0 and num<0:
    print("Number is even ")
elif num%2!=0 and num<0:
    print("Number is odd")