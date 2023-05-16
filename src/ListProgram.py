languages = ["C", "C++", "Java", "Python", "Scala"]
print(type(languages))
print(languages)

print(languages[3])

languages.append("Fortrain")
print(languages)

print(languages[-2])

sublist = languages[2:5]
print(sublist)
print(languages[:3])
print(languages[5:])
print(languages[-3:-1]) # sublist using negative indexing

if "Scala" in languages:
    print("Scala is present in language")

languages[0] = "html"
print(languages)

# changing the range
languages[0:1]=["css", "Javascript"]
print(languages)

for i in range(0, len(languages)):
    print(languages[i], end=", ")

print("")
languages.insert(0, "typescript")
print(languages)

anotherLanguage = ["English", "Hindi", "Sanskrit"]
languages.extend(anotherLanguage)
print(languages)

languages.remove("Hindi")
languages.pop()
print(languages)
languages.pop(1)
print(languages)

del languages[0]
print(languages)

# languages.clear()
# print(languages)

# using in operator
for language in languages:
    print(language, end=" ")

print("\nprinting using range")
for i in range(len(languages)):
    print(languages[i], end=" ")

i=0
while( i < len(languages)):
    print(languages[i], end=" ")
    i = i+1
print("")

numbers = [4,2,9,0,11,-3]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

languages.sort()
print(languages)

languageCopy = languages.copy();
languages.pop(0)
print(languages)
print(languageCopy)

languageCopy2 = list(languages)
languages.pop(0)
print(languages)
print(languageCopy2)

list3 = languages+numbers
print(list3)

for num in numbers:
    languages.append(num)
print(languages)


