#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''2
5
2'''

s=s.splitlines()

#Number of cases
n=int(s[0])

fact=[]
for i in range(1, len(s)):
    fact.append(s[i])

#find factorial
import math
for i in fact:
    factorial=str(math.factorial(int(i)))
    lastdig=factorial[-1]
    print(lastdig)

#Accepted