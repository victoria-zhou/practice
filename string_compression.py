def str_compression(str1):
    compare_str = str1[0]
    result = ''
    count = 0
    for i in range(len(str1)):
        if compare_str == str1[i]:
            count += 1
        else:
            result += (str1[i-1] + str(count))
            compare_str = str1[i]
            count = 1
    result +=(str1[i] + str(count)) # This is for the last letter to be counted and added to result.
    return ''.join(map(str, result))


print(str_compression('aaacccbbb'))
print(str_compression('aaacccCbbb'))
print(str_compression('aaacccbbbD'))

