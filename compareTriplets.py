#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(tripletA, tripletB):
    score_a = score_b = 0
    for num_a, num_b in zip(tripletA, tripletB):
        if num_a > num_b:
            score_a += 1
        elif num_a < num_b:
            score_b += 1
    return [score_a, score_b]
#     s = o
#     e = 0
#     i = 0
#     for num in a:
#         if num > b[i]:
#             s += 1
#         elif num < b[i]:
#             e += 1
#         i += 1
#     return [s,e]
            

if __name__ == '__main__':
    tripletA = [5, 6, 7]
    tripletB = [5, 6, 10]
    print(compareTriplets(tripletA, tripletB))

