import math
import os
import random
import re
import sys

def maximum_toys(prices, k):
    prices = sorted(prices)
    toys = []
    for price in prices:
        k -= price
        if k>0:
            toys.append(price)
        else:
            break
    return len(toys)



assert maximum_toys([1, 12, 5, 111, 200, 1000, 10], 50) == 4