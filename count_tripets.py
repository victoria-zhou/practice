import math
import os
import random
import re
import sys
from collections import defaultdict

def count_triplets(arr, r):
    v2 = defaultdict(int)
    v3 = defaultdict(int)
    count = 0
    for k in arr:
        count += v3[k]
        v3[k*r] += v2[k]
        v2[k*r] += 1

        print(v3[k*r])
        print(v2[k*r])

    return count





print(count_triplets([1,2,2,4],2))