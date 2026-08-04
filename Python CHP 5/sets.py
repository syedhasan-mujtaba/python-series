#SETS IN PYTHON:
"""A set is a built-in Python data structure used to store a collection of unique elements. """
#NOTE: A mutable, unordered collection of unique elements.

#SYNTAX:
"""
set_name = {element1, element2, element3}
"""
#EXAMPLE:
"""
my_set = {1, 2, 3, 4, 5}
"""


#EMPTY SET:
"""SYNTAX: set_name = set() #NOT USE {} AS IT WILL CREATE AN EMPTY DICTIONARY INSTEAD OF A SET
"""

#NEED OF SETS:
#1. To store unique elements.
#2. To perform mathematical operations like union, intersection, difference, etc.
#3. To eliminate duplicate values from a list or other iterable.
#4. sets can contain elements of different data types (like integers, strings, tuples, etc.) but cannot contain mutable elements like lists or dictionaries.

#PROPERTIES OF SETS:
#1. Unordered: The elements in a set are not indexed, so they do not have a defined order.
#2. Unindexed: Since sets are unordered, they do not support indexing, slicing, or other sequence-like behavior.
#3. Unchangeable: While the elements of a set must be immutable (like numbers, strings, or tuples), the set itself is mutable, meaning you can add or remove elements after its creation.
#4. Unique Elements: Sets automatically eliminate duplicate values, ensuring that each element is unique within the set.
