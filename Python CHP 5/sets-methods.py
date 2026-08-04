#SETS METHODS or OPERATIONS:

#1. add() - adds an element to the set.
#SYNTAX: set.add(element)
#EXAMPLE:
""" my_set = {1, 2, 3}
my_set.add(4) #OUTPUT: {1, 2, 3, 4} """

#2. remove() - removes a specified element from the set. If the element is not found, it raises a KeyError.
#SYNTAX: set.remove(element)
#EXAMPLE:
""" my_set = {1, 2, 3}
my_set.remove(2) #OUTPUT: {1, 3} """

#3. len() - returns the number of elements in the set.
#SYNTAX: len(set)
#EXAMPLE:
""" my_set = {1, 2, 3}
print(len(my_set)) #OUTPUT: 3 """

#4. pop() - removes and returns an arbitrary (unpredictable/random) element from the set. If the set is empty, it raises a KeyError.
#SYNTAX: set.pop()
#EXAMPLE:
""" my_set = {1, 2, 3}
element = my_set.pop() #OUTPUT: an arbitrary element from the set + my_set = {1, 3} """

#5. clear() - removes all elements from the set.
#SYNTAX: set.clear()
#EXAMPLE:
""" my_set = {1, 2, 3}
my_set.clear() #OUTPUT: set() """