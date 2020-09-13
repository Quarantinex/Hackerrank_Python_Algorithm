#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    count = 0
    counter = 0

    for step in path:
        if step == 'D':
            counter -= 1
        if step == 'U':
            counter += 1
            if counter == 0:
                count += 1
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
