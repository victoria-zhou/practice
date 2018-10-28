# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

import math
import os
import random
import re
import sys

def sock_merchant(ar):
    result = count = 0
    set1 = set(ar)
    for clor in set1:
        count = ar.count(clor)
        result += int(count/2)
        count = 0
    return result
        
assert sock_merchant([1, 2, 2, 1, 1, 3, 5, 1, 2]) == 3
assert sock_merchant([1, 2, 1, 2, 1, 3, 2]) == 2