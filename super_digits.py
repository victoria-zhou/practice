# https://www.hackerrank.com/challenges/recursive-digit-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking

import math
import os
import random
import re
import sys

def super_digit(n, k=0):
    n = int(n)
    if n < 10:
        return n
    if k:
        n = str(n) * k
    else:
        n = str(n)
    total = sum(int(num) for num in n)
    
    return super_digit(total)

assert super_digit(148, 3) == 3
        
