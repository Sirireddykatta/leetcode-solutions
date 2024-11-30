# Problem: Reverse Integer
# Difficulty: Medium
# Platform: LeetCode
# Description:
# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], return 0.

# Examples:
# Input: x = 123
# Output: 321
#
# Input: x = -123
# Output: -321
#
# Input: x = 120
# Output: 21

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

        
