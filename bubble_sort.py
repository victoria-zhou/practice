def bubble_sort(a):
    swap_num = 0
    size = len(a)
    for i in range(size):
        for j in range(i-1,-1,-1):
            if a[j+1]<a[j]:
                temp = a[j+1]
                a[j+1]=a[j]
                a[j] = temp
                swap_num += 1
    
    print("Array is sorted in", swap_num, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[size-1])

bubble_sort([1,2,3])
bubble_sort([1,3,2])

