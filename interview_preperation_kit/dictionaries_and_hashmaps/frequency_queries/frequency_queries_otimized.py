#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the freqQuery function below.
def freqQuery(queries):
    #print(queries)
    res = Counter()
    freq_res = Counter()
    ret = []

    for i in queries:
        #print('op: ', i)
        if i[0] == 1:
            freq_res[res[i[1]]] -= 1
            res[i[1]] += 1
            freq_res[res[i[1]]] += 1
        elif i[0] == 2:
            if res[i[1]] > 0:
                freq_res[res[i[1]]] -= 1
                res[i[1]] -= 1
                freq_res[res[i[1]]] += 1
        else:
            if i[0] == 3:
                if freq_res[i[1]] > 0:
                    ret.append(1)
                    #print(1)
                else:
                    ret.append(0)
                    #print(0)
        #print('res:\t\t', res)
        #print('freq_res:\t', freq_res)
    return ret

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    #fptr.write('\n'.join(map(str, ans)))
    #fptr.write('\n')

    #fptr.close()
