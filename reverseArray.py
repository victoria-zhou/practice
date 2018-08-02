import math
import os
import random
import re
import sys
from array import array

def reverseArray(arA):
    arB = []
    j = 0
    for i in range(len(arA)-1,-1,-1):
        arB.append(arA[i])
    return arB

if __name__ == '__main__':
    
	arr = [1,2,3,4,5]
    
	print(reverseArray(arr))