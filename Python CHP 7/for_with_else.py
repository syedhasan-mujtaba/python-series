#FOR LOOP WITH ELSE:
""" In Python, a for loop can have an optional else clause that is executed after the loop finishes iterating over the sequence.
The else clause is executed only if the loop completes without encountering a break statement. """

#SYNTAX:
""" for item in sequence:
    # block of code to be executed
else:
    # block of code to be executed if the loop completes without a break statement """

#EXAMPLE:
l=[1, 2, 3, 4, 5]
for item in l:
    print(item)
else:
    print("Done") #this is printed when the loop exhausts!