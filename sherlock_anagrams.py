def sherlock_anagrams(s):
    size = len(s)
    result = 0
    for l in range(1, size):
        count_dic = {}
        for i in range(size - l + 1):
            subs = list(s[i:i + l])
            subs.sort()
            subs = ''.join(subs)
            if subs in count_dic:
                count_dic[subs] += 1
            else:
                count_dic[subs] = 1
            result += count_dic[subs] - 1
    return result

assert sherlock_anagrams('ifailuhkqq') == 3
assert sherlock_anagrams('kkkk') == 10
assert sherlock_anagrams('cdcd') == 5