#!/usr/bin/python

def print_stars():
    num_of_lines = int(input("Please enter the number of lines: "))
    for j in range(num_of_lines, 0, -1):
        print("* "*j, end='\n')

    print("Finished printing")



print_stars()