def print_heading(message):
    def inner_function(func):
        def wrapper(*args, **kwargs):
            print('-'*30, f' Executing {message} function ', '-'*30)
            return func(*args, **kwargs)
        return wrapper
    return inner_function

class Decorate:

    def __init__(self, function):
        self.f = function

    def __call__(self, *args, **kwargs):
        print("Hi, I am decorated")
        self.f(*args, **kwargs)

@print_heading('decorated')
@Decorate    
def decorated_greet(name):
    print(f"Hello, {name}")

@print_heading('undecorated')
def undecorated_greet(name):
    print(f"Hello, {name}")

decorated_greet('Mohan')
undecorated_greet('Mohan')