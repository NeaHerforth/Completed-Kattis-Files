#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''2
4
24 13 89 37
6
7 30 41 14 39 42'''

s=s.splitlines()

cases=int(s[0])

stores=[]
i=2
while i<len(s):
    positions=[]
    for x in s[i].split():
        positions.append(int(x))
    stores.append(positions)
    i=i+2


for i in stores:
    distance=(max(i)-min(i))*2
    print(distance)

#Accepted