# Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in your array.

# For example, the length of your array of zeros 

import math
import os
import random
import re
import sys


def array_manipulation(n, queries): 
    data = [0] * n
    for start, end, val in queries:
        for index in range(start-1, end):
            data[index] += val
    return max(data)

assert array_manipulation(5, ([1, 2, 100], [2, 5, 100], [3, 4, 100])) == 200