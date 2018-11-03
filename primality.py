# https://www.hackerrank.com/challenges/ctci-big-o/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=miscellaneous



import math
import os
import random
import re
import sys

def primality(n):
    if n == 2:
        return 'Prime'
    elif n == 1 or (n&1)== 0:
            return 'Not prime'
    for i in range(2, int(math.sqrt(n)) + 1):   # o(sqrt(n))
        if (n%i) == 0:
            return 'Not prime'
    return 'Prime'


assert primality(31) == 'Prime'
assert primality(33) == 'Not prime'
assert primality(2) == 'Prime'
assert primality(0) == 'Not prime'