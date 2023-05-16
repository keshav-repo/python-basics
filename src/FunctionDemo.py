# def is used to define a function
def my_function():
  print("Hello from a function")

# calling a function
my_function()

# we are passing string argument in function
def printName(name):
    print(name)

printName("John Dee")

minimum = min(101, 11, 1000) # inbuilt function
print(minimum)

def fun():
    print("something")
    variable =  10

fun()
#print(variable) # variable defined inside the function is destroyed when called from outside

firstName="john"
def fun():
    print("something")
    firstName =  "doe"

fun()
print(firstName)

score = 80
def fun():
    print("changing score value")
    score = 100

fun()
print(score)

