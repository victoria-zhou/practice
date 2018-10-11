# Given  arrays  of different sizes, find the number of distinct triplets  where  is an element of , written as , , and , satisfying the criteria: .

# For example, given  and , we find four distinct triplets: .

import math
import os
import random
import re
import sys
from bisect import bisect 

def triplets(a, b, c):
    a, b, c = sorted(set(a)), sorted(set(b)), sorted(set(c))
    return sum([bisect(a, x) * bisect(c, x) for x in reversed(c)])


print(triplets([1, 4 ,5], [2, 3, 3], [1, 2, 3]))
# assert triplets([1, 3, 5], [2, 3], [1, 2, 3]) == 8