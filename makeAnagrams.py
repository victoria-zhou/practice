#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    result1 = 0
    result2 = 0
    s1 = set(a)
    s2 = set(b)
    for letter in s1:
        if letter not in b:
            result1 += a.count(letter)
        elif a.count(letter) > b.count(letter):
            result1 += a.count(letter) - b.count(letter)
    print(result1)
    for letter in s2:
        if letter not in a:
            result2 +=b.count(letter)
        elif a.count(letter) < b.count(letter):
            result2 += b.count(letter) - a.count(letter)
    print(result2)
    return result1 + result2
    
    
    

if __name__ == '__main__':

    a = 'aab'

    b = 'bbcctyc'

    res = makeAnagram(a, b)
    print(res)