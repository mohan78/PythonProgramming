#!/usr/bin/python

"""
    Program to generate fibonnaci series upto the given term
"""

from functools import lru_cache


@lru_cache
def fibonnaci(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return fibonnaci(num-1) + fibonnaci(num-2)

def main():
    n_term = int(input("Enter a number: "))
    for i in range(1, n_term+1):
        print(f"{i} : {fibonnaci(i)}")


if __name__ == '__main__':
    main()
