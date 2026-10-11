#SINGLE INHERITANCE:
"""
Single inheritance is a type of inheritance where a child class inherits from a single parent class.
"""
#SYNTAX OF SINGLE INHERITANCE:
""" 
class ParentClass:
    # Parent class attributes and methods
    pass

class ChildClass(ParentClass):
    # Child class attributes and methods
    pass
"""
#EXAMPLE OF SINGLE INHERITANCE WITH OVERRIDING:
class Employee:
    company = "ABC Corporation"                #THIS IS A CLASS ATTRIBUTE (ALSO CALLED PROPERTY)
    def show(self):
        print(f"Company: {self.company}")

class Programmer(Employee):
    company = "XYZ Corporation"
    def showLanguage(self):
        print("Programming Language: Python")

a = Employee()
b = Programmer()

print(f"a.company: {a.company}")
print(f"b.company: {b.company}")

#OUTPUT:
"""
a.company: ABC Corporation
b.company: XYZ Corporation
"""