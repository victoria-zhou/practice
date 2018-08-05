#!/bin/python3

import math
import os
import random
import re
import sys

def become_binary(n):
    longest = 0
    ones = 0
    while n != 0:
        if n % 2 == 1:
            ones += 1
        else:
            if longest < ones:
                longest = ones
            ones = 0
        n = int(n/2)
    return max(longest, ones)

 

if __name__ == '__main__':
    n = int(input())
    print(become_binary(n))
