#BREAK STATEMENT IN FOR LOOP:
""" The break statement is used to exit a for loop prematurely, before it has finished iterating over the entire sequence.
When the break statement is encountered, the loop is immediately terminated, and the program continues with the next statement after the loop. """

#SYNTAX:
""" for item in sequence:
    # block of code to be executed
    if condition:
        break  # exit the loop if the condition is met """

#EXAMPLE:
for i in range (100):
    if (i==20):
        break #exit the loop right now when i equals 20
    print(i) #this will print numbers from 0 to 19 and then exit the loop when i equals 20

#CONTINUE STATEMENT IN FOR LOOP:
""" The continue statement is used to skip the current iteration of a for loop and move on to the next iteration.
When the continue statement is encountered, the remaining code in the loop for that iteration is skipped,
and the loop proceeds to the next item in the sequence. """

#SYNTAX:
""" for item in sequence:
    # block of code to be executed
    if condition:
        continue  # skip the rest of the loop for this iteration and move to the next item """

#EXAMPLE:
for i in range (100):
    if (i==20):
        continue #skip this iteration when i equals 20 and move to the next iteration
    print(i) #this will print numbers from 0 to 19 except 20, as it is skipped

#PASS STATEMENT IN FOR LOOP:
""" The pass statement is a placeholder that does nothing when executed.
It is often used in for loops as a placeholder for code that will be added later or to create an empty loop body. 
When the pass statement is encountered, the loop continues to the next iteration without performing any action. """

#SYNTAX:
""" for item in sequence:
    # block of code to be executed
    if condition:
        pass  # do nothing and continue to the next iteration """

#EXAMPLE:
for i in range (100):
    if (i==20):
        pass #do nothing when i equals 20 and continue to the next iteration
    print(i) #this will print numbers from 0 to 99, including 20, as it is not skipped or exited
    