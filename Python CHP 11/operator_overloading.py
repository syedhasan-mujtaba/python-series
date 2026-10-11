#WHAT IS OPERATOR OVERLOADING? (IN PYTHON)
"""
Operator overloading in Python allows you to define the behavior of standard operators (like +, -, *, etc.) for your own custom classes.
""" 
#SYNTAX OF OPERATOR OVERLOADING:
"""
class MyClass:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        # Define behavior for the + operator
        return MyClass(self.value + other.value)

    def __str__(self):
        return str(self.value)
"""
#EXAMPLE OF OPERATOR OVERLOADING:
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):                         #ADD VALUE OF TWO OBJECTS (RETURN VALUE OF OBJECT)
        return Number(self.value + other.value)

    def __sub__(self, other):                         #SUBTRACT VALUE OF TWO OBJECTS (RETURN VALUE OF OBJECT)
        return Number(self.value - other.value)

    def __mul__(self, other):                         #MULTIPLY VALUE OF TWO OBJECTS (RETURN VALUE OF OBJECT)
        return Number(self.value * other.value)

    def __truediv__(self, other):                     #DIVIDE VALUE OF TWO OBJECTS (RETURN FLOAT VALUE)
        return Number(self.value / other.value)

    def __floordiv__(self, other):                    #FLOOR DIVIDE VALUE OF TWO OBJECTS (RETURN INTEGER VALUE)
        return Number(self.value // other.value)

    def __str__(self):                                #RETURN STRING REPRESENTATION OF OBJECT (RETURN VALUE OF OBJECT)
        return str(self.value)

    def __len__(self):                                #RETURN LENGTH OF STRING REPRESENTATION OF OBJECT (RETURN NUMBER OF DIGITS IN VALUE)
        return len(str(self.value))
    
n = Number(1)
m = Number(2)

print(n + m)  # Output: 3
print(n - m)  # Output: -1
print(n * m)  # Output: 2
print(n / m)  # Output: 0.5
print(n // m)  # Output: 0
print(str(n))  # Output: 1
print(len(n))  # Output: 1

#IMPORTANT NOTE:
"""
Operator overloading allows you to customize the behavior of operators for your own classes,
making them work with instances of those classes in a way that's intuitive and consistent with the class's purpose.
"""