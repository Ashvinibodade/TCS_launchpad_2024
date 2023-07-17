# WAp to create a student record ,which will give us final report in the form of tuple ,displaying all the 
# records of the students

sc=int(input("Enter student count:"))
list=[]
for i in range(sc):
    marks=[]
    sn=input("Enter name:")
    srn=input("Enter rollno:")
    m=int(input("Enter number of subject :"))
    for j in range(m):
        ms=int(input("Enter marks:"))
        marks.append(ms)
    ty=(sn,srn,marks)
    list.append(ty)

fl=tuple(list)
print(f"final data:{fl}")


