#WHAT IS SUPER METHOD?
"""
The super() method in Python is used to call a method from a parent class. 
It is particularly useful in inheritance scenarios where you want to extend the functionality of a parent class method while still utilizing the original implementation.
"""
#SYNTAX OF SUPER METHOD:
"""
class ParentClass:
    def method_name(self):
        # Parent class method implementation
        pass

class ChildClass(ParentClass):
    def method_name(self):
        # Call the parent class method and extend its functionality
        super().method_name()
        # Additional functionality for the child class
        pass
"""
#EXAMPLE OF SUPER METHOD:
class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Manager(Employee):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (Employee)
        print("Constructor of Manager")
    b = 2

class Programmer(Manager):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (Manager)
        print("Constructor of Programmer")
    c = 3

o = Employee()
print(o.a)

o = Manager()
print(o.a, o.b)

o = Programmer()
print(o.a, o.b, o.c)

#OUTPUT:
"""
Constructor of Employee
1
Constructor of Employee
Constructor of Manager
1 2
Constructor of Employee
Constructor of Manager
Constructor of Programmer
1 2 3
"""
