#!/bin/python3

import math
import os
import random
import re
import sys

def breakingRecords(scores):
    print(scores[0])
    min = scores[0]
    max = scores[0]
    count = [0,0]

    for i in scores:
        if i < min:
            min = i
            count[1] += 1
        elif i > max:
            max = i
            count[0] += 1

    return (count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
