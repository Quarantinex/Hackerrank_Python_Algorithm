import math
import os
import random
import re
import sys
def plusMinus(arr, n):
    count_pos = 0
    count_neg = 0
    count_zero = 0
    for i in range (n):
        if arr[i] > 0:
            count_pos += 1
        elif arr[i] < 0:
            count_neg += 1
        else:
            count_zero += 1
    print("{0:.6f}".format(count_pos/n))
    print("{0:.6f}".format(count_neg/n))
    print("{0:.6f}".format(count_zero/n))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)