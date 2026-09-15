# FUNCTIONS IN FILE IN PYTHON:

#FOR OPENING A FILE:
"""
open(): This function is used to open a file in Python.
It takes two arguments: the name of the file and the mode in which the file should be opened (e.g., read, write, append).
#SYNTAX: open("filename" , "mode of opening(read mode by default)")
#EXAMPLE: file = open("example.txt", "r")  # Opens the file in read mode
"""


# MODES OF OPENING A FILE:
""" 
'r': Read mode (default)
'w': Write mode 
'a': Append mode 
'+': Update mode (read and write)
'rb': Read binary mode
'rt': Read text mode (default)
'wb': Write binary mode 
'wt': Write text mode (default)
"""
#1. FOR READING FROM A FILE:
"""
read(): This function is used to read the contents of a file in Python.
It can be called on a file object to read the entire contents of the file or a specified number of bytes.
#SYNTAX: file.read(size or entire file)  # Reads 'size' bytes from the file
#EXAMPLE: f = open("example.txt", "r")
         content = f.read()  # Reads the entire file
         print(content)  # Prints the content of the file
         f.close()  # Closes the file
#OUTPUT: This is an example of reading from a file.
"""
# =>READLINE:
"""
readline(): This function is used to read a single line from a file in Python.
It can be called on a file object to read the next line from the file.
#SYNTAX: file.readline()  # Reads the next line from the file
#EXAMPLE: f = open("example.txt", "r")
         line2 = f.readline()  # Reads the second line from the file
         print(line2)  # Prints the line2
         f.close()  # Closes the file
#OUTPUT: This is the second line of the file.
"""
# =>READLINES:
"""
readlines(): This function is used to read all lines from a file in Python.
It can be called on a file object to read all lines from the file and return them as a list.
#SYNTAX: file.readlines()  # Reads all lines from the file
#EXAMPLE: f = open("example.txt", "r")
         lines = f.readlines()  # Reads all lines from the file
         print(lines)  # Prints the list of lines
         f.close()  # Closes the file
#OUTPUT: ['This is the first line of the file.\n', 'This is the second line of the file.\n']
"""
#2. FOR WRITING TO A FILE:
"""
write(): This function is used to write data to a file in Python.
It takes one argument: the data to be written.
#SYNTAX: file.write("data to be written")
#EXAMPLE: string = "Hello, World!"
            f = open("example.txt", "w")
            f.write(string)  # Writes the string to the file
            f.close()  # Closes the file
#OUTPUT: The file "example.txt" will contain the text "Hello, World!" after executing the above code.
"""
#3. FOR APPENDING TO A FILE:
"""
append(): This function is used to append data to a file in Python.
It takes one argument: the data to be appended.
#SYNTAX: file.append("data to be appended")
#EXAMPLE: string = "This is a new line."
            f = open("example.txt", "a")
            f.append(string)  # Appends the string to the file
            f.close()  # Closes the file
#OUTPUT: The file "example.txt" will have the new line appended to it after executing the above code.
"""
#4. FOR CLOSING A FILE:
"""
close(): This function is used to close a file in Python.
It takes no arguments and is called on a file object to close the file.
#SYNTAX: file.close()
#EXAMPLE: f = open("example.txt", "r")
         f.close()  # Closes the file
#OUTPUT: The file "example.txt" will be closed after executing the above code.
"""