(1)Variables: Python Variable is containers that store values. Python is not “statically typed”. We do not need to declare variables before using them or declare their type.
A variable is created the moment we first assign a value to it. A Python variable is a name given to a memory location.
It is the basic unit of storage in a program.
Rules for Python variables
 1.A Python variable name must start with a letter or the underscore character.
 2.A Python variable name cannot start with a number.
 3.A Python variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
 4.Variable in Python names are case-sensitive (name, Name, and NAME are three different variables).
 5.The reserved words(keywords) in Python cannot be used to name the variable in Python.
(2)Numbers:There are three numeric types in Python:

   int
   float
  complex
Variables of numeric types are created when you assign a value to them:
 x = 1    # int
 y = 2.8  # float
 z = 1j   # complex
 Note: You cannot convert complex numbers into another number type.
 (3)Strings:A String is a data structure in Python Programming that represents a sequence of characters.
 It is an immutable data type, meaning that once you have created a string, you cannot change it.
 Python String are used widely in many different applications, such as storing and manipulating text data, representing names, addresses, and other types of data that can be represented as text.
 Python Programming does not have a character data type, a single character is simply a string with a length of 1.
 (4)List:
 Lists are used to store multiple items in a single variable.
 Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
 Lists are created using square brackets.
 List items are ordered, changeable, and allow duplicate values.
 List items are indexed, the first item has index [0], the second item has index [1] etc.
 (4)IF statement:The if statement is the most simple decision-making statement. It is used to decide whether a certain statement or block of statements will be executed or not.
 (5)For loop:A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
   This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
   With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
 (6)Functions:
      A function is a block of code which only runs when it is called.
     You can pass data, known as parameters, into a function.A function can return data as a result.
     In Python a function is defined using the def keyword.
(7)Dictionary:
     Dictionaries are used to store data values in key:value pairs.
    A dictionary is a collection which is ordered, changeable and do not allow duplicates.
    Dictionaries are written with curly brackets.
(8)Tuple:
    Tuples are used to store multiple items in a single variable.
    Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
    A tuple is a collection which is ordered and unchangeable.
    Tuples are written with round brackets.
(9)Read Write:
     Python offers various methods to read and write to files where each functions behaves differently.
     One important thing to note is the file operations mode. To read a file, you need to open the file in the read or write mode.
     While to write to a file in Python, you need the file to be open in write mode.

    Here are some of the functions in Python that allow you to read and write to files:

   read() : This function reads the entire file and returns a string
   readline() : This function reads lines from that file and returns as a string. It fetch the line n, if it is been called nth time.
   readlines() : This function returns a list where each element is single line of that file.
   readlines() : This function returns a list where each element is single line of that file.
   write() : This function writes a fixed sequence of characters to a file.
   writelines() : This function writes a list of string.
   append() : This function append string to the file instead of overwriting the file.
