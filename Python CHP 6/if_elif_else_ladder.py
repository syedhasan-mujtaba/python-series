#ELIF CLAUSE:
""" Elif in Python is short for "else if". It allows you to check multiple conditions
in a sequential manner. If the first condition is not true, it checks the next condition, 
and so on, until it finds a true condition or reaches the else clause."""

#IF-ELIF-ELSE LADDER:
""" An if-elif-else ladder is a way to check multiple conditions in a sequential manner. It allows
you to test several conditions and execute different blocks of code based on which condition is true."""

#SYNTAX OF IF-ELIF-ELSE LADDER:
if condition1:
    # code to execute if condition1 is True
    pass
elif condition2:
    # code to execute if condition2 is True
    pass
else:
    # code to execute if none of the above conditions are True
    pass

#EXAMPLE OF IF-ELIF-ELSE LADDER:
if (a>=18):
    print("You are eligible to vote.")
elif (a<0):
    print("Invalid negative age.")
elif (a==0):
    print("You are not born yet.")
else:
    print("You are not eligible to vote.")

#IMPORTANT NOTE:
#1. There can be any number of elif clauses in an if-elif-else ladder.
#2. Last else is executed only if all the above conditions are false.