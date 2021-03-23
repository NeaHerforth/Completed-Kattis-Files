#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''3
213
102
45'''

s=s.splitlines()

n=int(s[0])

result=0
for i in range(1, len(s)):
    number=int(s[i][:-1])
    expo=int(s[i][-1])
    p=number**expo
    result=result+p
print(result)
#Accepted