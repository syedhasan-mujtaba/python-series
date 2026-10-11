#MULTILEVEL INHERITANCE:
"""
Multilevel inheritance is a type of inheritance where a child class inherits from a parent class, and another child class inherits from the first child class.
"""
#SYNTAX OF MULTILEVEL INHERITANCE:
"""
class ParentClass:
    # Parent class attributes and methods
    pass

class ChildClass1(ParentClass):
    # Child class 1 attributes and methods
    pass

class ChildClass2(ChildClass1):
    # Child class 2 attributes and methods
    pass
"""
#EXAMPLE OF MULTILEVEL INHERITANCE WITH OVERRIDING:
class Employee:
    company = "ABC Corporation"
    def show(self):
        print(f"Company: {self.company}")

class Coder(Employee):
    language = "Python"
    def showLanguage(self):
        print(f"Programming Language: {self.language}")        

class Programmer(Coder):
    company = "XYZ Corporation"
    def showLanguage(self):
        print("Programming Language: Python")
        print(f"Company: {self.company}")

a = Employee()
b = Coder()
c = Programmer()

print(f"a.company: {a.company}")
print(f"b.company: {b.company}")
print(f"c.company: {c.company}")
print(f"b.language: {b.language}")
print(f"c.language: {c.language}")

#OUTPUT:
"""
a.company: ABC Corporation
b.company: ABC Corporation
c.company: XYZ Corporation
b.language: Python
c.language: Python
"""
