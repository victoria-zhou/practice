#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    for index in range(d):
        temp = a[0]
        for number in range(1, len(a)):
            a[number-1]=a[number]
        a[len(a)-1] = temp
    print(a)
    return a


if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)
