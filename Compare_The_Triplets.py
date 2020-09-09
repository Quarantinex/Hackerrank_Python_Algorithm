import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    tempa = 0
    tempb = 0
    for n in range(3):
        if a[n] > b[n]:
            tempa+=1
        elif a[n] < b[n]:
            tempb+=1
    return(tempa, tempb)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()