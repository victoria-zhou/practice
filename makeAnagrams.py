#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram_1(a, b):
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
    
    
def makeAnagram(a, b):
    letter_count_a = {}
    for letter in a:
        if letter in letter_count_a:
            letter_count_a[letter] += 1
        else:
            letter_count_a[letter] = 1
    print(letter_count_a)
    letter_count_b = {}
    for letter in b:
        if letter in letter_count_b:
            letter_count_b[letter] += 1
        else:
            letter_count_b[letter] = 1
    print(letter_count_b)
    res = 0
    for key, val in letter_count_a.items():
        res += abs(letter_count_b.get(key, 0 ) - val)
    for key, val in letter_count_b.items():
        if key not in letter_count_a:
            res += val
    return res


if __name__ == '__main__':

    a = 'aab'

    b = 'bbcctyc'

    res = makeAnagram(a, b)
    print(res)