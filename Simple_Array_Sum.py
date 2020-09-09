import os
import sys
def simpleArraySum(ar, ar_count):
    temp = 0
    for n in range (ar_count):
        temp = temp + ar[n]
    return temp

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar, ar_count)

    fptr.write(str(result) + '\n')

    fptr.close()