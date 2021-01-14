def main(array, sequence):
    arrIdx = 0
    seqIdx = 0

    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1

    return seqIdx == len(sequence)
'''
    arrIndex = 0
    seqIndex = 0

    while arrIndex < len(array) and seqIndex < len(sequence):

        if array[arrIndex] == sequence[seqIndex]:
            seqIndex += 1
        arrIndex += 1

    return seqIndex == len(sequence) 
'''
