#MULTIPLE INHERITANCE:
"""
Multiple inheritance is a type of inheritance where a child class inherits from multiple parent classes.
"""
#SYNTAX OF MULTIPLE INHERITANCE:
"""
class ParentClass1:
    # Parent class 1 attributes and methods
    pass

class ParentClass2:
    # Parent class 2 attributes and methods
    pass

class ChildClass(ParentClass1, ParentClass2):
    # Child class attributes and methods
    pass
"""
#EXAMPLE OF MULTIPLE INHERITANCE WITH OVERRIDING:
class Employee:
    company = "ABC Corporation"
    def show(self):
        print(f"Company: {self.company}")

class Coder:
    language = "Python"
    def showLanguage(self):
        print(f"Programming Language: {self.language}")        

class Programmer(Employee, Coder):
    company = "XYZ Corporation"
    def showLanguage(self):
        print("Programming Language: Python")

a = Employee()
c = Coder()
b = Programmer()

print(f"a.company: {a.company}")
print(f"b.company: {b.company}")
print(f"c.language: {c.language}")
print(f"b.language: {b.language}")

#OUTPUT:
"""
a.company: ABC Corporation
b.company: XYZ Corporation
c.language: Python
b.language: Python
"""