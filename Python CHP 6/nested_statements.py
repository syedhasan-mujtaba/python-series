#NESTED IF STATEMENTS:
""" In Python, you can have if statements inside other if statements.
 This is called nested if statements. """

#SYNTAX OF NESTED IF STATEMENTS:
if condition1:
    # code to execute if condition1 is True
    if condition2:
        # code to execute if both condition1 and condition2 are True
        pass

#EXAMPLE OF NESTED IF STATEMENTS:
a = 10
if a > 0:
    print("The number is positive.")
    if a % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is not positive.")

#DIFFERENCE BETWEEN NESTED IF STATEMENTS AND MULTIPLE IF STATEMENTS:
""" Nested if statements are used when you want to check a condition only if the previous condition is true.
    Multiple if statements are used when you want to check multiple conditions independently, regardless of the previous conditions. """

#IMPORTANT NOTE:
#1. You can have multiple levels of nested if statements, but it is generally recommended to keep the nesting to a reasonable level for better readability and maintainability of the code.
#2. Be careful with the indentation. If the indentation is not consistent, it will result in an IndentationError.
#3. Nested if statements can be combined with elif and else clauses to create more complex decision-making structures.