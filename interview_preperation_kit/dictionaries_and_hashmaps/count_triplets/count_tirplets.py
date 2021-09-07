#!/bin/python3

import math
import os
import random
import re
import sys

'''
# Complete the countTriplets function below.
def countTriplets(arr, r):
    triplet_table = []
    res = 0
    aux_res = 1

    for i in range(len(arr)):
        triplets = {}
        key = arr[i]
        #print("\nfor i == %d:" % i)

        for j in range(len(arr) - i):
            #print('key:\t\t', key)

            if key * r == arr[j + i]:
                if key not in triplets:
                    triplets[key] = 1
                if arr[j + i] not in triplets:
                    triplets[arr[j+i]] = 1
                else:
                    triplets[arr[j+i]] += 1
                
                if (j + i + 1) < len(arr) and arr[j+i] != arr[j+i+1]:
                    key = arr[j+i]
            print('triplets:\t', triplets)

            if len(triplets) == 3 and (((j + i + 1) < len(arr) and arr[j+i+1] not in triplets) or (j + i + 1) >= len(arr)):
                triplet_table.append(triplets)
                print('triplet_table:\t', triplet_table)
                break

    for i in triplet_table:
        counter = Counter(i)
        #print('counter for', i, ':\t', counter)
        for j in counter:
            if counter[j] >= 2:
                aux_res *= counter[j]
        if aux_res > 1:
            res += aux_res
        else:
            res += 1
        aux_res = 1
    #print('triplet_table:\t', triplet_table)
    print('res:\t', res)
    return res
'''

# Complete the countTriplets function below.
def countTriplets(arr, r):
    #print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
    #print('arr:\t', arr)
    second_numb_table = {}
    third_numb_table = {}
    num_triplets = 0

    for i in arr:
        if i in third_numb_table:
            num_triplets += third_numb_table[i]
        if i in second_numb_table:
            if i * r not in third_numb_table:
                third_numb_table[i * r] = second_numb_table[i]
            else:
                third_numb_table[i * r] += second_numb_table[i]
        
        if i * r not in second_numb_table:
            second_numb_table[i * r] = 1
        else:
            second_numb_table[i * r] += 1
        
        #print('\ni:\t', i)
        #print('second_numb_table:\t', second_numb_table)
        #print('third_numb_table:\t', third_numb_table)

    return num_triplets


#print(countTriplets([1, 5, 5, 25, 125], 5), '\n')
#print(countTriplets([1, 2, 2, 4], 2), '\n')
#print(countTriplets([1, 2, 2, 4, 4], 2), '\n')
#print(countTriplets([1, 3, 9, 9, 27, 81], 3), '\n')

'''
[1, 2, 2, 4]        = 2 #var = 1 rep_var = 2
[1, 2, 2, 2, 4]     = 3 #var = 1 rep_var = 3
[1, 2, 2, 4, 4]     = 4 #var = 2 rep_var = 2, 2
[1, 2, 2, 2, 4, 4]  = 6 #var = 2 rep_var = 3, 2
[1, 2, 2, 2, 2, 4]  = 4 #var = 1 rep_var = 4


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    #fptr.write(str(ans) + '\n')

    #fptr.close()

'''
