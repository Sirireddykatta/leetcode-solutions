# Problem: Count Digits
# Difficulty: Easy
# Accuracy: 30.45%
# Submissions: 353K+
# Points: 2

# Given a positive integer n, count the number of digits in n that divide n evenly (i.e., without leaving a remainder).
# Return the total number of such digits.

# A digit d of n divides n evenly if the remainder when n is divided by d is 0 (n % d == 0).
# Digits of n should be checked individually. If a digit is 0, it should be ignored because division by 0 is undefined.

# Examples:

# Input: n = 12
# Output: 2
# Explanation: 1, 2 when both divide 12 leaves remainder 0.

# Input: n = 2446
# Output: 1
# Explanation: Here among 2, 4, 6 only 2 divides 2446 evenly while 4 and 6 do not.

# Solution:
class Solution:
    def evenlyDivides(self, n):
        # Initialize count of digits that divide n
        count = 0
        # Copy the original number
        num = n
        # Check each digit of the number
        while n > 0:
            d = n % 10  # Get the last digit
            if d != 0 and num % d == 0:  # Check if it divides n evenly
                count += 1
            n = n // 10  # Remove the last digit
        return count
