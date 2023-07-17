# Write a program to take a float input from console as Salary.Print the salary with hike.If salary  is 
# greater than or equal to 10000 ,hike should 10% of the salary,If salary is greater than or equal to 6000 and 
# less than 10000,hike should be 8%  of the salary .If the salary is less than 6000 ,hike should be 5% of the salary .
# Round the updated salary to 2 digits

salary=float(input())

if(salary>=10000):
    salary=salary+(salary*0.1)
elif (salary>=6000 and salary<10000):
    salary=salary+(salary*0.08)
elif(salary<6000):
    salary=salary+(salary*0.05)

salary=round(salary,2)
print(salary)