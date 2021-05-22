#!/usr/bin/python

"""
    A string will be given. If number of occurrences of a charater is equal to number of
    occurrences of other characters, then print 'The string is creative' else print
    'The string is not creative'.

    For example:
    if input is 'aadb' then a message should be printed since occurrence of character a is same
    as the occurrence of other characters.
"""

def is_string_creative(string):
    """
        My strategy is to create a dictionary of occurrences of a character against the
        character in the string.
        
        Then if we substract the occurrence of a particular character from the total 
        occurrences and the difference is equal to occurrence of that character,
        the we should print 'The string is creative' else print 'The string is not creative'
    """
    occurrences_map = {}
    for i in string:
        if i in occurrences_map:
            occurrences_map[i] += 1
        else:
            occurrences_map[i] = 1

    total_occurrences = len(string)

    for i in occurrences_map:
        if total_occurrences - occurrences_map[i] == occurrences_map[i]:
            print('The string is creative')
            break
    else:
        print('The string is not creative')


if __name__ == '__main__':  
    string = input()
    is_string_creative(string)

