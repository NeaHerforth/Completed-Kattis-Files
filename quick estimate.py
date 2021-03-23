#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''3
0
10
100'''

s=s.splitlines()

n=int(s[0])

for i in range(1, len(s)):
    print(len(s[i]))