"""
    Python does not generally support the concept of private variable like in Java i.e.
    they will still be accessible from the object. They are not hidden.

    But in general practice, if a attribute or a method is made private, then it means
    they should be accessed outside the class i.e. the developer needs to take care that
    they are not accessed outside although Python doesn't throw an error.
"""

class Employee:
    
    def __init__(self, first_name, last_name, salary) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self._salary = salary # Here salary is made private by appending '_' (underscore)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def _get_salary_band(self):
        return self._salary / 10 # Accessing private variable inside a class is allowed.


mohan = Employee('mohan', 'peddapuli', 32000)
print(mohan._salary) # Even though this works, we should not do this.
print(mohan._get_salary_band()) # Same as above.


"""
    To really hide variable from getting accessed accidentally by users, we can do that by
    appending two underscores(__) to the attribute.
"""

class Employee:
    
    def __init__(self, first_name, last_name, salary) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.__salary = salary

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_salary_band(self): # Made a normal method
        return self.__salary / 10 # Inside the class, we can access this.


mohan = Employee('mohan', 'peddapuli', 32000)
# print(mohan.__salary) This wont work
print(mohan.get_salary_band())
