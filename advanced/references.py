"""
    You have keep in mind that everything in Python is an object. And an variable is nothing but
    an reference to that object.

    for example, if you declare x = 10, the an integer object 10 is created and its address is stored
    in x. Now if you do y = 10, then a new object is not created but the reference to the same integer
    object 10 that is created earlier is now stored in y. That means x and y will point to the same
    object.
"""
x = 10
y = 10
# Since they both share the same address if you compare the addresses of both these variables, they
# will be same.
print(id(x) == id(y)) # Output: True

# Now if you add 1 to y, then a new object 11 would be created and the reference to it is stored in y.
# So, now x and y will refer to different addresses.
y = y + 1
print(id(x) != id(y)) # Output: False

# If you add 1 to x, then the address of integer object 11 that is created earlier will be stored in x.
x = x + 1
print(id(x) == id(y)) # Output: True
# Now object 10 will be removed from the memory by the garbage collector.

# Now comes the trickiest thing. Let's say
x = [1,2,3,4]
y = [1,2,3,4]
print(id(x) == id(y)) # Output: False
# But if you compare the individual ids of elements inside the loop, they match.
print(id(x[0]) == id(y[0])) # Output: True
print(id(x[1]) == id(y[1])) # Output: True
print(id(x[2]) == id(y[2])) # Output: True
print(id(x[3]) == id(y[3])) # Output: True
# That means first integers will created and then a list is created with those elements.
# Hence, ids of lists do not match but ids of elements inside lists match.

# This same mechanism would cause an issue when there is variable's data sharing
x = [1,2,3,4]
y = x
# If you update y, then the change would be seen in x also
y.append(5)
print(x == y) # Output: True
# So, you have to be careful when doing such things.

# If you really need to copy data of a variable into another variable, you can use
# copy module in Python
from copy import copy, deepcopy
x = [1,2,3,4]
y = copy(x)
y.append(5)
print(x == y) # Output: False
print(x) # Output: [1,2,3,4]
print(y) # Output: [1,2,3,4,5]

# So, if there are nested list inside a list, you need to copy it using deepcopy
x = [1,2,3,[1,2,3]]
y1 = deepcopy(x)
y2 = copy(x)
y1[3].append(4)
y2[3].append(4)
print(x == y1) # Output: True
print(x != y2) # Output: True
