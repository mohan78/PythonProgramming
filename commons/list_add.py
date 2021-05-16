"""
    Write a program to add elements in two lists.

    For example:
    x = [1,2,4]
    y = [4,5,6]

    on adding x and y we should get [5, 7, 10].
"""

x = [1,2,4]
y = [4,5,6]

resultant = []

for i in range(0, len(x)):
    sum = x[i] + y[i]
    resultant.append(sum)

print(f'The sum of given lists {x} and {y} is {resultant}')
