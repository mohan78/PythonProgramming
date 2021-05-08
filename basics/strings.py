#!/usr/bin/python

"""
    String in python are represented by the keyword 'str'. Strings in python can be treated as an array of characters.
    Strings are immutable in Python i.e. a string cannot be changed once it is defined. Both single quotes and double
    quotes can be used to define strings.
"""

word_1 = 'apple'
word_2 = "apple"


# A character in a string can be accessed using index.
print(word_1[0]) # Output: a
print(word_1[3]) # Output: l

# Adding strings:
# 1. Simply add
print(word_1+word_2) # Output: appleapple
# 2. Using .join string method
print(word_1.join(word_2)) # Output: appleapple


"""
    String splicing: Splicing is technique where you can extract sub-string from a string using indexes.
    syntax: str[start: stop: step]
    start is the starting index. Default value of start is 0
    stop is the index upto which the string should be extracted. Default value of stop is one value less of length of string
    step is the number of steps the index should be increased to get the next index. Default value of step is 1 

    Note: space is also treated as a character
"""

word = "My name is itachi uchiha"
print(word[1: 7]) # Output:  y name
print(word[:5]) # Output: My na

# If we increase step as 2, then every time, the index is increased by 2. i.e. for example if we take starting index as 0, stop as 5
# step as 2, then the first index of the substring is 0 then 2 is added to start and the next index will be 2, then again 2 is added
# so the next index will be 4 and then 2 is added again to it which means the next index is 6. Since the the stop index is 5 which is
# less than 6 hence it will not be printed
print(word[:8:2]) # Output: M ae 

# Inorder to reverse the direction of string, just give step as -1.
print(word[::-1]) # Output: ahihcu ihcati si eman yM
# The above output is nothing but reversed form og the given string which can be used to compute palindrome


"""
    String methods: The following are some of the import string methods
"""
# len(string): prints the length of the given string
print(len(word)) # Output: 24

# replace(character_that_needs_to_be_replaced, character)
print(word.replace('a', 'p')) # Output: My npme is itpchi uchihp

# count(character): prints the number of times the given character appeared in a string
print(word.count('a')) # Output: 3

# split(character): Splits the string at the given character
print(word.split(' ')) # Output: ['My', 'name', 'is', 'itachi', 'uchiha']

# More info on string methods can be found at : https://www.programiz.com/python-programming/methods/string
