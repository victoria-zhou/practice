# def merge_sort(lists):
#     if len(lists) <= 1:
#         return lists
#     middle = len(lists)/2
#     left = merge_sort(lists[:middle])
#     right = merge_sort(lists[middle:])
#     return merge(left, right)


# if __name__ == '__main__':
#     a = [4, 7, 8, 3, 5, 9]
#     print merge_sort(a)

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr)/2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr
    print merge_sort([4,8,9,1,3])