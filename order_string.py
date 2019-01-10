 # In a given string for example 'sadbcg' how to rearrange them into alphabetical order which means the solution will be 'abcdgs'. 


def order_string(str):
    str_list = list(str)
    for fillslot in range(len(str_list)-1, 0, -1):
        max_index = 0
        for j in range(1, fillslot+1):
            if str_list[j] >= str_list[max_index]:
                max_index = j


        temp = str_list[fillslot]
        str_list[fillslot] = str_list[max_index]
        str_list[max_index] = temp

    return ''.join(str_list)

print(order_string('adbcoegiht'))