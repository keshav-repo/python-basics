a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
# print(a)

a = "Lorem ipsum dolor sit amet,"+\
"consectetur adipiscing elit,"+"sed do eiusmod tempor incididunt"+"ut labore et dolore magna aliqua."

print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[1])

for ch in a:
    print(ch, end=" ")

print(len(a))

print("Hello" in a)

if("Hi" not in a):
    print("Hi not present")

#8
print(a[2:5])
print(a[:2])
print(a[2:])
print(a[-5:-2])

# 9
a = " Hello, World! "
print(a.strip())
print(a.strip("!"))

# 10
a = "Hello"
b = "World"
c = a + b
print(c)

# 11
quantity = 3
itemno = 567
price = 49.95

myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# 12
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
