# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

import math
import os
import random
import re
import sys


def repeated_string(s, n):
    result = 0 
    if 'a' not in s:
        return result 
    else:
        a_freq = s.count('a')
        result = (n/len(s))*a_freq
        for i in range(n%len(s)):
            if s[i] == 'a':
                result += 1
    return result

assert repeated_string('aba', 10) == 7
assert repeated_string('a', 1000000) == 1000000