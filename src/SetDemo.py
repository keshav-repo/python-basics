fruits = { "cherry","apple", "banana", "apple"}

fruits.add("Guava")
print(fruits)

fruits.add("Watermelon")
print(fruits)

emptySet = set()
print(emptySet)

language =set({"English", "Hindi", "Marathi"})
print(language)

language.add("kannada")
print(language)

language.update(["java", "C", "C++"])
print(language)

language.discard("java")
print(language)

for lang in language:
    print(lang, end=",")

setA = {1,2,4,7,3}
setB = {3,6,8}

print("")

setUnion = setA.union(setB)
print(setUnion)

setIntersection = setA.intersection(setB)
print(setIntersection)

setDiff = setA.difference(setB)
print(setDiff)



