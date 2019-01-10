def insertion_sort(arr):
    for index in range(1, len(arr)):

        position = index
        current_value = arr[index]

        while position > 0 and arr[position-1] >= current_value:
            arr[position] = arr[position-1]
            position = position - 1

        arr[position] = current_value

    return arr


print(insertion_sort([1,6,3,4,8,2,0,3]))