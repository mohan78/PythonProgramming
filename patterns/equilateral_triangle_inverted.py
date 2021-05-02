#!/usr/bin/python

"""
pattern name: Inverted equilateral triangle

The pattern should look like this:

* * * * * * * *
 * * * * * * *
  * * * * * *
   * * * * *
    * * * *
     * * *
      * *
       *

"""

def print_stars():
    num_of_lines = int(input("Please enter the number of lines: "))
    for j in range(num_of_lines, 0, -1):
        print(" "*(num_of_lines-j), end='')
        print("* "*j, end='\n')

    print("Finished printing")



print_stars()