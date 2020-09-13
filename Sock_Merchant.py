#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    final = [0]*100
    for i in ar:
        final[i-1] = final[i-1] + 1
    for j in range(100):
        final[j] = final[j]//2
    count = 0
    for pair in final:
        count = count + pair
    return(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
