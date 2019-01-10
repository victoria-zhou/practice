# def remove_duplicate(str):
#     result = []

#     for each in str:
#         if each not in result or each == ' ':
#             result.append(each)


#     return ''.join(result)

# print(remove_duplicate('AAA B CC DD AA'))


def remove_duplicate(str):
    result = []

    for each in str:
        if each not in result and each != ' ':
            result.append(each)


    return ''.join(result)

print(remove_duplicate('AAA B CC DD AA'))