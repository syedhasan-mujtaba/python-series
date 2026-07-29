#TUPLE METHODS:
"""
TUPLES HAVE ONLY TWO BUILT-IN METHODS:
1. count(): RETURNS THE NUMBER OF OCCURRENCES OF A SPECIFIED ELEMENT IN THE TUPLE.
SYNTAX: tuple_name.count(element)
EXAMPLE: a=(1, 2, 3, 2, 4)
print(a.count(2)) #OUTPUT: 2

2. index(): RETURNS THE INDEX OF THE FIRST OCCURRENCE OF A SPECIFIED ELEMENT IN THE TUPLE.
SYNTAX: tuple_name.index(element)
EXAMPLE: a=(1, 2, 3, 2, 4)
print(a.index(2)) #OUTPUT: 1
"""

"""
(TUPLES DO NOT HAVE METHODS LIKE append(), extend(), insert(), remove(), pop(), clear(), sort(),
 or reverse() BECAUSE THEY ARE IMMUTABLE.)
"""

#SOME OTHER USEFUL TUPLE OPERATIONS:
"""
1. Concatenation: Tuples can be concatenated using the + operator.
SYNTAX: tuple1 + tuple2
    EXAMPLE: a=(1, 2, 3)
            b=(4, 5, 6)
            c=a+b #OUTPUT: (1, 2, 3, 4, 5, 6)

2. Repetition: Tuples can be repeated using the * operator.
SYNTAX: tuple * n (where n is the number of times to repeat the tuple)
   EXAMPLE: a=(1, 2)
            b=a*3 #OUTPUT: (1, 2, 1, 2, 1, 2)

3. Membership Testing: The in and not in operators can be used to check if an element is present in a tuple.
SYNTAX: element in tuple, element not in tuple
   EXAMPLE: a=(1, 2, 3)
            print(2 in a) #OUTPUT: True
            print(4 in a) #OUTPUT: False

4.Length: The len() function can be used to get the number of elements in a tuple.
SYNTAX: len(tuple)
   EXAMPLE: a=(1, 2, 3)
            print(len(a)) #OUTPUT: 3

5.Minimum and Maximum: The min() and max() functions can be used to get the smallest and largest elements in a tuple.
SYNTAX: min(tuple), max(tuple)
   EXAMPLE: a=(1, 2, 3)
               print(min(a)) #OUTPUT: 1
                print(max(a)) #OUTPUT: 3

6. Conversion: Tuples can be converted to lists and vice versa using the list() and tuple() functions.
SYNTAX: list(tuple), tuple(list)
   EXAMPLE: a=(1, 2, 3)
               b=list(a) #OUTPUT: [1, 2, 3]
                c=tuple(b) #OUTPUT: (1, 2, 3)

7. Unpacking: Tuples can be unpacked into individual variables.
SYNTAX: var1, var2, var3=tuple   
   EXAMPLE: a=(1, 2, 3)
               x, y, z=a
                    print(x) #OUTPUT: 1
                    print(y) #OUTPUT: 2
                    print(z) #OUTPUT: 3                                            
"""