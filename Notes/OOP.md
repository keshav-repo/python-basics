# Object Oriented Programming

1. Object oriented Programming: It is programming design/methodology that binds together data and function associated 
 with object.
2. OOPs Concepts: \
    Class \
    Objects \
3. Class: It is used defined data type. It consists of data and function. 
   Example: a) Car is the class, and wheels, speed limits, mileage are their properties. Function can be move forward, take 
   left etc. \
   b) Bulb  c) Dog  e) Employee
4. Object: Object is a instance of class 
5. dot(.) is used to access the properties of object.
5. Initializer: When we need to give our custom initialisation to object, we use initializer. __init__ is the method name 
   used to initialize object. 
6. We can give default Initializer to a argument. This way argument becomes optional. 
7. self: self represents the instance of the class. By using the “self”  we can access the attributes and 
    methods of the class in python. The first argument of every class method, including init, is always 
    a reference to the current instance of the class.  By convention, this argument is always named self. 
    In the init method, self refers to the newly created object; in other class methods, 
    it refers to the instance whose method was called.
8. class and instance variable: class variable is a variable of class. Every object in class will have same value for class 
   variable. Every object will have a seperate copy of instance variable. Instance variable are defined inside initializer. 
   It can be modified  inside instance parameter and using instances. 
9. Methods in class \
   a) instance \
   b) class method are used to access and modify class level variable \
   c) static method is used as a utility method. It has nothing to do with class and instance level variable. And static method
     is not inherited. 
10. Passing default value: 
11. Encapsulation: Encapsulation is a mechanism of wrapping the data (variables) and code acting on the data (methods)
     together as a single unit. It is done to hide the sensitive information from outer world. It is generally achieved 
     by making all the variable private and using getter and setter to access and modify the values. \
     To make a variable private,we can use double underscore (__) \
     Best approach to expose only those method and variable which are need.
12. Inheritance: Inherit the properties method from parent class 
13. super() keyword is used to access parent class variable and method if accessible. 
14. types of inheritance \
    a) Single \
    b) Multi lavel: When a class can be derived from more than one base class this type of inheritance is called multiple inheritances. \
        <img height="300" src="https://media.geeksforgeeks.org/wp-content/uploads/20200108144705/Multilevel-inheritance1.png" width="300"/>\
    c) Hierarchical inheritance: A single base class can have multiple derived classes, and other subclasses can further inherit these derived classes, forming a hierarchy of classes ![](https://www.simplilearn.com/ice9/free_resources_article_thumb/Hierarchical_Inheritance_In_C_P_P_Chart.png) \
    d) Multiple \
       <img height="300" src="https://media.geeksforgeeks.org/wp-content/uploads/20191222084630/multipleinh.png" width="300"/> \
    e) Hybrid: It is mix of two or more type of inheritance
15. pass: The pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
16. Diamond Problem: \
   <img height="300" src="https://media.geeksforgeeks.org/wp-content/uploads/20191222084637/Diamond1.png" width="300"/>
17. Advantage of inheriance: a) Reusibility b) Low development time 
18. Polymorphism: The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
    four ways we can achieve polymorphism in python \
    i. Duck typing: Due to dynamic nature of python, passed argument don't need to be a subclass of a particular class. Only it has to implement thhe method \
    ii. Method overloading \
    iii. Operator overloading: This can be achieved by implementing corresponding method of operator. [Details here](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types) \
    iv. method overiding 
20. Duck Typing: Duck typing is a concept related to dynamic typing, where the type or the class of an object is less important than the methods it defines. When you use duck typing, you do not check types at all. Instead, you check for the presence of a given method or attribute.
21. __str__(): The __str__() method returns a human-readable, or informal, string representation of an object. Default value is the pointer of object. 

Question based on oops concept
1. Create classes for Product. Consider example from amazon and flipkart ? 
   Notes: Consider electronics, Books, Pet Supplies.  
2. Create classes for account that is used for auth and authorisation ? 
    Conside account in a organisation. 
3. Design all the classes in [cardekho](https://www.cardekho.com/jeep/grand-cherokee-l-2022) website 


Images reference from [geeksforgeeks](https://www.geeksforgeeks.org/types-of-inheritance-python/)
