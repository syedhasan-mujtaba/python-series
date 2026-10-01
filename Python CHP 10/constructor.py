#__INIT__() CONSTRUCTOR:
"""
The __init__() method is a special (dunder) method in Python classes that is automatically called when an object of the class is created.
It is used to initialize the attributes of the object. It is commonly referred to as the constructor of the class.
It takes self argument and can take further arguments to initialize the object with specific values.
"""
#SYNTAX:
"""
def __init__(self, other_parameters):
    # Initialization code
"""
#EXAMPLE:
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayInfo(self):
        print(f"Name: {self.name}, Age: {self.age}")
#OUTPUT:
"""
emp1 = Employee("Alice", 30)
emp1.displayInfo()  # Output: Name: Alice, Age: 30
"""

#IMPORTANT NOTE:
"""
In __init__() method, the self parameter is a reference to the current instance of the class.
It is used to access the attributes and methods of the class.
The self parameter is automatically passed to the __init__() method when an object is created, and it allows you to set the initial state of the object.
The __init__() method can take additional parameters to allow for more flexible object initialization.
"""
#WARNING:
"""
We should not return any value from the __init__() method. If we try to return a value, it will raise a TypeError.
We should add an argument to the __init__() method if we want to initialize the object with specific values otherwise, we can use default values for the parameters.
"""

#WHAT ARE DUNDER METHODS?
"""
Dunder methods (short for "double underscore" methods) are special methods in Python that have double underscores at the beginning and end of their names.
They are also known as magic methods or special methods.
These methods are called automatically by Python in response to specific operations on objects of a class.
Examples of dunder methods include __init__, __str__, __repr__, __add__, etc.
"""

#DIFFERENCE BETWEEN A PARAMETER AND AN ARGUMENT:
"""
A parameter is a variable defined in the function definition, while an argument is the actual value passed to the function when it is called.
In the context of __init__(), parameters are the variables defined in the method signature, and arguments are the values passed when an object of the class is created.
"""
