'''
Background:
Monotonic arrays are those whose numbers are always traveling in one direction
(are non-decreasing or non-increasing). 

Prompt:
Create a function that determines whether an input array is monotonic.

INPUT:  [1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9]
OUTPUT: TRUE

INPUT:  [1, 0, 0, 0, -1, -2, -10, -12]
OUTPUT: TRUE

'''

def main(arr):
    if arr is []:
        return True
