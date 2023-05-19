**Dictinary**

1. Dictinary are used to store data in key value format. Dictionaries allow us to associate a value to a unique key, and then to quickly access this value. It's a good idea to use them whenever we want to find (lookup for) a certain Python object.
2. curley bracket {} is used to initialise it.
```
car={
    "brand": "Hyundai",
    "Model": "i10",
    "Year": 2020
}
```
Create a new dict with brand Tata, model Nexon and year 2023.
3. Does not allow dublicate key. I we put same key, it will replace value corresponding to it. 
4. Print the value for brand ? \
   Note: We can get value corresponding to key using square bracket or get() method 
5. Print all the keys of car dictionary ? \
   Note: keys() method is used to get all keys in dictionary.
6. To change the value for a existing key
```
car["brand"]="Maruti"
```
Another way of achieving this is using update method 
```
car.update({"Model": "Dzire"})
```
change the model year to 2022 ? 
7. Add a new key called color with value Blue ? 
   We can use same operation as we did in changing the value. 
8. Remove the last and first item added in the car ? 
   Note: pop(<X>) remove the element with the key as X, popitem() removed the element which is coming last 
9. Looping in the dictionary \
   Looping keys 
   ```commandline
        for x in car:
            print(x, end=" ")
   ```
   Looping values \
```commandline
for x in car:
    print( car[x], end=" ")
for y in car.values():
    print(y, end=" ")
```
Looping key and values together 
```commandline
for key, value in car.items():
    print(value, end=",")
```
**Q.** Try to loop key and values in dictionary crearted in step 1 ? 
10. Create a copy of dictionary with variable name carCpy ? 
   Note: copy() or dict() can be used to created copy 
11. Created a dictionary about company having division and employee information. employee data should be nested in
    division information. And print the employees name which has maxiumum employees. \
    Note: Nested Dictionary example: 
```commandline
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
```
