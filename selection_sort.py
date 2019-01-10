def selection_sort(arr):
    size = len(arr)
    for fill_slot in range(size-1, 0, -1):
        max_index = 0
        for location in range(1, fill_slot+1):
            if arr[location] >= arr[max_index]:
                max_index = location

        temp = arr[fill_slot]
        arr[fill_slot]= arr[max_index]
        arr[max_index] = temp


    return arr


print(selection_sort([4,3,1,1,6,7]))

print(selection_sort([4,5,2,3,1,6,8,9]))