#On various type of access specifier

#PUBLIC ACCESS MODIFIER
class employee:
    def __init__(self,name,sal):
        self.name=name
        self.salary=sal

e1=employee('Kiran',10000)
print(e1.salary)
e1.salary=20000
print(e1.salary)

#PROTECTED ACCESS MODIFIER :USE _(SINGLE UNDERSCORE)
class employee1:
    def __init__(self,name,sal):
        self._name=name
        self._salary=sal

e2=employee1('Kiran',10000)
print(e2._salary)
e2._salary=20000
print(e2._salary)

#PRIVATE ACCESS MODIFIER : USE __(DOUBLE UNDERSCORE)
class employee2:
    def __init__(self,name,sal):
        self.__name=name
        self.__salary=sal

# e3=employee2('Kiran',10000)
# print(e1.__salary)     #Due to private access modifier we cant access them directly
# e3.__salary=20000
# print(e1.__salary)

e3=employee2('Kiran',10000)
e3._employee2__salary=2222
print(e3._employee2__salary)


