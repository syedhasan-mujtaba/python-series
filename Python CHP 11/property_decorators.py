#WHAT IS PROPERTY DECORATORS?
"""
Property decorators in Python are used to define methods that can be accessed like attributes,
providing a way to encapsulate the access to an attribute and add additional logic when getting, setting, or deleting it.
"""
#SYNTAX OF PROPERTY DECORATORS:
"""
class MyClass:
    def __init__(self):
        self._attribute = None  # Private attribute

    @property
    def attribute(self):
        # Getter method for the property
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        # Setter method for the property
        self._attribute = value

    @attribute.deleter
    def attribute(self):
        # Deleter method for the property
        del self._attribute
"""
#EXAMPLE OF PROPERTY DECORATORS:
class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"Class attribute a: {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname, self.lname = value.split(" ")

e = Employee()
e.a = 2

e.name = "John Doe"
print(e.fname)  # Output: John
print(e.lname)  # Output: Doe

e.show()

#CONCEPT OF ABSTRACTION AND ENCAPSULATION:
"""
Abstraction is the process of hiding the internal details of an object and exposing only the necessary information.
Encapsulation is the practice of bundling the data and methods that operate on that data within a single unit (class), restricting direct access to some of the object's components.
"""
