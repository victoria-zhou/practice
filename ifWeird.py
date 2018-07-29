#!/bin/python3

import math
import os
import random
import re
import sys

def ifWeird(n):
    if (n%2 == 1):
        w = 'Weird'
    elif (n>=2 and n<=5):
        w = 'Not Weird'
    elif (n>=6 and n<=20):
        w = 'Weird'
    elif (n>20):
        w = 'Not Weird'
    return w


if __name__ == '__main__':
    print('Please type an integer')
    N = int(input())
    print(ifWeird(N))
