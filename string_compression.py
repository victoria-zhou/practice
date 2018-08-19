# from io import StringIO
import time

# print('-------- Method 1: String --------')
# #naive approach using string, string is immutable, thus requires more run time

# start_time1 = time.time()

# def str_compression1(str1):
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


# assert str_compression1('aaacccbbb') == 'a3c3b3'
# assert str_compression1('aaacccCbbb') == 'a3c3C1b3'
# assert str_compression1('aaacccbbbD') == 'a3c3b3D1'

# print("--- %f seconds ---" % (time.time() - start_time1))

# print('-------- Method 2: list + range --------')

# start_time2 = time.time()
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

# assert str_compression2('aaacccbbb') == 'a3c3b3'
# assert str_compression2('aaacccCbbb') == 'a3c3C1b3'
# assert str_compression2('aaacccbbbD') == 'a3c3b3D1'
# print("--- %f seconds ---" % (time.time() - start_time2))

print('-------- Method 3: list + char, better result.append position --------')
start_time3 = time.time()
def str_compression3(str2):
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
assert str_compression3('aaacccbbb') == 'a3c3b3'
assert str_compression3('aaacccCbbb') == 'a3c3C1b3'
assert str_compression3('aaacccbbbD') == 'a3c3b3D1'
print("--- %f seconds ---" % (time.time() - start_time3))

# print('-------- Method 4: StringIO --------')
# start_time4 = time.time()
# def str_compression4(str2):
#     file_str = StringIO()
#     prev = None
#     for char in str2:
#         if not prev:
#             prev = char
#             count = 1
#         elif char == prev:
#             count += 1
#         else:
#             file_str.write(f'{prev}{count}')
#             prev = char
#             count = 1
#     file_str.write(f'{char}{count}')  
#     return file_str.getvalue()
# assert str_compression4('aaacccbbb') == 'a3c3b3'
# assert str_compression4('aaacccCbbb') == 'a3c3C1b3'
# assert str_compression4('aaacccbbbD') == 'a3c3b3D1'
# print("--- %f seconds ---" % (time.time() - start_time4))
