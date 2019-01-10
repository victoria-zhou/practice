def count_vowels(str):
    lower_str = str.lower()
    result = 0

    for char in lower_str:
        if char in ('a', 'e', 'i', 'o', 'u'):
            result += 1

    return result 


print(count_vowels('Graduate Opportunities'))