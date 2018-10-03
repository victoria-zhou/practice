# You will be given an array of integers and a target value. Determine the number of pairs of array elements that have a difference equal to a target value.

# For example, given an array of [1, 2, 3, 4] and a target value of 1, we have three values meeting the condition: , , and .


def pairs(k, arr):
    pairs = {}
    results = []
    for item in arr:
        pairs[item + k] = item
    results = [[item, pairs[item]] for item in arr if item in pairs ]
    return len(results)


assert pairs(2, [1, 5, 3, 4, 2]) == 3
assert pairs(1, [1, 2, 3, 4]) == 3