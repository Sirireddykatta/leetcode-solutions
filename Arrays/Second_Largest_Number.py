'''
Problem statement
You have been given an array ‘a’ of ‘n’ unique non-negative integers.



Find the second largest and second smallest element from the array.



Return the two elements (second largest and second smallest) as another array of size 2.



Example :
Input: ‘n’ = 5, ‘a’ = [1, 2, 3, 4, 5]
Output: [4, 2]

The second largest element after 5 is 4, and the second smallest element after 1 is 2.
'''
def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    small = float("inf")
    second_small = float ("inf")
    large = float ("-inf")
    second_large = float ("-inf")
    for i in range(0,len(a)):
        if a[i]<small:
            second_small = small
            small = a[i]
        elif a[i]<second_small and a[i]!= small:
            second_small = a[i]
        if a[i]>large:
            second_large = large
            large = a[i]
        elif a[i]>second_large and a[i]!= large:
            second_large = a[i]
    return [second_large,second_small]
