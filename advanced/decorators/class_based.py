class Decorate:

    def __init__(self, function):
        self.f = function

    def __call__(self, *args, **kwargs):
        print("Executing the decorated function")
        self.f(*args, **kwargs)

@Decorate    
def decorated_greet(name):
    print(f"Hello, {name}")

def undecorated_greet(name):
    print(f"Hello, {name}")

print('-'*30, ' Executing decorated function ', '-'*30)
decorated_greet('Mohan')
print('-'*30, ' Executing undecorated function ', '-'*30)
undecorated_greet('Mohan')