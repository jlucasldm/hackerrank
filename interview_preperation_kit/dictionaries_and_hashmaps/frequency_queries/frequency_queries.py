#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    #print(queries)
    res = {}
    ret = []

    for i in queries:
        if i[0] == 1:
            if i[1] not in res: 
                res[i[1]] = 1
            else:
                res[i[1]] += 1
        elif i[0] == 2:
            if i[1] in res and res[i[1]] > 0:
                res[i[1]] -= 1
        else:
            if i[0] == 3:
                if i[1] not in res.values():
                    ret.append(0)
                    #print(0)
                else:
                    ret.append(1)
                    #print(1)
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
