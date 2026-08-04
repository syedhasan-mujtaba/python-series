#SOME MATHEMATICAL OPERATIONS ON SETS:

#1. Union - Combines all elements from both sets, removing duplicates.
#SYNTAX: set1 | set2 or set1.union(set2)
#EXAMPLE:
""" set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2 #OUTPUT: {1, 2, 3, 4, 5} """

#2. Intersection - Returns only the elements that are common to both sets.
#SYNTAX: set1 & set2 or set1.intersection(set2)
#EXAMPLE:
""" set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1 & set2 #OUTPUT: {3} """

#3. Difference - Returns the elements that are in the first set but not in the second set.
#SYNTAX: set1 - set2 or set1.difference(set2)
#EXAMPLE:
""" set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1 - set2 #OUTPUT: {1, 2} """

#4. Symmetric Difference - Returns the elements that are in either of the sets but not in both.
#SYNTAX: set1 ^ set2 or set1.symmetric_difference(set2)
#EXAMPLE:
""" set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_diff_set = set1 ^ set2 #OUTPUT: {1, 2, 4, 5} """
