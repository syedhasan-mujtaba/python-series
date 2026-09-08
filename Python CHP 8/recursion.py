#WHAT IS RECURSION? (IMPORTANT CONCEPT IN PROGRAMMING)
"""
Recursion is a programming technique where a function calls itself in its own definition.
It is used to directly use a mathematical formula as a funtion in programming.
Recursion is a powerful tool that allows for elegant solutions to complex problems, but it requires careful handling to avoid infinite loops and stack overflow errors.
It is used to solve problems that can be broken down into smaller, similar subproblems.
"""
#EXPLANATION OF RECURSION:
"""
In recursion, a function calls itself with modified parameters until it reaches a base condition that stops the recursion.
The base condition is a specific case where the function does not call itself again, preventing infinite loops and 
allowing the function to return a value. Recursion is often used in problems that can be defined in terms of smaller instances
of the same problem, such as calculating factorials, Fibonacci numbers, and traversing data structures like trees and graphs. """

##SYNTAX OF RECURSION:
"""
def function_name(parameters):
    if base_condition:
        return value
    else:
        return function_name(modified_parameters)
"""

#EXAMPLE OF RECURSION:
def factorial(n):
    if (n == 0 or n == 1):  # Base condition
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call with modified parameter

    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"The factorial of {n} is: {factorial(n)}")  # Output: Factorial of n

#CONCEPT OF FACTORIAL:
"""
The factorial of a non-negative integer n is the product of all positive integers less than or equal to n. It is denoted by n!.
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 * factorial(1) = 2 * 1 = 2
factorial(3) = 3 * factorial(2) = 3 * 2 * 1 = 6
factorial(n) = n * n-1 * n-2 * ... * 3 * 2 * 1
factorial(n) = n * factorial(n-1)  # Recursive definition of factorial
"""

#WHAT IS THE BASE CONDITION IN RECURSION?
"""
The base condition in recursion is a specific case that stops the recursive calls and allows the function to return a value.
It is essential to prevent infinite loops and stack overflow errors.
The base condition is typically a simple case that can be solved directly without further recursion.
For example, in the factorial function, the base condition is when n is 0 or 1, where the function returns 1 without making any further recursive calls."""

#WARNING ABOUT RECURSION:
"""
The programmer needs to be extremely careful while working with recursion to ensure that the function 
doesnot infinitely keep calling itself. Recursion is sometimes the most direct way to code an algorithms.
"""
#MOST IMPORTANT POINTS ABOUT RECURSION:
"""
1. A recursive function must have a base case to terminate the recursion.
2. Each recursive call should move towards the base case.
3. The function should call itself with modified arguments.
4. Recursion can make code more readable and easier to understand for certain problems.
5. However, excessive recursion can lead to stack overflow errors and performance issues.
"""

#MOST COMMON USE CASES OF RECURSION:
"""
1. Calculating Factorials: As shown in the example above, recursion can be used to calculate the factorial of a number.
2. Computing Fibonacci Numbers: Recursion can be used to compute Fibonacci numbers, where each number is the sum of the two preceding ones.
3. Traversing Trees and Graphs: Recursion is often used to traverse tree and graph data structures, visiting each node and its children.
"""
#MOST COMMON USE CASES OF RECURSION (CONTINUED):
"""4. Solving Puzzles and Games: Recursion can be used to solve puzzles and games, such as the Tower of Hanoi or maze-solving algorithms.
5. Backtracking Algorithms: Recursion is used in backtracking algorithms to explore all possible solutions to a problem, such as in solving Sudoku or generating permutations and combinations.
6. Divide and Conquer Algorithms: Recursion is used in divide and conquer algorithms, where a problem is divided into smaller subproblems, solved recursively, and then combined to form the final solution. Examples include merge sort and quicksort.
7. Dynamic Programming: Recursion is often used in dynamic programming to solve problems by breaking them down into overlapping subproblems and storing the results of these subproblems to avoid redundant calculations. Examples include the knapsack problem and longest common subsequence.
8. Recursive Descent Parsing: Recursion is used in parsing techniques, such as recursive descent parsing, to analyze the structure of programming languages and generate parse trees.
9. Generating Combinations and Permutations: Recursion can be used to generate all possible combinations and permutations of a set of elements, which is useful in combinatorial problems.
10. Implementing Mathematical Functions: Recursion can be used to implement mathematical functions, such as exponentiation, greatest common divisor (GCD), and least common multiple (LCM), by breaking them down into simpler cases.
"""