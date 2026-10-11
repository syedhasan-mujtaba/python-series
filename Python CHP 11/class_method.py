#WHAT IS A CLASS METHOD?
"""
A class method is a method (decorator) that is bound to the class and not the instance of the class.
It can access and modify the class state that applies across all instances of the class.
"""

#SYNTAX OF A CLASS METHOD:
"""
class MyClass:
    @classmethod
    def class_method(cls):
        # Code for the class method
        pass
"""

#EXAMPLE OF A CLASS METHOD:
class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"Class attribute a: {cls.a}")

e = Employee()
e.a = 2
e.show()  # Output: Class attribute a: 1 

""" The output is 1 because the class method accesses the class attribute 'a' using 'cls.a',
which refers to the class itself, not the instance.
"""