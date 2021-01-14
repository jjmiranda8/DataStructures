'''
Given two non-empty arrays of integers, write a function that 
determines if the second array is a subsequence of the first. 

The numbers of the first array don't have to be adjacent, but
they do need to be in order of the second array to count as a 
subsequence.

INPUT:
[5, 1, 22, 25, 6, -1, 8, 10]
[1, 6, -1, 10]

OUTPUT:
True

SOLUTIONS:
1) Create pointers of the index of both arrays. While the pointers are less than
the length of both the first AND the second arrays check if the numbers at the 
positions of each array == each other. If yes, we've found one of the sequence numbers,
and increment the seqIndex pointer. Regardless, increment the arrIndex pointer. 
If after the while condition is over the len(sequence) == seqIndex, you've found 
the sequence exists in the first array (True)

def isValidSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0

    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1

    return seqIdx == len(sequence)

2) Create a pointer for the seqIdx. We will loop through the main array and if 
the seqIdx == len(sequence), break because we've found sequence. If the value is 
equal to sequence(seqIdx), we've found one match so increment seqIdx += 1. Return
seqIdx == len(sequence).

def isValidSubsequence(array, sequence):
    seqIdx = 0

    for value in array:
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)

'''
