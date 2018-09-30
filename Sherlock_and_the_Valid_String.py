import math
import os
import random
import re
import sys
from collections import Counter

def is_valid(s):
    letter_counters = Counter(s)
    counter_counters = Counter(letter_counters.values()) # counter() returnes a dictionary
    counters = len(counter_counters)
    if counters == 1:
        return 'YES'
    elif counters == 2:
        # print(counter_counters)
        if counter_counters.get(1) == 1:
            return 'YES'
        cc = list(counter_counters.items())
        if (cc[0][1] == 1 and cc[0][0] - cc[1][0] == 1
            or cc[1][1] == 1 and cc[1][0] - cc[0][0] == 1):
            return 'YES'
    return 'NO'


 
assert is_valid('aabbcd') == 'NO'
assert is_valid('aabbccddeefghi') == 'NO'
assert is_valid('a') == 'YES'