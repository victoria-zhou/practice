# https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking

import math
import os
import random
import re
import sys

result_map = {
    1: 1,
    2: 2,
    3: 4,
}

def step_perms(n):
    if n in result_map:
        return result_map[n]
    else:
        result = step_perms(n-1)
        result += step_perms(n-2)
        result += step_perms(n-3)
        result_map[n] = result
        return result

assert step_perms(1) == 1
assert step_perms(5) == 13
assert step_perms(7) == 44

