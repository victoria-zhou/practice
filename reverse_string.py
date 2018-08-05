def reverse_string(a_str):
    reversed_str = []
    words = a_str.split()
    count = len(words)
    for i in range(count-1, -1, -1):
        reversed_str.append(words[i])
    print(' '.join(reversed_str))
    return ' '.join(reversed_str)

assert reverse_string('victor is stupid') == 'stupid is victor'
assert reverse_string('as') == 'as'