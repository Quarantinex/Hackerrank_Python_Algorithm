import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    total = sum(arr)
    print (str(total - max(arr)) + " " + str(total - min(arr)))
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
