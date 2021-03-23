#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''4 4 3 3
5 4 3 5
5 5 2 4
5 5 5 1
4 4 4 4'''

s=s.splitlines()

results=[]
for i in range(len(s)):
    line=s[i].split()
    sum=0
    for x in line:
        sum=sum+ int(x)
    results.append(sum)

winner=max(results)
winner_index=results.index(winner)+1
print(winner_index, winner)

