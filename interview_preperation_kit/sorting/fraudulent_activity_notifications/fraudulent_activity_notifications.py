#!/bin/python3

import math
import os
import random
import re
import sys
import statistics
from collections import deque
import bisect

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#


def activityNotifications(expenditure, d):
    # Write your code here
    #print("expenditure:\t", expenditure)
    elements = sorted(expenditure[0:d])
    #print("elements:\t", elements,"\n\n")
    notifications = 0

    for i in range(d, len(expenditure)):
        #print("i:\t", i)
        #print("mediana:\t", median(elements, d))
        #print("expenditure[i]:\t", expenditure[i])
        if expenditure[i] >= 2*statistics.median(elements, d):
            notifications += 1
        #print("antes pop:\t", elements)
        elements.pop(bisect.bisect_left(elements, expenditure[i-d]))
        #print("apos pop:\t",elements)
        bisect.insort_right(elements, expenditure[i])
        #print("apos insert:\t",elements, '\n')

    #print(notifications)
    return notifications

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    #fptr.write(str(result) + '\n')

    #fptr.close()
