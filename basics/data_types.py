#!/usr/bin/python

"""
    Python is a dynamically typed language. It means, the datatype of a variable is decided during run time by looking at the
    value assigned. For example, if you define x = 10, x is assigned integer datatype 'int'. If you define x = '10', the x is assigned string
    datatype 'str'.

    There are 7 datatypes in Python.
    int - Integers
    float - Floating point numbers
    str - Strings
    complex - Complex numbers
    list - Index based arrays
    tuple - Index based arrays
    dict - Dictionaries i.e. hash maps consisting a key and value
    set - Sets

    - int, float, str, tuple are immutable, meaning, they cannot be changed once they are defined.
    - list, tuple, dict, set are called collections.
    - list, dict, tuple are ordered arrays meaning they are indexed and can be accessed by index.
    - set are unordered.
"""

# Hint: To check the type of variable in Python, we can use the method 'type'

# Integers

number_1 = 10
number_2 = 20
print(type(number_1)) # Output: <class 'int'>


# Floating point numbers
fp_1 = 10.0
fp_2 = 12.11
print(type(fp_1)) # Output: <class 'float'>


# Adding a integer and floating point numbers will result in floating point number
print(number_1 + fp_1) # Output: 20.0


"""
    Tip: Type casting: It is the process of converting one datatype to another datatype. For example, coverting floating type
    into integer datatype. It is done in Python as below:
"""
result = number_1 + fp_1 # Output: 20.0
result = int(result)
print(result) # Output: 20
print(type(result)) # Output: <class 'int'>
 
 
"""
    Tip: Dividing two integers using normal division operator '/' will result in float type. If we want integer result, we 
    should perform floor division '//'
"""
print(10/2) # Output: 5.0
print(10//2) # Output: 5
