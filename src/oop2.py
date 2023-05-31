"""
data , function
oop

code make my trip -> tons of code

Class ->
Object ->

Car ->properties: Whells , enginer, color, milage
    function: goForward, TakeLaft, horn,

Bulb: filamant , glass , power,
   Function:  turnOn, turuOff

Dog: color, legs, head,
     run, walk, bark

Employee: empId, name, dept
          work,

ABC private limited
20th Main, 3rd Cross, MG Road, Bangalore

20 employee

employee1 =
employee2 =
employee3 =

variable: class level -> class level
variable: instance level -> unique for every object

self -> this is first argument in class level method

__init__ -> Initilizer -> initi the variable

"""

# class Employee():
#     companyName="ABC private limited"
#     address="20th Main, 3rd Cross, MG Road, Bangalore"
#     def __init__(self, empId, name):
#         self.empId = empId
#         self.name = name
#     def displayEmpInfo(self):
#         print("empId {}, name {}".format(self.empId, self.name))
#


# anmol = Employee(1, "Anmol")
#
# print(anmol.empId)
# print(anmol.name)
# print(anmol.companyName)
# anmol.displayEmpInfo()
#
# keshav = Employee(2, "Keshav")
# print(keshav.empId, keshav.name)
# print(keshav.companyName)
# keshav.displayEmpInfo()

"""
methods: 
1. Instance method 
2. class level method: 
3. static method 
"""

# class Employee():
#     companyName="ABC private limited"
#     address="20th Main, 3rd Cross, MG Road, Bangalore"
#     def __init__(self, empId, name):
#         self.empId = empId
#         self.name = name
#     def displayEmpInfo(self):
#         print("empId {}, name {}".format(self.empId, self.name))
#
#     @classmethod
#     def displayCompanyInfo(cls):
#         print("comapny name is {} and address is {}".format(cls.companyName, cls.address) )
#
#     @staticmethod
#     def parseDate(date):
#         print("paring the date"+str(date))
#
# emp1 = Employee(100, "John")
# emp1.displayEmpInfo()
# emp1.displayCompanyInfo()
# emp1.parseDate(" 26 May, 2023")
# Employee.displayCompanyInfo()
# Employee.parseDate(" 26 May, 2023")

# class Employee():
#     companyName="ABC private limited"
#     address="20th Main, 3rd Cross, MG Road, Bangalore"
#     def __init__(self, empId, name=None, deptId=100):
#         self.empId = empId
#         self.name = name
#         self.deptId = deptId
#     def setName(self, name="name"):
#         self.name = name
#
# emp1 = Employee(101)
# emp1.setName()
# print(emp1.name)
# emp2 = Employee(2, "John")
# print(emp2.deptId)
# emp3 = Employee(2, "John",90)
# print(emp3.deptId)

"""
username 
password 
encapsulate data -> related method 
Needed -> we will expose those 

private variable 
custom method -> set, access the value 

__ -> private 
custom method -> set the private variable, 
custom method -> fetch the private method 
"""

# class User():
#     def __init__(self, username, password, dob, gender, phonenumber):
#         self.__username = username
#         self.__password = password
#         self.__dob = dob
#         self.__gender = gender
#         self.__phonenumber = phonenumber
#
#     def setUserName(self, userName):
#         self.__username = userName
#     def getUserName(self):
#         return self.__username
#     def printUserInfo(self):
#         print("username: {}, dob {}, gender {}, phoneNumber: {}".format(self.__username,self.__dob, self.__gender, self.__phonenumber ))
#
#
# john = User("john", "pass1234", "20 March, 1985", "Male", "xxxxxxxx")
# # print(john.__password)
# # john.username = "Alpha"
# print(john.getUserName())
# john.printUserInfo()

"""
obj 1 -> some properties 

obj2 -> some same properties 



"""

class Person():
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
    def getName(self):
        return self.__name
    def getGender(self):
        return self.__gender

class Employee(Person):
    def __init__(self, name, gender, empId):
        super().__init__(name, gender) # called parent constructor
        self.empId = empId

class Student(Person):
    def __init__(self, name, gender, rollNo):
        super().__init__(name, gender)
        self.rollNo = rollNo

emp1 = Employee("John", "Male", 100)
print(emp1.getName())

student = Student("Rahul", "Male", 10)
print(student.getGender())

class Product():
    def __init__(self, name, price ):
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
    def __init__(self,  name, price, memory, camera):
        super().__init__(name, price,memory)
        self.__camera = camera
    def getCamera(self):
        return self.__camera

# , memory, dimesions, color, batteryLife, features, warrenty

"""


"""

## mult level inheritance
class A():
    def __init__(self, x):
        self.x = x
        print("in class A")

class B(A):
    def __init__(self,x, y):
        super().__init__(x)
        self.y = y
class C(B):
    def __init__(self,x, y, z):
        super().__init__(x,y)
        self.z = z

c = C(1,2,3)
print(c.x)


### multiple inheritance
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
class Deriver(B, A): # A, B -> B,A
    def __init__(self):
        super().__init__()
        print("in derived class")

der = Deriver()
der.fun()

"""

1+2 = 3 


"""

a = 1+1
print(a)

b = "a"+"b"
print(b)

print("hello", end=",")
print("world")

"""
Shape 
1. Circle 
2. Square
3. Rectangle 
4. Trapazium 

shapes = [circle, square, rec, trap]

"""


"""
1. 
collage management portal
User -> Student , Professor, Security Guard, Dean 
user-> name, userid
Professor -> no. of classes, expertise
Dean -> 

2. https://www.cardekho.com/
car -> electric, cng car , petrol, Diesel 
Used car
New Car

city-> 
login -> phoneno
Language -> 
article -> author, content, picture 

 


"""










