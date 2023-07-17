# create simple  oops based program which reads, store the data into objects
# Creating multiple entries as per the real time requirement -Employee and Organization and keeping the propertise
# (variables/data members ) ,constructor,behaviour (methods/member function) under the right entry (class design) and
# defining the methods to access the data members using the object and object creation

class Employee:
    def __init__(self,name,id,age,gender):
        self.eid=id
        self.ename=name
        self.age=age
        self.gender=gender

class Organization:
    def __init__(self,name,elist):
        self.oname=name
        self.elist=elist

    def addEmp(self,id,name,age,gender):
        print("In add employee function")
        e=Employee(id,name,age,gender)
        self.elist.append(e)
        print("End add employee function")

    def viewEmp(self):
        print("In view employee function")
        for e in self.elist:
            print(e.eid)
            print(e.ename)
            print(e.age)
            print(e.gender)
        print("End view employee function")

    def getEmpCount(self):
        print("In count employee function")
        print("End count employee function")
        return len(self.elist)
    
    def findEmpAge(self,id):
        print("In find employee function")
        age=-1
        for e in self.elist:
            if e.eid==id:
                age=e.age
                break
        print("End find employee function")
        return age
    
    def countEmp(self,age):
        count=0
        print("In count employee age wise func")
        for e in self.elist:
            if e.age>age:
               count+=1 
        print("End count employee age wise func")
        return count
    
if __name__=='__main__':
    employees=[]
    o=Organization('ABC',employees)
    n=int(input())
    for i in range(n):
        name=input()
        id=int(input())
        age=int(input())
        gender=input()
        o.addEmp(name,id,age,gender)

    o.viewEmp()
    
    print(o.getEmpCount())

    id=int(input())
    print(o.findEmpAge(id))

    age=int(input())
    print(o.countEmp(age))