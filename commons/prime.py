#!/usr/bin/python

"""
    Program to display prime numbers
"""

import time

def is_prime(num):
    """
    Here we will check whether the given number is divisible by any of the numbers between 2 and square root of num plus one.
    If any one of the number in that range divides the given number, then we will return False because the number is divided by
    some number. Else we will return True since no number divided the given number.
    """
    if num == 2:
        return True

    if num > 2 and num % 2 == 0:
        return False

    for i in range(3, int(num ** 0.5)+1, 2):
        if num % i == 0:
            return False
    else:
        return True


def main():
    try:
        num = int(input("Enter the number upto which numbers should be displayed: "))
        for i in range(2, num+1):
            if is_prime(i):
                print(f"{i} is a prime number")
            else:
                print(f"{i} is not a prime number")
    except TypeError as e:
        print(f"Invalid number supplied {e}")

if __name__ == '__main__':
    main()
