class User:
    def __init__(self, username, password, name):
        self.__username = username
        self.__password = password
        self.__name = name
    def getUserName(self):
        return self.__username
    def getName(self):
        return self.__name
    def checkAuth(self, username, password):
        if self.__username == username and self.__password == password:
            print("Successful login")
        else:
            print("Wrong credentials")

class Student(User):
    def __init__(self, username, password, name, rollNo):
        super().__init__(username, password, name)
        self.__rollNo = rollNo
    def getRollNo(self):
        return self.__rollNo
    def displayStudentInfo(self):
        print("student name is {}, roll no: {}".format(self.getName(), self.__rollNo))

class PG_Student(Student):
    def __init__(self, username, password, name, rollNo, courseLenInYears):
        super().__init__( username, password, name, rollNo)
        self.__courseLenInYears = courseLenInYears
    def getCourseLenInYears(self):
        return self.__courseLenInYears
    def displayStudentInfo(self):
        print("student name is {}, roll no: {}, courseLenInYears {}".format(self.getName(), self.getRollNo(), self.__courseLenInYears))

class UG_sutudent(Student):
    def __init__(self, username, password, name, rollNo, subjects):
        super().__init__(username, password, name, rollNo)
        self.__subjects = subjects
    def getSubjects(self):
        return self.__subjects
    def displayStudentInfo(self):
        print("student name is {}, roll no: {}".format(self.getName(), self.getRollNo()))
        print("Subjects are")
        for subject in subjects:
            print(subject, end=",")

subjects = ["ISS", "ISB", "Maths", "ISB 208L"]
s1 = UG_sutudent("John","pass", "John Smith", 102, subjects )
anomal = UG_sutudent("anmol", "pass5", "Anmol Viswanath", 123 , subjects)
adithya = UG_sutudent("adithya", "pass6", "Adithya Prasad", 124, subjects)
subjects = ["AI", "Data Science", "Machine Learning", "Mathematics 4"]
nathan = PG_Student("Nathan", "pass7", "Nathan Smith", 125, subjects)
mitali = PG_Student("Mithali", "pass8", "Mitali ", 126, subjects)

students = [s1, anomal, adithya, nathan, mitali]
for stud in students:
    stud.displayStudentInfo()

class Professor(User):
    def __init__(self, username, password, name, expertise):
        super().__init__(username, password, name)
        self.__expertise = expertise
    def getExpertise(self):
        return self.__expertise

class GuestProfessor(Professor):
    def __init__(self, username, password, name, expertise, weeklyAppearence):
        super().__init__(username, password, name, expertise)
        self.__weeklyAppearence = weeklyAppearence
    def getWeeklyAppearence(self):
        return self.__weeklyAppearence
    def aboutProfessor(self):
        print("Guest professor name is {} and his expertise is {} and his weekely appearence is ".format(self.getName(), self.getExpertise(), self.getWeeklyAppearence() ))

class FullTimeProfessor(Professor):
    def __init__(self, username, password, name, expertise, hiredYear):
        super().__init__(username, password, name, expertise)
        self.__hiredYear = hiredYear
    def getHiredYear(self):
        return self.__hiredYear
    def aboutProfessor(self):
        print("Full time professor name is {} and his expertise is {} started from {}".format(self.getName(), self.getExpertise(), self.getHiredYear() ))

john = GuestProfessor("John","pass", "John Smith","Mathematics", 4)
james = FullTimeProfessor("James", "pass2", "James Speed", "English", 2020)
harry = GuestProfessor("Harry", "pass3", "Harry Brown", "History", 2)
brandy = FullTimeProfessor("brandy", "pass4", "Brandy Allision", "Physics",2018 )

professors = [john, james, harry, brandy]
for prof in professors:
    prof.aboutProfessor()


# s1 = PG_Student("John","pass", "John Smith", 102, 2 )
# s1.displayStudentInfo()

# s1 = Student("John","pass", "John Smith", 102 )
# s1.displayStudentInfo()

# u1 = User("John", "pass")
# print(u1.getUserName())
#
# u1.checkAuth("John", "pass")


