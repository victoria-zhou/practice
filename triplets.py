# https://www.hackerrank.com/challenges/triple-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search



import math
import os
import random
import re
import sys

def triplets(a, b, c):
    setb = set(b)
    result = fst_count = lst_count = 0
    
    for mid in setb:
        for fst in a:
            if mid >= fst:
                fst_count += 1
        
        for lst in c:
            if mid >= lst:
                lst_count += 1
        
        result += fst_count * lst_count
        fst_count = lst_count = 0
    return result

assert triplets([1, 3, 5, 7], [5, 7, 9], [7, 9, 11, 13]) == 12
assert triplets([1, 4, 5], [2, 3, 3], [1, 2, 3]) == 5
