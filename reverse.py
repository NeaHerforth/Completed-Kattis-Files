#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''3
10
12
9'''

s=s.splitlines()
del s[0]
print(s)

for i in range(len(s)-1, -1, -1):
    print(s[i])

#Accepted