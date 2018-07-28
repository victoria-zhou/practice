#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * tip_percent
    tax = meal_cost * tax_percent
    totalCost = meal_cost + tip + tax
    roundedTotal = round(totalCost)
    print ('The total meal cost is '+ str(roundedTotal) + ' dollars.')

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
