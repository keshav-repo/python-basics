# 2
car={
    "brand": "Tata",
    "Model": "Nexon",
    "Year": 2023
}

# 3
car={
    "brand": "Tata",
    "Model": "Nexon",
    "Year": 2023,
    "Year": 2020
}
print(car)

# 4
print(car["Model"])
print(car.get("Model"))

# 5
print(car.keys())

# 6
car["brand"]="Maruti"

# 7
car.update({"Model": "Dzire"})

# 9
for x in car:
    print(x, end=" ")
for x in car:
    print(car[x], end=" ")
for y in car.values():
    print(y, end=" ")
for key, value in car.items():
    print(value, end=",")

# 11
subjects={
    "chemistry": {
        "name": "Chemistry",
        "pages": 300,
        "standard": "Twelth",
        "cat": ["Organic", "Physical", "inorganic"]
    },
    "physics": {
        "pages" : 300,
        "standard": "Twelth",
        "cat": ["Optics", "Electromagnatics", "Semiconductor"]
    }
}
print(subjects["physics"]["cat"])