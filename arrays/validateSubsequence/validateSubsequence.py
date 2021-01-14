def main(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        elif sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)
'''
1)
    arrIndex = 0
    seqIndex = 0

    while arrIndex < len(array) and seqIndex < len(sequence):

        if array[arrIndex] == sequence[seqIndex]:
            seqIndex += 1
        arrIndex += 1

    return seqIndex == len(sequence) 
'''
