#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(arr, rot_times):
    return arr[rot_times:] + arr[:rot_times]
    # for index in range(d):
    #     temp = a[0]
    #     for number in range(1, len(a)):
    #         a[number-1]=a[number]
    #     a[len(a)-1] = temp
    # return a
        

arr = [1,2,3,4,5]
print arr
print(rotLeft(arr,4))

arr = [1,2,3,4,5,6,8,9]
print arr
print(rotLeft(arr,5))
