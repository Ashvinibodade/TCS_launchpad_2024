class student:
    def __init__(self,sid,sname,cname,score):
        self.studentid=sid
        self.studentname=sname
        self.courseEnrolled=cname
        self.studentscore=score


class Department:
    def __init__(self,dname,slist):
        self.departmentname=dname
        self.studentlist=slist

    def findCourseWiseStudent(self):
        result={}
        clist=[]
        for student in self.studentlist:
            clist.append(student.courseEnrolled)
        courselist=list(set(clist))
        for course in courselist:
            result[course]=clist.count(course)
        return result
    
    def findStudentGrade(self,sid):
        grade=None
        for student in self.studentlist:
            if student.studentid==sid:
                if student.studentscore>=80:
                    grade='A'
                elif student.studentscore>=65:
                    grade='B'
                elif student.studentscore>=55:
                    grade='C'
                else:
                    grade='F'
        return grade
    
if __name__=='__main__':
    count=int(input())
    slist=[]
    for i in range(count):
        sid=int(input())
        sname=input()
        course=input()
        score=float(input())
        slist.append(student(sid,sname,course,score))
    d=Department("Humanities",slist)
    inputId=int(input())
    outDict=d.findCourseWiseStudent()
    for course in sorted(outDict.keys()):
        print(course,outDict[course])
    outGrade=d.findStudentGrade(inputId)
    if outGrade is None:
        print('No student found')
    else:
        print(outGrade)