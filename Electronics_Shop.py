#!/bin/python3

import os
import sys

def getMoneySpent(keyboards, drives, b):
    cost = [-1]
    for k in keyboards:
        for d in drives:
            if (k+d) <= b:
                cost.append(k+d)
    return (max(cost))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
