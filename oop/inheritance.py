"""
    Inheritance in Object Oriented terms is the method of acquiring access to attributes and methods from one class by
    another class. The class from which attributes and methods are acquired is called "parent" class and the one which
    acquires is called "child" class.

    Syntax:
    
    class ChildClass(ParentClass):
        pass
"""

# For example let's create a Parent class Car and extend it to a HatchBack class

class Car:

    def __init__(self, color, company) -> None:
        self.color = color
        self.company = company


    def is_car_black(self):
        # Returns True if the color of the car is black else returns False
        return self.color.lower() == 'black'


class HatchBack(Car):
    
    def __init__(self, color, company, boot_size, engine_cc) -> None:
        # Here we need to inherit the attributes of parent class using the keyword super. without this statement,
        # the init method of this class overrides the Parent class.
        super().__init__(color, company)
        self.boot_size = boot_size
        self.engine_cc = engine_cc

    def is_sports_car(self):
        # If the engine power of an hatchback object is greater than 1000, it is a sports car
        return self.engine_cc >= 1000


class SedanCar(Car):
    def __init__(self, color, company, engine_cc, seating_cap) -> None:
        super().__init__(color, company)
        self.engine_cc = engine_cc
        self.seating_cap = seating_cap


    def is_5_seater(self):
        # Returns True if the seating capacity of the given object is 5 else returns False
        return self.seating_cap == 5


# Method overriding

"""
    We can choose to override a method by giving the method name same as the name in the parent class. Thus we
    can override (overwrite) the functionality of Parent class to suit our needs.
"""