# John in ABC college.Principle of clg wants to create gr of all the students based on following criteria:
# 1.student must have A grade 
# 2.student must have join the college before 2020
# 3.students age must be greater than 18

# marks>=80 should have grade A

# Write a program to check if the input student id is eligible to be a part of group or not

# if eligible the print {students age}:True
# else print{students age}:False

marks=int(input("Enter:"))
year=int(input("Enter:"))
age=int(input("Enter:"))

if (marks>=80 and year<2020 and age>18):
    print("{} :true".format(age))
else:
    print("{} :false".format(age))