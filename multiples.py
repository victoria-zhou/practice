import math
import os
import random
import re
import sys

def multiples(n):
    for i in range(1,11):
    	#2 x 1 = 2
        print("%i x %i = %i" % (n, i, n*i))


print(multiples(2))
print(multiples(6))