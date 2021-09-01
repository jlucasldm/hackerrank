#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    # Write your code here
    #print("set(s1):\t\t", set(s1))
    #print("set(s2):\t\t", set(s2))
    #print("set(s1) and set(s2):\t", set(s1).intersection(set(s2)))
    if set(s1).intersection(set(s2)):
        return "YES"
    else:
        return "NO"


#twoStrings("hello", "world")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
