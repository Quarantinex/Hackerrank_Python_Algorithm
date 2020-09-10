#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_roof = 0
    oranges_roof = 0
    for i in range (len(apples)):
        if apples[i]>0:
            if (apples[i]+a) >= s and (apples[i]+a) <= t:
                apples_roof += 1
    for i in range (len(oranges)):
        if oranges[i]<0:
            if (oranges[i]+b) >= s and (oranges[i]+b) <= t:
                oranges_roof += 1
    print(apples_roof)
    print(oranges_roof)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
