import math
import os
import random
import re
import sys

def diagonalDifference(arr, n):
    sum1 = 0
    sum2 = 0
    for a in range (n):
        sum1 = sum1 + arr[a][a]
        sum2 = sum2 + arr[a][n-1-a]
    temp = abs(sum1 - sum2)
    return temp
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()