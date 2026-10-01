#STATIC METHOD:
"""
A static method is a decorator that belongs to a class rather than an instance of the class.
It does not receive the self parameter and cannot access the instance or class attributes.
"""
#SYNTAX:
"""
@staticmethod
def method_name():
    # Method body
"""
#EXAMPLE:
class Employee:
    language = "Python"  # Class attribute

    @staticmethod
    def greet():
        print("Good Morning!")
#OUTPUT:
"""
Employee.greet()  # Output: Good Morning!
"""

#IMPORTANT NOTE:
"""
Static methods are useful when you want to define a method that belongs to a class but doesn't need to access the instance or class attributes.
"""