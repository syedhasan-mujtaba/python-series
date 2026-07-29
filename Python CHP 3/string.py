#STRING FUNCTIONS:
"""
STRING FUNCTIONS ARE BUILT-IN METHODS THAT CAN BE USED TO MANIPULATE STRINGS.
"""
#NOTE:
"""
 STRING FUNCTION IS IMMUTABLE, MEANING THAT IT DOES NOT MODIFY THE ORIGINAL STRING
 BUT RETURNS A NEW STRING WITH THE MODIFICATIONS.
"""


#SOME COMMON STRING FUNCTIONS ARE:
#1. len(): RETURNS THE LENGTH OF THE STRING (INCLUDING SPACES).
#SYNTAX: len(string)
#EXAMPLE:
s="hello world"
len(s) #OUTPUT: 11

#2. endswith(): RETURNS TRUE IF THE STRING ENDS WITH THE SPECIFIED SUFFIX (CASE-SENSITIVE).
#SYNTAX: string.endswith(suffix)
#EXAMPLE:
s="hello world"
print(s.endswith("world")) #OUTPUT: True

#3. startswith(): RETURNS TRUE IF THE STRING STARTS WITH THE SPECIFIED PREFIX (CASE-SENSITIVE).
#SYNTAX: string.startswith(prefix)
#EXAMPLE:
s="hello world"
print(s.startswith("hello")) #OUTPUT: True

#4. capitalize(): RETURNS A COPY OF THE STRING WITH THE FIRST CHARACTER CAPITALIZED AND THE REST LOWERCASE.
#SYNTAX: string.capitalize()
#EXAMPLE:
s="hello world"
print(s.capitalize()) #OUTPUT: Hello world

#5. str(): RETURNS A STRING VERSION OF THE OBJECT.
#SYNTAX: str(object)
#EXAMPLE:
s=123
print(str(s)) #OUTPUT: "123"

#6. upper(): RETURNS A COPY OF THE STRING WITH ALL CHARACTERS CONVERTED TO UPPERCASE.
#SYNTAX: string.upper()
#EXAMPLE:
s="hello world"
print(s.upper()) #OUTPUT: HELLO WORLD


#7. lower(): RETURNS A COPY OF THE STRING WITH ALL CHARACTERS CONVERTED TO LOWERCASE.
#SYNTAX: string.lower()
#EXAMPLE:
s="HELLO WORLD"
print(s.lower()) #OUTPUT: hello world

#8. title(): RETURNS A COPY OF THE STRING WITH THE FIRST CHARACTER OF EACH WORD CAPITALIZED.
#SYNTAX: string.title()
#EXAMPLE:
s="hello world"
print(s.title()) #OUTPUT: Hello World

#9. count(): RETURNS THE NUMBER OF OCCURRENCES OF A SPECIFIED WORD IN THE STRING.
#SYNTAX: string.count(word)
#EXAMPLE:
s="hello world, hello Python"
print(s.count("hello")) #OUTPUT: 2

#10. find(): RETURNS THE INDEX OF THE FIRST OCCURRENCE OF A SPECIFIED WORD IN THE STRING. RETURNS -1 IF NOT FOUND.
#SYNTAX: string.find(word)
#EXAMPLE:
s="hello world"
print(s.find("world")) #OUTPUT: 6

#11. replace(): RETURNS A COPY OF THE STRING WITH ALL OCCURRENCES OF A SPECIFIED WORD REPLACED WITH ANOTHER WORD.
#SYNTAX: string.replace(old_word, new_word)
#EXAMPLE:
s="hello world world"
print(s.replace("world", "Python")) #OUTPUT: hello Python Python
