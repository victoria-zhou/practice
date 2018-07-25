#!/bin/python3


def simpleArraySum(ar):
    sum = 0
    for number in ar:
        sum = sum + number

    return sum


if __name__ == '__main__':
   ar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
   print(simpleArraySum(ar))