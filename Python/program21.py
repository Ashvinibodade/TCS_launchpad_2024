# WAP to read numbers from single line and print the missing numbers .Numbers will be in consecutive order

n=input()
input_num=n.split(" ")
input_num=[int(num) for num in input_num]

begin=input_num[0]
end=input_num[-1]

total_num=[i for i in range(begin,end+1)]

ans=list(set(total_num).difference(set(input_num)))

for i in ans:
    print(i,end=" ")