num1 = 10
num2 = 20

if(num1>num2):
    print("num 1 is greater")
else:
    print("num 2 is greater")

# using conditional operator
num = 15
if num%2==0 and num%5==0:
    print("number is even number and also divisible by 5")
elif(num%2==0): # adding bracket is optional
    print("number is even number")
elif num%5==0:
    print("number is divisible by 5")

# nested if else
num = 10
if num%2==0:
    if num%5==0:
        print("number is even number and also divisible by 5")
        num=100
        num3=7
print(num)
print(num3)
