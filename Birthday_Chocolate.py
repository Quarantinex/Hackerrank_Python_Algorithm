import math
import os
import random
import re
import sys

def birthday(s, d, m):
    temp = 0
    count = 0

    for i in range (len(s)+1-m):
        for x in range (m):
            print(s[i+x])
            temp = temp + s[i+x]
        if temp == d:
            count += 1
        temp = 0
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
