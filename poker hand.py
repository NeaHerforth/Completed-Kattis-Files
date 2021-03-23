#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s=['AH 2H 3H 4H 5H']

cards=s[0].split()
ranks=[]
for i in cards:
    ranks.append(i[0])

#Count the max rank
count={}
for i in ranks:
    count.setdefault(i,0)
    count[i]=count[i] +1

print(max(count.values()))
#Accepted