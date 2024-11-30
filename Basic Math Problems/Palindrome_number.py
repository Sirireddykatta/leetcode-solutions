# Problem: Palindrome Number
# Difficulty: Easy
# Platform: LeetCode
#
# Given an integer x, return true if x is a palindrome, and false otherwise.
#
# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#
# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. 
# Therefore it is not a palindrome.
#
# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
# Constraints:
# -2^31 <= x <= 2^31 - 1

class Solution:
    def isPalindrome(self, x: int) -> bool:
        d = 0
        rev = 0
        num = x
        if x<0:
            return False
        
        while (num!=0) :
            d=num%10
            rev = (rev*10)+d
            num=num//10
        if (x==rev):
            return True
        else:
            return False
