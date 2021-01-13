'''
PROMPT
Write a function that takes in a non-empty array of distinct integers and an
integer representing a target sum. If any two numbers in the input arrray sum 
up to the target sum, the function should return them in an array, in any order.
If no two numbers sum up to the target sum , the function should return an
empty array. 

SAMPLE INPUT:
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum =  10

SAMPLE OUTPUT:
[-1, 11]


There are three common ways to solve this question with different time 
complexities:

1)
We could use 2 for loops: at each number of the array, traverse the entire array
again and see if the original array number and any of the other numbers add up 
to the target sum. Start traverseing the second array from the current number 
of the first loop, not the entire array again. TIME: O(n**2)

def main(array, targetSum):
    for i in range(len(array)-1:

        firstNum = array[i]
        for j in range(i + 1, len(array)):
        secondNum = array[j]
        if firstNum + secondNum == targetSum:
            return [firstNum,  secondNum]
    return []


2)
First sort the array. Create a left pointer (L) at the start of the array. Create
a right pointer (R) at the end of the array. Sum up the two numbers that L and R
point to. If the sum is larger than the targetSum, move the R pointer to the left,
and because the array is sorted, the next time we sum the pointers, the summed number
will be smaller. If sum is too small, move L to the right and the sum will be larger.
If target sum is found return array of [L, R] else return []. TIME: O(n(log(n)))

def main(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []


3)
Create a hash, loop through array and if the targetSum minus the current number 
is not within the hash we created, move to the next number. If the targetSum -
current num is inside the hash, return the number in the hash and the current num 
that add up to the targetSum in an array. TIME: O(n) 

def main(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []
'''
