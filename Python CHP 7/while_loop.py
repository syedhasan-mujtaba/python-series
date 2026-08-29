#WHILE LOOP IN PYTHON:
""" A while loop is used to execute a block of code repeatedly as long as a certain condition is true. """
#SYNTAX:
""" while (condition):
    # block of code to be executed
    # update the condition (if necessary) """

#NOTE: 
""" The condition is checked first. If it evaluates to True,the body of the loop is executed otherwise not.
If the loop is entered, the process (condition check, execution of the body, and updating the condition) is repeated until it becomes False. """

#EXAMPLE:
i = 1
while (i < 6):
    print(i)
    i += 1 OR i = i + 1

#OUTPUT:
"""
1
2
3
4
5
"""