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

