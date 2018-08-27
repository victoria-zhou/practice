def reverseArray(a):
    reverse_a = []
    for item in a[::-1]:
        reverse_a.append(item)
    return reverse_a

assert reverseArray([3, 4, 1, 2]) == [2, 1, 3, 4]
