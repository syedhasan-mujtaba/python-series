#DEFINITION OF CLASS:
"""
Class is a blueprint for creating objects.
It defines a set of attributes and methods that the created objects will have.
In Python, classes are defined using the 'class' keyword followed by the class name and a colon.
The attributes are defined within the class, and methods are defined as functions within the class.
Classes can also inherit from other classes, allowing for code reuse and organization.
"""
#SYNTAX:
"""
class ClassName:
    # class attributes
    attribute1 = value1
    attribute2 = value2
    
    # constructor method:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    # other methods:
    def method1(self):
        # method implementation
        pass   
"""

#EXAMPLE:
class Employee:
    # class attributes
    name = "Harry"
    language = "Python"
    salary = 50000

    harry = Employee()  # creating an object of the class Employee
    print(harry.name)  # accessing the class attribute 'name' using the object 'harry'
    print(harry.language)  # accessing the class attribute 'language' using the object 'harry'
    print(harry.salary)  # accessing the class attribute 'salary' using the object 'harry'

#ABSTRACTIONS AND ENCAPSULATION:
"""
Abstraction is the process of hiding the internal details of an object and showing only the essential features.
Encapsulation is the process of bundling the data and methods that operate on that data within a single unit (class).
"""