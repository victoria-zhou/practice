

#https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

def array_manipulation(n, queries):
    my_array = [0] * (n+1)
    count = 0
    temp = 0
    for first,last,value in queries:
        
        my_array[first-1] += value
        my_array[last] -= value
    
    for item in my_array:
        count += item
        if count > temp:
            temp = count
       
    return temp

assert array_manipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]) == 200