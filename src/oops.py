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
        print('Grandfather name : {}, Father name : {}, Son name : {}'.format(self.grandfathername, self.fathername,
                                                                              self.sonname))


s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()


## another example of multi level inheritance
class A():
    def __init__(self, x):
        self.x = x
        print("in class A")


class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y


class C(B):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


c = C(1, 2, 3)
print(c.x)


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


# Another example of Hierarchical inheritance
class Product():
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price


class ElectronicProduct(Product):
    def __init__(self, name, price, memory):
        super().__init__(name, price)
        self.__memory = memory

    def getMemory(self):
        return self.__memory


class Book(Product):
    def __init__(self, name, price, author, page):
        super().__init__(name, price)
        self.__author = author
        self.__page = page

    def getAuthor(self):
        return self.__author

    def getPages(self):
        return self.__page


iphone8 = Product("iphone 8", 40000)
print(iphone8.getPrice())
iphone8.setPrice(35000)
print(iphone8.getPrice())

harryPorter = Book("Harry Potter", 700, "J.K Rowling", 600)
print(harryPorter.getName())
print(harryPorter.getAuthor())


class Phone(ElectronicProduct):
    def __init__(self, name, price, memory, camera):
        super().__init__(name, price, memory)
        self.__camera = camera

    def getCamera(self):
        return self.__camera


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


class D(B, A):
    def __init__(self):
        pass

    def fun(self):
        print("function in D")


d = D()
d.fun()


### multiple inheritance example
class Base():
    def __init__(self):
        print("in base class")


class A(Base):
    def __init__(self):
        super().__init__()
        print("in class A")

    def fun(self):
        print("fun in class A")


class B(Base):
    def __init__(self):
        super().__init__()
        print("in class B")

    def fun(self):
        print("fun in class B")


class Deriver(B, A):  # A, B -> B,A
    def __init__(self):
        super().__init__()
        print("in derived class")


der = Deriver()
der.fun()


# polymorphism using duck typing
class AnimalAction():
    def fly(self, animal):
        animal.fly()


class Bird:
    def fly(self):
        print("fly with wings")


class Airplane:
    def fly(self):
        print("fly with fuel")


class Drone:
    def fly(self):
        print("fly with battery")


bird = Bird()
plane = Airplane()
drone = Drone()
animals = [bird, plane, drone]

for animal in animals:
    animal.fly()

# checking the duck typing in inbuilt function
print(len("abc"))
print(len([1, 2, 3, 4]))


# polymorphism using method overloading
def product(a, b, c=None):
    if c is None:
        return a * b
    else:
        return a * b * c


print(product(10, 2, 3))
print(product(20, 2))

## polymorphism using abstract method
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def sides(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def sides(self):
        return 4


rec = Rectangle(4, 3)
print(rec.area())


class Trapezium(Shape):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def area(self):
        return ((self.a + self.b) * self.h) / 2

    def sides(self):
        5


trap = Trapezium(3, 5, 2)

shapes = [rec, trap]
for shape in shapes:
    print("area is {}".format(shape.area()))
print("")

## polymorphism using operator overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x,y)
    def __str__(self):
        return "x:{}, y: {}".format(self.x, self.y)

p1 = Point(1,2)
print(p1)
p2 = Point(3,4)
p3 = p1 + p2
print(p3)
p4 = p1 -p2
print(p4)

# operator overloading built in method
print(1+2)
print("Hello "+"world")

