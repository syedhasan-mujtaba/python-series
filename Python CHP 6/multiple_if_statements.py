#MULTIPLE IF STATEMENTS:
""" In Python, you can use multiple if statements to check several conditions independently.
Each if statement is evaluated separately, and all conditions that are true will have their 
corresponding blocks of code executed."""

 #SYNTAX OF MULTIPLE IF STATEMENTS:
if condition1:
    # code to execute if condition1 is True
    pass
if condition2:
    # code to execute if condition2 is True
    pass

#EXAMPLE OF MULTIPLE IF STATEMENTS:

   #if statement to check if a number is even
if (a%2==0):
    print("The number is even.")
   #if statement to check if a number is positive 
if (a>=18):
    print("You are eligible to vote.")
elif (a<0):
    print("Invalid negative age.")
elif (a==0):
    print("You are not born yet.")
else:
    print("You are not eligible to vote.")

#IMPORTANT NOTE:
#1. Each if statement is evaluated independently, so multiple blocks of code can be executed if multiple conditions are true.
#2. If you want to check multiple conditions and execute only one block of code, you should use an if-elif-else ladder instead of multiple if statements.
#3. Be careful with the indentation. If the indentation is not consistent, it will result in an IndentationError.
