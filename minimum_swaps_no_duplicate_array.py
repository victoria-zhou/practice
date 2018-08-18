import math
import os
import random
import re
import sys

def minimum_swaps(arr):
    correct_arr = sorted(arr)
    index_dic = {v: i for i,v in enumerate(arr)}
    swaps = 0
    
    for i,v in enumerate(arr):
        correct_value = correct_arr[i]
        if correct_value != v:
            swap_index = index_dic[correct_value]
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
            index_dic[v] = swap_index
            index_dic[correct_value] = i
            swaps += 1
    return swaps


assert minimum_swaps([1, 5, 8, 9, 6, 7, 4]) == 5
assert minimum_swaps([4, 3, 1, 2]) == 3
assert minimum_swaps([2, 3, 4, 1, 5]) == 3
