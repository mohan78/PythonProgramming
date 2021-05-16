"""
    Tuples are a immutable collection or arrays in python i.e. once defined the elements of
    a tuple cannot be changed or updated.
    
    A tuple can be created using round brackets () or using keyword 'tuple'
"""

x = ()
# or
x = tuple

# When there is a only single element in a tuple, we need to put comma after it for it to become
# a tuple
x = (2,)
print(type(x))
x = (2) # This will be an integer
print(type(x))

# Tuple methods

# count
# This will return the number of occurrences of a given element in a tupel
x = (1,2,3,4,2,3,2)
print(x.count(2)) # Output: 3
print(x.count(3)) # Output: 2

# index
# This will return the index of given element
x = (1,2,3,4)
print(x.index(2)) # Output: 1
print(x.index(1)) # Output: 0
