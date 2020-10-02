#!/bin/python3
n = int(input())
ps = [int(x) for x in input().split()]

for x in range(1, n+1):
    for y in range(n):
        if ps[ps[y]-1] == x:
            print(y+1)
            break