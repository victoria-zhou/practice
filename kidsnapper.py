#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    word_count_mag = {}
    word_count_note = {}
    for word in magazine:
        if word in word_count_mag:
            word_count_mag[word] +=1
        else:
            word_count_mag[word] = 1
    for letter in note:
        if letter in word_count_note:
            word_count_note[letter] +=1
        else:
            word_count_note[letter] = 1
    for key, val in word_count_note.items():
        if key in word_count_mag and val <= word_count_mag[key]:
            continue
        else:
            return 'No'
    return 'Yes'

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))