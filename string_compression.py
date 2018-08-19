# naive approach using string, string is immutable, thus requires more run time
# def str_compression(str1):
#     compare_str = str1[0]
#     result = ''
#     count = 0
#     for i in range(len(str1)):
#         if compare_str == str1[i]:
#             count += 1
#         else:
#             result += (str1[i-1] + str(count))
#             compare_str = str1[i]
#             count = 1
#     result +=(str1[i] + str(count)) # This is for the last letter to be counted and added to result.
#     return ''.join(map(str, result))


# print(str_compression('aaacccbbb'))
# print(str_compression('aaacccCbbb'))
# print(str_compression('aaacccbbbD'))

# def str_compression2(str2):
#     compare_str = str2[0]
#     result = []
#     count = 0
#     for i in range(len(str2)):  # using char in str2 is better, range takes time
#         if compare_str == str2[i]:
#             count += 1
#         else:
#             result.append(str2[i-1])
#             result.append(count)
#             compare_str = str2[i]
#             count = 1
#     result.append(str2[i])
#     result.append(str(count))
#     return ''.join(map(str,result))

# def str_compression2(str2):
#     result = []
#     prev = None
#     for char in str2:
#         if not prev:
#             prev = char
#             count = 1
#         elif char == prev:
#             count += 1
#         else:
#             prev = char
#             count = 1
#             if count == 1:
#                 result.append(char)
#             else:
#                 result.append(f'{char}{count}')
#     return ''.join(result)

def str_compression2(str2):
    result = []
    prev = None
    for char in str2:
        if not prev:
            prev = char
            count = 1
        elif char == prev:
            count += 1
        else:
            result.append(f'{prev}{count}')
            prev = char
            count = 1
    result.append(f'{char}{count}')
    return ''.join(result)

  

print(str_compression2('aaacccbbb'))
print(str_compression2('aaacccCbbb'))
print(str_compression2('aaacccbbbD'))

