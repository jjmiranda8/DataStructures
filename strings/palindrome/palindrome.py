'''
PROMPT  
Create a function that checks whether an input string is a palindrome
SAMPLE INPUT 

SAMPLE OUTPUT

'''

def isPalindrome(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True 
