#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''2
2
4'''

s=s.splitlines()

nCases=int(s[0])

cases=[]
for i in range(1,len(s)):
    cases.append(s[i])
print(cases)

#Nope