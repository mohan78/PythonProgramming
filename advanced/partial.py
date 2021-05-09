from functools import partial


def f(a, b, c):
    return a+b+c

g = partial(f, 1, 2)

print(g(3))