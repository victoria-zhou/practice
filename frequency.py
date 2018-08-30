import math
import os
import random
import re
import sys
from collections import Counter
from collections import defaultdict


def freq_query1(queries):
    freq = Counter()
    cnt = Counter()
    result = []
    for action, value in queries:
        if action == 1:
            cnt[ freq[value] ] -= 1
            freq[value] += 1
            cnt[ freq[value] ] += 1
        elif action == 2:
            if freq[value] > 0:
                cnt[ freq[value] ] -= 1
                freq[value] -= 1
                cnt[ freq[value] ] += 1
        else:
            result.append(1 if cnt[value] > 0 else 0)
    return result

print(freq_query1(([1,2],[3,1],[1,3],[2,1],[1,5],[3,4])))


def freq_query2(queries):
    result = []
    freq_dic = defaultdict(int)
    for query in queries:
        if query[0] == 1:
            freq_dic[query[1]] += 1
        elif query[0] == 2:
            value = freq_dic.get(query[1], 0)
            if value:
                freq_dic[query[1]] = value - 1
        else:
            if query[1] in freq_dic.values():
                result.append(1)
            else:
                result.append(0)
    return result

print(freq_query2(([1,2],[3,1],[1,3],[2,1],[1,5],[3,4])))