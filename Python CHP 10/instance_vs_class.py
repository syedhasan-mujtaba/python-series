#CLASS ATTRIBUTE:
"""
Class attributes are variables that are shared among all instances of a class.
They are defined within the class and are accessed using the class name or an instance of the class.
Class attributes are used to store data that is common to all instances (objects) of a class.
In Python, class attributes are defined within the class body, outside of any methods.
They can be accessed using the class name or an instance of the class.
Class attributes can also be modified, but it is generally recommended to use instance attributes for data that is specific to an instance.
"""
#SYNTAX:
"""
class ClassName:
    class_attribute = value  # Class attribute defined here
"""

#INSTANCE (OBJECT) ATTRIBUTE:
"""
Instance attributes are variables that are unique to each instance (object) of a class.
They are defined within the class's __init__ method and are accessed using an instance of the class.
Instance attributes are used to store data that is specific to each instance of a class.
"""
#SYNTAX:
"""
class ClassName:
    def __init__(self):
        self.instance_attribute = value  # Instance attribute defined here
"""
#IMPORTANT NOTE:
"""
Instance attributes, take preference over class attributes with the same name.
If an instance attribute is defined with the same name as a class attribute, the instance attribute will override the class attribute for that specific instance.
"""
#EXAMPLE:
class Employee:
    language = "Python"  # Class attribute

harry = Employee()  # Creating an instance of the Employee class
harry.language = "Javascript"  # Instance attributes (Modifying the instance attribute for harry)
print(harry.language)  # Output: Javascript (Instance attribute takes precedence over class attribute)
