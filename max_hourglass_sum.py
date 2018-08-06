#!/bin/python3

import math
import os
import random
import re
import sys

def max_hourglass_sum(arr):
    size = len(arr)
    hour_sum = 0
    result = -math.inf #know how to represent infinity in python
    for i in range (size-2):
        for j in range(size-2):
            hour_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] +arr[i+2][j+1] + arr[i+2][j+2] # sum(arr[][]+ arr[]) will give error: list + interger does not work
            if hour_sum > result:
                result = hour_sum
    return result


if __name__ == '__main__':
    # arr = []
    arr=[[1,2,3,4], [2,3,4,5], [3,4,5,7],[3,4,5,6]] #know how to represent list of list
    # print('Please give an integer')
    # n = int(input())
    # for _ in range(n):
    #     print(f'Please give {n} numbers')
    #     arr.append(list(map(int, input().rstrip().split())))
    print(max_hourglass_sum(arr))
