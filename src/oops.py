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
    companyName="ABC Company Privated Limited"
    addRess = "101, 5th Floor, Brigade Road, MG Road"
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

emp1=Employee(1, "name1", 100)
print(emp1.deptId)
emp2=Employee(2,"name2")
print(emp2.deptId)

emp1.displayEmployeeInfo()
emp1.setSalary(3000)

print(emp1.getSalary())




