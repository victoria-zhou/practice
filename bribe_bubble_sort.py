import math
import os
import random
import re
import sys

def minimumBribes(q):
    result = 0
    size = len(q)
    swaped = False 
    
    for i, v in enumerate(q):
        if (v - 1- i) > 2:
           return "Too chaotic"
    
    
    for j in range(size):
        for k in range(size - 1):
            if q[k]>q[k+1]:
                temp = q[k+1]
                q[k+1] = q[k]
                q[k] = temp
                result += 1
                swaped = True 
        if swaped:
            swaped = False 
        else:
            break
    return result


assert minimumBribes([2,1,5,3,4])==3
assert minimumBribes([2,5,1,3,4])=="Too chaotic"
