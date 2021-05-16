"""
    Lists are one type of collections or arrays that are mutable. That means, once defined, we can alter
    any element of a list which is opposite to tuples, where we will be not change any element of a tuple
    after it is defined.

    List are created using square brackets []. To create an empty list we can simply define it using empty
    square braces or using the keyword 'list'.
"""

x = []
# or
x = list()

# To create a list of numbers like 1,2,3 we can do it as follows:
x = [1,2,3]

# Lists can contain heterogenous elements i.e. elements in lists can be of different datatypes.
x = [1, 2.0, 'a', '#', [1,2,3], (1,2,3)]

# To access a element in a list, we can access it using index of the element
x[0] # Output: 1 since index of element 1 is 0
x[1] # Output: 2.0 since index of element 2.0 is 1

# To add lists we can do it by using '+'
x = [1, 2]
y = [4, 5]
print(x+y) # Output: [1, 2, 4, 5]

# To get length of a list i.e. the number of elements in a list, we should pass the list to len function
print(len(x)) # Output: 2

# List methods:

# append:
# To add an element to list we use append method on a list
x = [1,2]
x.append(3) # Now elements in x will be [1,2,3]

# extend:
# This is used to elements of another list to a list
x = [1,2]
y = [3,4]
x.extend(y) # Now elements in x will be [1,2,3,4]

"""
    Tip: What would happend if we give a list to append method?
    Ans: It will append the list directly. But if we give it to extend method, it will only add the elements
    to the list instead creating a nested list.
"""
x1 = [1, 2]
y1 = [3, 4]
x1.append(y1) # Now elements in x1 is [1, 2, [3, 4]]

x2 = [1, 2]
y2 = [3, 4]
x2.extend(y2) # Now elements in x2 is [1, 2, 3, 4]

# remove
# This is used to remove an element from the given list
x.remove(1) # This is will remove 1 from x. 

# pop
# This is used to remove an element by given index from a list
x.pop(1) # This is will remove 2 from x
# If no index is given, it will remove the last element from a list
# Also the removed element will be returned.
x = [1, 2]
y = x.pop()
# Now y will contain 2 and x will be [1]

# index
# This is used to return the index for a given value
x = ['a', 'b', 'c', 'd']
x.index('d') # This will give 3 as output since 3 is the index of element 'd'.

# count
# This will return the count of a given element is a list
x = ['a', 'a', 'd', 'b', 'a']
x.count('a') # This will return 3 since 'a' appeared 3 times in list x


# List slicing
# THis is same as string slicing. Slicing is tecnique used to make sub lists from a list
# syntax of slicing is <variable>[start:stop:step]
x = [1,2,3,4,5]
print(x[0:5]) # Output: [1, 2, 3, 4, 5]

# Default value of start is 0, stop is length of the list, step is 1
# Note: stop is exlusive that means the index will be upto stop but does not include stop
# for example is start is 2, stop is 10, then indexes will be 2,3,4,5,6,7,8,9 only. Since stop
# is exlusive it will not appear in the output.
print(x[2:4]) # Output: [3, 4]
