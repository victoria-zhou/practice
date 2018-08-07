from collections import defaultdict

def minimum_distance(strs, str1, str2):
    if str1 not in strs or str2 not in strs:
        return -1
    elif str1 == str2:
        return 0

    str_pos = defaultdict(list)
    for index, item in enumerate(strs):
        if item in (str1, str2):
            str_pos[item].append(index)
    min_dist = len(strs)

    for pos1 in str_pos[str1]:
        for pos2 in str_pos[str2]:
            dist = abs(pos1 - pos2)
            if dist < min_dist:
                min_dist = dist
    
    return min_dist

assert minimum_distance([1, 2, 3, 4, 5, 6, 7, 8], 5, 7) == 2
assert minimum_distance([1, 2, 3, 4, 5, 6, 7, 8, 5], 5, 7) == 2
assert minimum_distance([1, 2, 3, 4, 5, 6, 7, 8, 5, 7], 5, 7) == 1