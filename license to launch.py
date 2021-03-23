#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''5
5 3 5 23 4 24 3 2 1'''

s=s.splitlines()

n=s[0]
days=[]
for i in s[1].split():
    i=int(i)
    days.append(i)
print(days)

min_day=min(days)
min_day=days.index(min_day)

print(min_day)
#Accepted - didn't accept it when the list 'days' contianed strings