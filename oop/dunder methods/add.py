"""
    we can use __add__ to define the logic that needs to be performed on the instances
    that are being summed or added.
"""

class Coordinates:
    """
        We are creating a class which instances represent the position of a point in a
        2D plane. Let's say the coordinates are x and y.

        So two different point can be represented as x1, y1 and x2, y2. When we need to
        add two coordinates, we need to add x1 to x2 and y1 to y2. So, we need to use
        the __add__ method, to perform the addition as specified above.
    """
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Coordinates):
            raise TypeError('Both the instance need to be of same type in order to be added')
        return (self.x+other.x, self.y+other.y)


point1 = Coordinates(2, 3)
point2 = Coordinates(4, 5)

print(point1+point2) # Output: (6, 8)
# The above code should print the added coordinates are 6, 8 since 2+4=6, 3+5=8

# Same for __sub__ for substraction, __mul__ for multiplication, __divmod__ for divmod operation.
