# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup


import math
import os
import random
import re
import sys


def counting_valleys(s):
    result = valley = 0
    for letter in s:
        if letter == "U":
            result += 1
        else:
            result -= 1
        if result == 0 and letter == "U":
           valley += 1
    return valley


assert counting_valleys("UDDDUDUU'") == 1
