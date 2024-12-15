"""
Given an array of n integers, your task is to find the maximum sum of values in a contiguous, nonempty subarray.

Input
The first input line has an integer n: the size of the array.
The second line has n integers x1,x2, ... ,xn: the array values.

Output
Print one integer: the maximum subarray sum.
"""

def max_subarray_sum(n, arr):
    """
    Implements max_subarray_sum function to find the maximum sum of a contiguous subarray.
    
    Parameters:
        n (int): The size of the array.
        arr (list): A list of integers of length n.
    
    Returns:
        int: The maximum sum of any contiguous subarray.
    """    
    max_sum = arr[0]
    current_sum = arr[0]
    
    for i in range(1, n):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# ------------
# Input data
# ------------
n = int(input())
arr = list(map(int, input().split()))

# ------------
# Output
# ------------
output = max_subarray_sum(n, arr)
print(output)
