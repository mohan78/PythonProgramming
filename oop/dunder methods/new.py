"""
    __new__ is a magic method that is responsible for object or instance creation for a class.

    It is the first magic method that is called when an object is instansiated i.e. created. This
    method in turn calls the __init__ method implicitly.

    By using this methods, we can customize the object creation in Python. __new__ takes the class
    itself as the first parameter (we can say, class method).
"""

class Sample:
    """
        Let's create a class that takes first_name as an attribute
    """

    def __new__(cls, first_name):
        print('calling __new__ method')
        instance = object.__new__(cls)
        print('Do something in __new__')
        return instance.__init__(first_name)

    def __init__(self, first_name) -> None:
        print('calling __init__ method')
        self.first_name = first_name


sample = Sample('Mohan')

# Output:
# calling __new__ method
# Do something in __new__
# calling __init__ method

# As you can see above output, __new__ will be called first along with the class and attributes that
# are required to instansiate the object. In our case, it is 'first_name'. It will make an instance
# using the base object.__new__ method. Then initialize will be called by passing it the necessary
# or expected attributes that are needed to instansiate the object.

# __init__ method is responsible for setting the attributes for an object. It requires the instance
# itself as the first parameter i.e. 'self'.
