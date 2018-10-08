# Given an array of integers, find the subset of non-adjacent elements with the maximum sum. Calculate the sum of that subset.

# For example, given an array  we have the following possible subsets:

# Subset      Sum
# [-2, 3, 5]   6
# [-2, 3]      1
# [-2, -4]    -6
# [-2, 5]      3
# [1, -4]     -3
# [1, 5]       6
# [3, 5]       8


import math
import os
import random
import re
import sys

def max_subset_sum(arr):
    incl = excl = temp = 0
    for item in arr:
        temp = incl
        incl = max(item + excl, temp);
        excl = temp
    return max(incl, excl)

assert max_subset_sum([3, 5, -7, 8, 10]) == 15
assert max_subset_sum([2, 1, 5, 8, 4]) == 11