def dividing_array(arr, k):
    if k not in arr:
        return -1
    for number in arr:
        if number == k:
            return arr.index(number)

assert dividing_array([3,2,2,1], 2) == 1
assert dividing_array([3,2,2,1,4,4,4], 4) == 4