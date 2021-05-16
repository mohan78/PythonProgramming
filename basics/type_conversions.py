"""
    Type casting is the process of converting one datatype into another.
    i.e. in Python, you can convert float to int, tuple to list etc.
"""

# 1. Converting float to int will remove the decimals after point
x = 2.002
x = int(x)
print(x) # Output: 2

# 2. Converting int to float will add decimals after the number
x = 2
x = float(x)
print(x) # Output: 2.0

# 3. Converting a string to list will convert each character in a string to
# single element in list. Same for tuple
x = 'hello'
x = list(x)
print(x) # Output: ['h', 'e', 'l', 'l', 'o']

# 4. Converting a list to tuple will change type to tuple without altering the
# element indices. Vice versa for tuple to list.
x = [1, 2, 3, 4]
x = tuple(x)
print(x) # Output: (1, 2, 3, 4)

# 5. Converting a dictionary to list results in list containing all the keys of the
# dictionary. Same for dictionary to tuple
x = {1: 'a', 2: 'b', 3: 'c'}
x = list(x)
print(x) # Output: [1, 2, 3]

# 6. Converting a list to set will result in a set with no duplicate elements
x = [1, 2, 3, 2, 3, 4]
x = set(x)
print(x) # Output: {1, 2, 3, 4}

"""
    The following conversions will result in an exception

    string -> int
    string -> float
    list -> dict
    tuple -> dict
"""

# ------------------------------------- Boolean conversions -------------------------------------

# The following Boolean conversions will result in True
bool(1)
bool(2.0)
bool('a')
bool([1])
bool(['a'])
bool({1: 'a'})
bool((1,))

# The following Boolean conversions will result in False
bool(0)
bool(0.0)
bool('')
bool([])
bool(())
bool({})
bool(None)
