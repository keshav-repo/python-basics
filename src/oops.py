# 3,4,5
class Employee:
    empId = 100
    name = None
    dept = None


emp1 = Employee
print(emp1.empId)

emp2 = Employee
print(emp2.empId)


# 5
class Employee:
    def __init__(self, empId, name):
        self.empId = empId
        self.name = name


emp1 = Employee(151, "Emp1")
print(emp1.empId)


# 6
class Employee:
    companyName = "ABC Company Privated Limited"
    address = "101, 5th Floor, Brigade Road, MG Road"

    def __init__(self, empId, name, deptId=20):
        self.empId = empId
        self.name = name
        self.deptId = deptId

    def displayEmployeeInfo(self):
        print("Employee details-> employeeId: {}, name {}, department id {}".format(self.empId, self.name, self.deptId))

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

    @classmethod
    def printComapnyName(cls):
        print(cls.companyName)

    @classmethod
    def printCompanyAddress(cls):
        print(cls.address)

    @staticmethod
    def demo():
        print("this is demo method")


emp1 = Employee(1, "name1", 100)
print(emp1.deptId)
emp2 = Employee(2, "name2")
print(emp2.deptId)

emp1.displayEmployeeInfo()
emp1.setSalary(3000)

print(emp1.getSalary())


class User:
    def __init__(self, username):
        self.__username = username

    def getUserName(self):
        return self.__username

    def setUserName(self, username):
        self.__username = username


user1 = User("user1")
print(user1.getUserName())


class Person:
    def __init__(self, name, address, gender):
        self.name = name
        self.address = address
        self.gender = gender


class Student(Person):
    def __init__(self, name, address, gender, rollNo):
        super().__init__(name, address, gender)
        self.rollNo = rollNo


class Employee(Person):
    def __init__(self, name, address, gender, empId, dept):
        super().__init__(name, address, gender)
        self.empId = empId
        self.dept = dept


e1 = Employee("John", "MG Road", "Male", 100, "Software Engineer")
print(e1.name)


# Python program to demonstrate, multilevel inheritance
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        super().__init__(grandfathername)
        self.fathername = fathername
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        super().__init__(fathername, grandfathername)
        self.sonname = sonname
    def print_name(self):
        print('Grandfather name : {}, Father name : {}, Son name : {}'.format(self.grandfathername, self.fathername, self.sonname) )

s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()


# Hierarchical inheritance
class Parent:
    def __init__(self):
        print("Parent class")
class Child1(Parent):
    def __init__(self):
        print("Child 1 class")
class Child2(Parent):
    def __init__(self):
        print("child 2 class")

## Multiple inheritance
class A:
    def fun(self):
        print("function in A")
class B(A):
    def fun(self):
        print("function in B")
class C(A):
    def fun(self):
        print("function in C")
class D(B,A):
    def __init__(self):
        pass
    def fun(self):
        print("function in D")

d = D()
d.fun()




