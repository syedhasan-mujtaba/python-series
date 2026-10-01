#SELF PARAMETER:
"""
The self parameter is a reference to the current instance of the class.
It is the first parameter of any method defined in a class and is used to access the attributes and methods of the instance.
"""
#SYNTAX:
"""
def method_name(self, other_parameters):
    # Method body
"""
#EXAMPLE:
class Employee:
    language = "Python"  # Class attribute

    def getInfo(self):
        print(f"Language: {self.language}")  # Accessing the class attribute using self

    def greet(self):
        print("Good Morning!")

#NOTE: 
"""
Using the self parameter is just a convention in Python. You can use any name instead of self,
but it is strongly recommended to use self for better readability and understanding of the code.
"""
