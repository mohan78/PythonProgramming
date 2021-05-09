"""
    A class is a blueprint that is used to create objects in python. A class is nothing
    but collection of data and methods that operate on that data. A class can be created
    using the keyword 'class'. 

    Naming convention: A class name should follow CamelCase with the starting letter in uppercase
"""

class Car:
    
    pass


"""
    The above class Car is defined with no data and methods. We can create objects of Car type
    but it will not have any data or methods to access. If we try to access any attribute of an
    object that doesn't exist, it will raise an AttributeError exception.
"""

car = Car() # An object is created like this.
# In the above example, 'car' is an object created using class 'Car'.
# 'car' is called instance of class 'Car'.


class Car:
    """
        This class has now an initialization method will accept attributes and creates objects
        with those attributes. An attribute of an object can be accessed using .(dot) operator.
    """

    def __init__(self, kind, color, company):
        self.kind = kind
        self.color = color
        self.company = company


# We can create an object as below when there is an init method.
ferrari = Car(kind='Hatchback', color='Red', company='Ferrari')
tata = Car(kind='Sedan', color='Black', company='Tata')

print(f"Color of ferrari is {ferrari.color}")    # Output: Red
print(f"Color of tata is {tata.kind}")        # Output: Sedan


class Car:
    """
        Now I have added some functions (called methods of class). A method of a class will act on the
        data or attributes of an object.
    """

    def __init__(self, kind, color, company):
        self.kind = kind
        self.color = color
        self.company = company

    def is_hatchback(self):
        # This method will return true if the kind of the object is equal to Hatchback.
        return self.kind == 'Hatchback'
    
ferrari = Car(kind='Hatchback', color='Red', company='Ferrari')
tata = Car(kind='Sedan', color='Black', company='Tata')

print(f"Ferrari is a hatchback: {ferrari.is_hatchback()}")   # Output: True
print(f"tata is a hatchback: {tata.is_hatchback()}")      # Output: False


"""
    You may have noticed the parameter 'self' in the is_hatchback method the class. Every first argument to
    a method inside a class is 'self'. It becomes the actual class during runtime.

    for example, when we access is_hatchback method of ferrari using dot operator, it becomes like below
    ferrari.is_hatchback() => Car.is_hatchback(ferrari). That convention is for our convenience in writing
    programs.

    If you execute those two commands, you can see that both the results will be.
"""

print(ferrari.is_hatchback())       # Output: True
print(Car.is_hatchback(ferrari))    # Output: True
