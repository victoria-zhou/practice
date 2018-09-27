def diagonal_diff(arr):
    length = len(arr)
    diagonal_sum = 0
    anti_diagonal_sum = 0
    for index in range(length):
        diagonal_sum += arr[index][index]
        anti_diagonal_sum += arr[index][-1 - index]
    return abs(diagonal_sum - anti_diagonal_sum)

assert diagonal_diff([[11, 2, 4], [4, 5, 6], [10, 8, -12]]) == 15