import math
import os
import random
import re
import sys

def names_with_gmail(data_dic):
    names_list = []
    pattern = re.compile(r'@gmail.com$')
    for k,v in data_dic.items():
        #if '@gmail.com' in k:
        if pattern.search(k):
            names_list.append(v)
    return sorted(names_list)

if __name__ == '__main__':
    N = int(input())
    data = {}    
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        
        data[emailID] = firstName

print('\n'.join(names_with_gmail(data)))