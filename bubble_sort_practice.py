# def bubble_sort(arr):

#     for exchange in range(len(arr)-1, 0, -1):
#         for i in range(exchange):
#             if arr[i] >= arr[i+1]:
#                 temp = arr[i]
#                 arr[i] = arr[i+1]
#                 arr[i+1] = temp

#     return arr


# print(bubble_sort([1,6,3,7,0,8]))


def short_bubble_sort(arr):
    exchange = True
    passnum = len(arr) - 1

    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if arr[i] >= arr[i+1]:
                exchange = True
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

        passnum -= 1

    return arr

print(short_bubble_sort([1,6,3,7,0,8]))


