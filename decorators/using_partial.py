from functools import partial, wraps

def decorator(func=None, arg=None):
    if func is None:
        return partial(decorator, arg=arg)

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(arg)
        return func(*args, **kwargs)
    return wrapper

@decorator(arg='Mohan')
def greet():
    print('Hello')

greet()
