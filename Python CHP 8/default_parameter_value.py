#DEFAULT PARAMETER VALUE:
"""
Default parameter values are specified in the function definition.
If an argument is not provided when the function is called, the default value is used.
"""
#SYNTAX:
"""
def function_name(parameter1=default_value1, parameter2=default_value2):
    # Function body
    pass
"""
#EXAMPLE OF DEFAULT PARAMETER VALUE:
def goodday(name, ending="!"):
    print("Good day, " + name + ending)

goodday("Alice")  # Output: Good day, Alice!   #here the default value of 'ending' is used since it was not provided in the function call.
goodday("Bob", "?")  # Output: Good day, Bob?  #here the provided value of 'ending' is used instead of the default value.

#NOTE: Default parameter values must be specified after non-default parameters in the function definition.

#EXAMPLE OF DEFAULT PARAMETER VALUE WITH RETURN STATEMENT:
def goodday(name, ending="!"):
    return "Good day, " + name + ending
result1 = goodday("Alice")  # Output: Good day, Alice!
result2 = goodday("Bob", "?")  # Output: Good day, Bob?

#NOTE: The return statement stores the result of the function in a variable (in this case, 'result1' and 'result2') which can be used later in the program.