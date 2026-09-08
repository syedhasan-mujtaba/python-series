#FUNCTIONS WITH ARGUMENTS:
"""
Functions with arguments are those that take input values (arguments) when they are called.
These arguments can be used within the function to perform specific tasks.
"""
#SYNTAX OF FUNCTION WITH ARGUMENTS:
"""
def function_name(argument1, argument2):
    # Function body
    pass
"""
#EXAMPLE OF FUNCTION WITH ARGUMENTS:
def goodday(name, ending):
    print("Good day, " + name + ending)

    goodday("Alice", "!")  # Output: Good day, Alice!

#RETURN STATEMENT IN FUNCTION WITH ARGUMENTS:
"""
Return statement is used to send a value back from the function to the caller.
It can be used in functions with arguments to return a result based on the input values.
"""
#SYNTAX OF RETURN STATEMENT IN FUNCTION WITH ARGUMENTS:
"""
def function_name(argument1, argument2):
    # Function body
    return value
"""
#EXAMPLE OF RETURN STATEMENT IN FUNCTION WITH ARGUMENTS:
def goodday(name, ending):
    return "Good day, " + name + ending


result = goodday("Alice", "!")
print(result)  # Output: Good day, Alice!

#NOTE: The return statement stores the result of the function in a variable (in this case, 'result') which can be used later in the program.
