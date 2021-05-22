"""
    We can use __str__ method to format the way information is displayed for an instance. It is
    called when we apply 'print' or 'str' method on the instance.
"""

class Sample:
    
    def __init__(self, first_name) -> None:
        self.first_name = first_name


sample = Sample('Mohan')
print(sample) # Output: <__main__.Sample object at some_hex_code>


class Sample:

    def __init__(self, first_name) -> None:
        self.first_name = first_name

    def __str__(self) -> str:
        return f'instance of Sample class with first_name as {self.first_name}'


sample = Sample('Mohan')
print(sample) # Output: instance of Sample class with first_name as Mohan

# As you can see above, now we have some understandable information about the instance
# when it is printed.
