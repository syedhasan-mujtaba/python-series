#WHAT IS INHERITANCE?
"""
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (called a child or subclass) 
to inherit attributes and methods from another class (called a parent or superclass).
This promotes code reusability and establishes a hierarchical relationship between classes.
"""
#TYPES OF INHERITANCE:
"""
1. Single Inheritance: A child class inherits from a single parent class.
2. Multiple Inheritance: A child class inherits from multiple parent classes.
3. Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another parent class.
4. Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
5. Hybrid Inheritance: A combination of two or more types of inheritance.
"""
#SYNTAX OF INHERITANCE:
"""
class ParentClass:
    # Parent class attributes and methods
    pass

class ChildClass(ParentClass):
    # Child class attributes and methods
    pass
"""
#IMPORTANCE OF INHERITANCE:
"""
1. Code Reusability: Inheritance allows you to reuse existing code, reducing redundancy and promoting maintainability.
2. Extensibility: You can extend the functionality of existing classes by creating new subclasses.
3. Polymorphism: Inheritance enables polymorphism, allowing objects of different types to be treated uniformly.
"""
#IMPORTANT POINTS TO REMEMBER:
"""
1. The child class inherits all attributes and methods from the parent class.
2. The child class can override or extend the functionality of the parent class.
3. Inheritance promotes code reusability and maintainability.
"""
#IMPORTANT TERMS IN INHERITANCE:
"""
1. Parent Class: The class from which attributes and methods are inherited.
2. Child Class: The class that inherits attributes and methods from the parent class.
3. Super() Function: A function used to call the parent class's methods and constructors.
4. Override: The process of redefining a method in the child class with a different implementation.
"""
#IMPORTANT NOTES:
"""
1. Inheritance is a key feature of object-oriented programming that allows for the creation of a class hierarchy.
2. The parent class is also known as the base class or superclass.
3. The child class is also known as the derived class or subclass.
"""
#WARNING:
"""
1. Inheritance can lead to complex class hierarchies that are difficult to maintain.
2. Overuse of inheritance can result in tight coupling between classes.
3. It's important to use inheritance judiciously and consider composition as an alternative.
"""