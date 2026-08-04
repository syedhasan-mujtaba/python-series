#DICTIONARY METHODS:

#1. items() - returns a list of tuples containing key-value pairs from the dictionary.
#SYNTAX: dict.items()
#EXAMPLE:
"""my_dict = {'a': 1, 'b': 2, 'c': 3}
items = my_dict.items() #OUTPUT: dict_items([('a', 1), ('b', 2), ('c', 3)]) """

#2. keys() - returns a list of all the keys in the dictionary.
#SYNTAX: dict.keys()
#EXAMPLE:
"""my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys() #OUTPUT: dict_keys(['a', 'b', 'c']) """

#3. values() - returns a list of all the values in the dictionary.
#SYNTAX: dict.values()
#EXAMPLE:
"""my_dict = {'a': 1, 'b': 2, 'c': 3}
values = my_dict.values() #OUTPUT: dict_values([1, 2, 3]) """

#4. update() - updates the dictionary with key-value pairs from another dictionary or iterable of key-value pairs.
#SYNTAX: dict.update(other_dict)
#EXAMPLE:
"""my_dict = {'a': 1, 'b': 2}
other_dict = {'c': 3, 'd': 4}
my_dict.update(other_dict) #OUTPUT: {'a': 1, 'b': 2, 'c': 3, 'd': 4} """

#5. get() - returns the value for a specified key if the key is in the dictionary, otherwise returns none or a default value.
#SYNTAX: dict.get(key, default=None)
#EXAMPLE:
"""my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.get('b') #OUTPUT: 2"""

#6. pop() - removes the specified key and returns the corresponding value. If the key is not found, it raises a KeyError.
#SYNTAX: dict.pop(key, default=None)
#EXAMPLE:
"""my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.pop('b') #OUTPUT: 2 + my_dict = {'a': 1, 'c': 3} """

#7. popitem() - removes and returns the last inserted key-value pair as a tuple. If the dictionary is empty, it raises a KeyError.
#SYNTAX: dict.popitem()
#EXAMPLE:
"""my_dict = {'a': 1, 'b': 2, 'c': 3}
item = my_dict.popitem() #OUTPUT: ('c', 3) + my_dict = {'a': 1, 'b': 2} """

#8. clear() - removes all items from the dictionary.
#SYNTAX: dict.clear()
#EXAMPLE:
"""my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.clear() #OUTPUT: {} """

#9 issubset() - checks if all keys of the dictionary are present in another dictionary.
#SYNTAX: dict1.issubset(dict2)
#EXAMPLE:
"""my_dict = {'a': 1, 'b': 2}
other_dict = {'a': 1, 'b': 2, 'c': 3}
is_subset = my_dict.issubset(other_dict) #OUTPUT: True """

#10. issuperset() - checks if all keys of another dictionary are present in the dictionary.
#SYNTAX: dict1.issuperset(dict2)
#EXAMPLE:
"""my_dict = {'a': 1, 'b': 2, 'c': 3}
other_dict = {'a': 1, 'b': 2}
is_superset = my_dict.issuperset(other_dict) #OUTPUT: True """