#IMPORTANT NOTE:
"""LISTS ARE MUTABLE, MEANING THEIR CONTENTS CAN BE CHANGED AFTER CREATION.
 THE METHODS MENTIONED BELOW MODIFY THE ORIGINAL LIST IN PLACE (UNLIKE STRINGS, WHICH ARE IMMUTABLE).
 """

# LIST METHODS:
"""
PYTHON LISTS COME WITH BUILT-IN METHODS TO PERFORM VARIOUS OPERATIONS ON THEM.
SOME COMMONLY USED METHODS ARE:
1.sort(): SORTS THE ELEMENTS OF THE LIST IN ASCENDING ORDER (DEFAULT) OR DESCENDING ORDER (IF SPECIFIED).
EXAMPLE: numbers=[3, 1, 4, 2]
numbers.sort() #OUTPUT: [1, 2, 3, 4]
numbers.sort(reverse=True) #OUTPUT: [4, 3, 2, 1]

2. reverse(): REVERSES THE ORDER OF THE ELEMENTS IN THE LIST.
EXAMPLE: numbers=[1, 2, 3, 4]
numbers.reverse() #OUTPUT: [4, 3, 2, 1]

3. append(): ADDS AN ELEMENT TO THE END OF THE LIST.
EXAMPLE: fruits=["apple", "banana"]
fruits.append("cherry") #OUTPUT: ['apple', 'banana', 'cherry']

4. extend(): ADDS MULTIPLE ELEMENTS TO THE END OF THE LIST.
EXAMPLE: fruits=["apple", "banana"]
fruits.extend(["cherry", "date"]) #OUTPUT: ['apple', 'banana', 'cherry', 'date']

5. insert(): INSERTS AN ELEMENT AT A SPECIFIED INDEX.
EXAMPLE: fruits=["apple", "banana"]
fruits.insert(1, "cherry") #OUTPUT: ['apple', 'cherry', 'banana']

6. remove(): REMOVES THE FIRST OCCURRENCE OF A SPECIFIED ELEMENT FROM THE LIST.
EXAMPLE: fruits=["apple", "banana", "cherry"]
fruits.remove("banana") #OUTPUT: ['apple', 'cherry']

7. pop(): REMOVES AND RETURNS THE ELEMENT AT A SPECIFIED INDEX (DEFAULT IS THE LAST ELEMENT).
EXAMPLE: fruits=["apple", "banana", "cherry"]
fruits.pop() #OUTPUT: 'cherry', fruits becomes ['apple', 'banana']

8. index(): RETURNS THE INDEX OF THE FIRST OCCURRENCE OF A SPECIFIED ELEMENT IN THE LIST.
EXAMPLE: fruits=["apple", "banana", "cherry", "banana"]
fruits.index("banana") #OUTPUT: 1

9. count(): RETURNS THE NUMBER OF OCCURRENCES OF A SPECIFIED ELEMENT IN THE LIST.
EXAMPLE: fruits=["apple", "banana", "cherry", "banana"]
fruits.count("banana") #OUTPUT: 2

10. clear(): REMOVES ALL ELEMENTS FROM THE LIST.
EXAMPLE: fruits=["apple", "banana", "cherry"]
fruits.clear() #OUTPUT: [], fruits becomes an empty list
"""