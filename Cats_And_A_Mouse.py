import math
import os
import random
import re
import sys

def catAndMouse(x, y, z):
    cat1 = abs(z-x)
    cat2 = abs(z-y)

    if cat1 == cat2:
        return ("Mouse C")
    elif cat1 < cat2:
        return ("Cat A")
    elif cat2 < cat1:
        return ("Cat B")
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
