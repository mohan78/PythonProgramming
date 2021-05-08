#!/usr/bin/python

def decorate_me(f):
    def inner():
        print("I am being decorated")
        f()
        print("Inner execution completed")
    return inner


@decorate_me
def decorated_greet():
    print("Hello world")


def undecorated_greet():
    print("Hello world")


if __name__ == '__main__':
    print("Executing undecorated function")
    undecorated_greet()
    print("#"*30)
    print("Executing decorated function")
    decorated_greet()
    
