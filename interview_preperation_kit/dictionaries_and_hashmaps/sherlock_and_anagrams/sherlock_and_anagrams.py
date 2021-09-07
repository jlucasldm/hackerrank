#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    substrings = dict()

    print('size:\t', len(s))
    for i in range(len(s)):
        #print('i:\t', i)
        for j in range(len(s) - i):
            substring = s[i: j + 1 + i]
            #print('substring:\t\t', substring)
            substring = "".join(sorted(substring))
            #print("substring sorted:\t", substring)
            if substring not in substrings:
                substrings[substring] = 1
            else:
                substrings[substring] += 1

    #print("substrings: ", substrings)
    count = 0
    for i in substrings:
        res = substrings[i]

        if res > 1:
            count += (res * (res - 1) / 2)
    
    print(int(count))
    return int(count)


#sherlockAndAnagrams('abba')
#sherlockAndAnagrams('abcd')

'''
akkkka (5-0)
aa              1
ak,ka           2
akk,kka         3
akkk,kkka       4
akkkk,kkkka     5
'''


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
