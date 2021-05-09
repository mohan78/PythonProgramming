from functools import wraps

def set_min_temp(temp):
    """
    Decorator to check whether the given 
    """
    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if args[0] < temp:
                raise ValueError(f"Setting temperature cannot be less than {temp}")
            return function(*args, **kwargs)
        return wrapper
    return inner_function
    

@set_min_temp(2)
def convert_temp(temp):
    return temp * (9/5) + 32

temp = int(input("Enter the temperature: "))
result = convert_temp(temp)
print(f"{temp} converted to farenheit is {result}")
