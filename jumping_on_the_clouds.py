# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup


import math
import os
import random
import re
import sys

def jumping_on_clouds(c):
    steps = index = 0
    while index < len(c) - 1:
        if (index + 2) < len(c) and c[index + 2] == 0:
            index += 2
        elif c[index + 1] == 0:
            index += 1
        steps += 1
    return steps


assert jumping_on_clouds([0, 0, 0, 0, 1, 0]) == 3
assert  jumping_on_clouds([0, 0, 1, 0, 0, 1, 0]) == 4